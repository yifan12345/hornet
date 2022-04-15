class Error:
    """
    自定义错误码，错误信息
    """
    USER_OR_PAWD_NULL = {"10010": "用户名密码不能为空"}
    USER_OR_PAWD_ERROR = {"10011": "用户名密码错误"}
    PAWD_ERROR = {"10012": "两次密码不一致"}
    USER_EXIST = {"10013": "用户名已存在"}

    PROJECT_NAME_EXIST = {"10021": "项目名称已存在"}
    PROJECT_NOT_EXIST = {"10022": "项目不存在"}
    PROJECT_ALREADY_DELETE = {"10023": "项目已被删除"}

    FILE_TYPE_ERROR = {"10031": "文件类型错误"}
    FILE_SIZE_ERROR = {"10032": "超出文件大小"}

    MODULE_NAME_EXIST = {"10041": "模块名称已存在"}
    MODULE_NOT_EXIST = {"10042": "模块不存在"}
    MODULE_ALREADY_DELETE = {"10043": "模块已被删除"}
    MODULE_NOT_EDIT = {"10044": "更新失败，不能更改自己子节点的节点"}
    MODULE_PITCH_EXIST = {"10045":"节点数据错误，请查看"}


def response(success: bool = True, error=None, item=None) -> dict:
    """
    定义同一返回格式
    """
    if error is None:
        error_code = ""
        error_msg = ""
    else:
        success = False
        error_code = list(error.keys())[0]
        error_msg = list(error.values())[0]

    resp_dict = {
        "success": success,
        "error": {
            "code": error_code,
            "msg": error_msg,
        },
        "item": item

    }
    return resp_dict
