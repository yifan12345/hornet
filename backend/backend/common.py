
class Error:
    """
    自定义错误码，错误信息
    """
    USER_OR_PAWD_NULL = {"10010":"用户名密码不能为空"}
    USER_OR_PAWD_ERROR = {"10011":"用户名密码错误"}
    PAWD_ERROR = {"10012":"两次密码不一致"}
    USER_EXIST = {"10013":"用户名已存在"}


def response(success:bool=True,error=None,result=[])->dict:
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

    resp_dict={
        "success":success,
        "error":{
            "code":error_code,
            "msg":error_msg,
        },
        "result":result

    }
    return resp_dict
