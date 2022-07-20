import os
from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from backend.common import response
from tasks.models import TestResult
from backend.settings import BASE_DIR

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
    return response(item=model_to_dict(result))


@router.delete("/{report_id}/", auth=None)
def delete_result(request, report_id: int):
    """删除报告"""
    result = get_object_or_404(TestResult, id=report_id)
    result.delete()
    return response()
