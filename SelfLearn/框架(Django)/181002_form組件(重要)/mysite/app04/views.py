from django.shortcuts import render, redirect, HttpResponse
from django import forms
from django.forms import fields, widgets
from app01 import models
import json
from django.core.exceptions import ValidationError


class Expansion(forms.Form):
    username = fields.CharField()
    email = fields.EmailField()

    # ---------自定義單體驗證方法(clean_加字段名)，必須有返回值---------
    # clean_方法只能對當前字段進行驗證
    def clean_username(self):
        """
        單體錯誤信息，存放在各自字段名(username)
        """
        v = self.cleaned_data['username']  # 當前用戶提交的username
        if models.UserInfo.objects.filter(username=v).count():  # 判斷有沒有重名
            # 有重名，錯誤
            raise ValidationError('用戶名已存在')  # 必須使用ValidationError拋出錯誤
        return v

    # ---------自定義全體驗證方法(clean)，必須有返回值---------
    def clean(self):
        """
        整體錯誤信息，存放在__all__
        """
        value_dict = self.cleaned_data
        v1 = value_dict.get('username')
        v2 = value_dict.get('email')
        if v2.startswith(v1):
            raise ValidationError('整體錯誤信息，信箱和用戶名過於近似')
        return value_dict


def expansion(request):
    if request.method == 'GET':
        obj = Expansion()  # 生成html標籤
        return render(request, 'expansion.html', locals())
    else:
        ret = {'status': 'ok', 'msg': None}
        obj = Expansion(request.POST)
        if obj.is_valid():  # 驗證
            print(obj.cleaned_data)
            # ajax不能直接用redirect跳轉
            # return redirect('https://www.youtube.com/?gl=TW&hl=zh-tw')
            return HttpResponse(json.dumps(ret))
        else:
            print(obj.errors, type(obj.errors))
            # print(obj.errors.as_ul(), type(obj.errors.as_ul()))
            # print(obj.errors.as_json(), type(obj.errors.as_json()))
            ret['status'] = 'bad'
            ret['msg'] = obj.errors
            return HttpResponse(json.dumps(ret))

