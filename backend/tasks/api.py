import ast
import os
import json
from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from backend.common import response, Error
from cases.models import TestCase
from projects.models import Project
from tasks.api_scheam import TaskIn
from tasks.models import TestTask, TaskCaseRelevance
from backend.settings import BASE_DIR
from tasks.task_running.test_result import save_test_result

TEST_DATA = os.path.join(BASE_DIR, "tasks", "task_running", "test_data.json")
TEST_CASE = os.path.join(BASE_DIR, "tasks", "task_running", "test_case.py")

router = Router(tags=["tasks"])


@router.post("/", auth=None)
def create_tasks(request, data: TaskIn):
    """创建任务"""
    project = get_object_or_404(Project, pk=data.project)
    task = TestTask.objects.create(project=project, name=data.name, describe=data.describe)
    cases = []
    for case in data.case:
        TaskCaseRelevance.objects.create(task_id=task.id, case_id=case)
        case = TestCase.objects.get(pk=case)
        cases.append({
            "case": case.id,
            "module": case.module_id
        })

        task_dict = model_to_dict(task)
        task_dict["cases"] = cases
    return response(item=task_dict)


@router.post("/{task_id}/running", auth=None)
def running(request, task_id: int):
    """执行任务"""
    task = get_object_or_404(TestTask, pk=task_id)
    print("1_读取测试用例")
    relevace = TaskCaseRelevance.objects.filter(task_id=task.id)

    test_case = {}
    for rel in relevace:
        print(rel.case_id)
        try:
            case = TestCase.objects.get(pk=rel.case_id, is_delete=False)
            # ast.literal_eval 转换str为dict
            # dict_header = ast.literal_eval(case.header)
            # dict_params_body = ast.literal_eval(case.params_body)
            params_body = case.params_body.replace("\'","\"")
            dict_header = json.loads(case.header)
            dict_params_body = json.loads(params_body)

            test_case[case.name] = {
                "url": case.url,
                "method": case.method,
                "header": dict_header,
                "params_type": case.params_type,
                "params_body": dict_params_body,
                "assert_type": case.assert_type,
                "assert_text": case.assert_text
            }
        except TestCase.DoesNotExist:
            pass
    print("2_用例数据写到test_json文件")
    with open(TEST_DATA, "w") as f:
        f.write(json.dumps(test_case))

    # 执行用例
    print("3_执行用例")
    os.system(f"python {TEST_CASE}")
    # 读取测试结果
    print("4_保存测试结果")
    save_test_result(task_id)
    return response()
