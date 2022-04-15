import json
import requests
from typing import List
from ninja import Router, Query
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from ninja.pagination import paginate
from backend.common import response, Error
from backend.pagination import CustomPagination
from cases.models import Module,TestCase
from cases.apis.api_scheam import CaseIn, CaseDebugIn, CaseAssertIn, CaseOut

router = Router(tags=["cases"])


@router.post("/", auth=None)
def create_case(request, data: CaseIn):
    """创建用例"""
    module = Module.objects.filter(id=data.module_id)
    if len(module) == 0:
        return response(error=Error.MODULE_NOT_EXIST)

    case = TestCase.objects.create(**data.dict())
    return response(item=model_to_dict(case))


@router.put("/{case_id}/", auth=None)
def get_case_update(request, case_id: int,payload:CaseIn):
    """更新用例"""
    case = get_object_or_404(TestCase,id=case_id)
    for attr,value in payload.dict().items():
        setattr(case,attr,value)
        case.save()

    return response()

@router.delete("/{case_id}/", auth=None)
def get_case_delete(request, case_id: int):
    """删除用例"""
    case = get_object_or_404(TestCase, id=case_id)
    case.is_delete = True
    case.save()

    return response()


# 未完成
@router.get("/list", auth=None,response=List[CaseOut])
@paginate(CustomPagination)
def get_case_list(request, **kwargs):
    """获取用例列表"""

    return TestCase.objects.filter(is_delete=False).all()


@router.get("/{case_id}/", auth=None)
def get_case_details(request, case_id: int):
    """获取单个的用例详情"""
    case = get_object_or_404(TestCase, id=case_id)
    if case.is_delete is True:
        return response(error=Error.CASE_ALREADY_DELETE)
    data = {
        "id":case.id,
        "name": case.name,
        "module_id": case.module_id,
        "url": case.url,
        "method": case.method,
        "header": case.header,
        "params_type": case.params_type,
        "params_body": case.params_body,
        "response": case.response,
        "create_time": case.create_time,
        "update_time": case.update_time
    }
    return response(item=data)



@router.post("/debug", auth=None)
def debug_case(request, data: CaseDebugIn):
    """用例调试，发送请求"""
    url = data.url
    method = data.method
    header = data.header
    params_type = data.params_type
    params_body = data.params_body

    resp = ""
    if method not in ["get","post","put","delete"]:
        return response(error=Error.CASE_MODULE_ERROR)
    if params_type not in ["params","form","json"]:
        return response(error=Error.CASE_PARAMS_ERROR)

    if method== "get":
        resp = requests.get(url,headers=header,params=params_body).text

    if method == "post":
        if params_type == "form":
            resp = requests.post(url, headers=header, data=params_body).text
        elif params_type == "json":
            resp = requests.post(url, headers=header, json=params_body).text
        else:
            return response(error=Error.CASE_PARAMS_ERROR)

    if method == "put":
        if params_type == "form":
            resp = requests.put(url, headers=header, data=params_body).text
        elif params_type == "json":
            resp = requests.put(url, headers=header, json=params_body).text
        else:
            return response(error=Error.CASE_PARAMS_ERROR)

    if method == "delete":
        if params_type == "form":
            resp = requests.delete(url, headers=header, data=params_body).text
        elif params_type == "json":
            resp = requests.delete(url, headers=header, json=params_body).text
        else:
            return response(error=Error.CASE_PARAMS_ERROR)


    print(resp)
    #case = TestCase.objects.create(**data.dict())
    return response(item={"response":resp})

@router.post("/assert", auth=None)
def assert_case(request, data: CaseAssertIn):
    """用例断言"""
    resp = data.response
    assert_type = data.assert_type
    assert_text = data.assert_text
    if assert_type not in ["include","equal"]:
        return response(error=Error.CASE_ASSERT_TYPE_ISNONE)
    if assert_type == "include":
        if assert_text in resp:
            return response()
        else:
            return response(success=False)
    elif assert_type == "equal":
        if assert_text == resp:
            return response()
        else:
            return response(success=False)
    else:
        return response(error=Error.CASE_ASSERT_TYPE_ISNONE)
