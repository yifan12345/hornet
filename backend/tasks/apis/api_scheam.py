from ninja import Schema
from typing import List, Any


class TaskIn(Schema):
    """
    任务入参
    """
    project: int
    name: str
    describe: str = None
    case: list


class ResultOut(Schema):
    name: str
    passed: int
    error: int
    failure: int
    skipped: int
    tests: int
    run_time: float
    result: str
    create_time: any


class TaskOut(Schema):
    """项目出参"""
    id: int
    name: str
    describe: str
    image: str
    create_time: Any
