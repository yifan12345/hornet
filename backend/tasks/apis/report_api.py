import os
from typing import List

from ninja import Router
from django.db.utils import IntegrityError
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate

from backend.common import response, Error
from backend.pagination import CustomPagination
from cases.models import TestCase
from projects.api_scheam import ProjectOut
from projects.models import Project
from tasks.apis.api_scheam import TaskIn, ResultOut
from tasks.models import TestTask, TaskCaseRelevance
from backend.settings import BASE_DIR
from tasks.task_running.task_running import Task

TEST_DATA = os.path.join(BASE_DIR, "tasks", "task_running", "test_data.json")
TEST_CASE = os.path.join(BASE_DIR, "tasks", "task_running", "test_case.py")

router = Router(tags=["reports"])

@router.get("/list", auth=None,response=List[ResultOut])
@paginate(CustomPagination)
def get_project_list(request, **kwargs):
    """获取项目列表"""

    return Project.objects.filter(is_delete=False).all()


@router.get("/{task_id}/", auth=None)
def get_detail(request, task_id: int):
    """获取任务详情"""
    task = get_object_or_404(TestTask, pk=task_id)
    if task.is_delete is True:
        return response(error=Error.TASK_ALREADY_DELETE)
    relevance = TaskCaseRelevance.objects.filter(task_id=task_id)
    case_list = []
    for r in relevance:
        print(r.case_id)
        case_list.append(r.case_id)
    task_dict = model_to_dict(task)
    task_dict["cases"] = case_list
    return response(item=task_dict)


@router.delete("/{task_id}/", auth=None)
def get_task_delete(request, task_id: int):
    """删除用例"""
    task = get_object_or_404(TestTask, id=task_id)
    task.is_delete = True
    task.save()

    return response()
