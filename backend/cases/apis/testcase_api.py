from ninja import Router, Query
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from backend.common import response, Error
from cases.models import Module,TestCase
from projects.models import Project
from cases.apis.api_scheam import CaseIn, ProjectIn

router = Router(tags=["cases"])


@router.post("/", auth=None)
def create_case(request, data: CaseIn):
    """创建用例"""
    project = Module.objects.filter(id=data.module_id)
    if len(project) == 0:
        return response(error=Error.MODULE_NOT_EXIST)

    case = TestCase.objects.create(**data.dict())
    return response(item=model_to_dict(case))

