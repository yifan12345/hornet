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
from tasks.models import TestTask, TaskCaseRelevance, TestResult
from backend.settings import BASE_DIR
from tasks.task_running.task_running import Task

TEST_DATA = os.path.join(BASE_DIR, "tasks", "task_running", "test_data.json")
TEST_CASE = os.path.join(BASE_DIR, "tasks", "task_running", "test_case.py")

router = Router(tags=["reports"])


@router.get("/{report_id}/", auth=None)
def report_detail(request, report_id: int):
    """
    获取任务详情
    auth=None 该接口不需要认证
    """
    result = get_object_or_404(TestResult, pk=report_id)
    return response(item=result)


@router.delete("/{report_id}/", auth=None)
def get_task_delete(request, report_id: int):
    """删除任务"""
    result = get_object_or_404(TestResult, id=report_id)
    result.delete()
    return response()
