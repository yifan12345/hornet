from typing import Any
from ninja import Schema


class ProjectIn(Schema):
    project_id : int


class ModuleIn(Schema):
    """模块入参"""
    name: str
    project_id: int
    parent_id: int = 0


class ModuleOut(Schema):
    """
    模块出参
    """
    id: str
    name: str
    parent_id: int
    Project_id: int


class CaseIn(Schema):
    """模块入参"""
    name:str
    module_id:int
    url:str
    method:str
    header:dict
    params_type:str
    params_body:dict
    response:str
    assert_type:str
    assert_text:str


class CaseDebugIn(Schema):
    url:str
    method:str
    header:dict
    params_type:str
    params_body:dict


class CaseAssertIn(Schema):
    response:str
    assert_type:str
    assert_text:str


class CaseOut(Schema):
    name:str
    module_id:int
    url:str
    method:str
    create_time:Any
    update_time:Any

