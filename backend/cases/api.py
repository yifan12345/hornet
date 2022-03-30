from ninja import Router
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from typing import List
from ninja.pagination import paginate, LimitOffsetPagination, PageNumberPagination
from backend.common import response, Error
from backend.pagination import CustomPagination
from cases.models import Module
from projects.models import Project
from cases.api_scheam import ModuleIn
from cases.api_scheam import ModuleOut

router = Router(tags=["cases"])


@router.post("/", auth=None)
def create_module(request, data: ModuleIn):
    """创建模块"""
    project = Project.objects.filter(id=data.project_id)
    if project ==0:
        return response(error=Error.PROJECT_NOT_EXIST)
    module = Module.objects.filter(name=data.name, project_id=data.project_id)
    if len(module) > 0:
        return response(error=Error.MODULE_NAME_EXIST)
    module = Module.objects.create(**data.dict())
    return response(item=model_to_dict(module))
