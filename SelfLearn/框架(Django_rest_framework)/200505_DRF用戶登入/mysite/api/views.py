from django.shortcuts import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from api import models
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

# 訂單資料
ORDER_DICT = {
    1: {
        'name': "jamie",
        'age': 18,
        'gender': '男',
        'content': '...',
    },
    2: {
        'name': "jack",
        'age': 18,
        'gender': '男',
        'content': '***',
    },
}


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    # hashlib.md5(<<字節>>)
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))  # 加鹽
    return m.hexdigest()  # .hexdigest()返回十六進制字符串


class AuthView(APIView):
    """
    用於用戶登入
    """
    # 通常用戶登入是用post請求
    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用戶名或密碼錯誤'

            # 登入成功 => 為用戶創造token
            token = md5(user)
            # 存在就更新，不存在就創建
            models.UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '請求錯誤'

        return JsonResponse(ret)


class Authtication(BaseAuthentication):
    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用戶驗證失敗')
        # 在rest framework內會自動將return的這兩個字段賦值給request，以供操作使用。
        # 會賦值給(request.user, request.auth)
        return (token_obj.user, token_obj)


class OrderView(APIView):
    """
    訂單相關業務
    """
    # 加入認證
    authentication_classes = [Authtication, ]

    # GET：取出訂單(一項或多項)
    def get(self, request, *args, **kwargs):
        # self.dispatch()
        ret = {'code': 1000, 'msg': None}
        # 之後資料庫容易出錯，最好都用try包起來。
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '請求錯誤'

        return JsonResponse(ret)
