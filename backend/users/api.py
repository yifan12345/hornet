from django.contrib import auth
from django.contrib.auth.models import User
from ninja import Router, Schema
from backend.common import response, Error
from django.contrib.sessions.models import Session

router = Router(tags=["users"])


class RegisterIn(Schema):
    username: str
    password: str
    confirm_password: str


@router.post("/register", auth=None)
def user_register(request, payload: RegisterIn):
    """
    用户注册
    """
    username = payload.username
    password1 = payload.password
    password2 = payload.confirm_password

    if password1 != password2:
        return response(error=Error.PAWD_ERROR)
    try:
        User.objects.get_by_natural_key(username)
    except User.DoesNotExist:
        pass
    else:
        return response(error=Error.USER_EXIST)
    user = User.objects.create_user(username=username, password=password1)
    user_info = {
        "id": user.id,
        "username": user.username
    }
    return response(result=user_info)


class LoiginIn(Schema):
    username: str
    password: str


@router.post("/login",auth=None)
def user_login(request, payload: LoiginIn):
    """
    用户登录
    """
    username = payload.username
    password = payload.password
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active is True:
        auth.login(request, user)  # 向session表创建一条数据
        token = Session.objects.last()
        user_info = {
            "id": user.id,
            "username": user.username,
            "token": token.session_key
        }
        return response(result=user_info)
    else:
        return response(error=Error.USER_OR_PAWD_ERROR)
