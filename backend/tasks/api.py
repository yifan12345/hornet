import os
from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from backend.common import response, Error
from cases.models import TestCase
from projects.models import Project
from tasks.api_scheam import TaskIn
from tasks.models import TestTask,TaskCaseRelevance
from backend.settings import BASE_DIR

TEST_DATA = os.path.join(BASE_DIR,"tasks","task_running","test_data.json")
router = Router(tags=["tasks"])


@router.post("/", auth=None)
def create_tasks(request, data: TaskIn):
    """创建任务"""
    global task_dict
    project = get_object_or_404(Project,pk=data.project)
    task = TestTask.objects.create(project=project,name=data.name,describe=data.describe)
    cases = []
    for case in data.case:
        TaskCaseRelevance.objects.create(task_id=task.id,case_id=case)
        case = TestCase.objects.get(pk=case)
        cases.append({
            "case":case.id,
            "module":case.module_id
        })

        task_dict = model_to_dict(task)
        task_dict["cases"] = cases
    return response(item=task_dict)
