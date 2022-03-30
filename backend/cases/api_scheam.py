from typing import Any
from ninja import Schema


class ModuleIn(Schema):
    """项目入参"""
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
