from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields
from app01 import models
import json
from django.core.exceptions import ValidationError


class ExpansionForm(forms.Form):
    username = fields.CharField()
    age = fields.IntegerField()

    # ---------自定義單體驗證方法(clean_加字段名)，必須有返回值---------
    # clean_方法只能對當前字段進行驗證
    def clean_username(self):
        """
        單體錯誤信息，存放在各自字段名(username)
        :return: 用戶提交的username
        """
        v = self.cleaned_data['username']  # 當前用戶提交的username
        if models.UserInfo.objects.filter(username=v).count():  # 判斷有沒有重名
            # 有重名則拋出錯誤
            raise ValidationError('用戶名已存在')  # 必須使用ValidationError拋出錯誤
        return v

    # ---------自定義全體驗證方法(clean)，必須有返回值---------
    def clean(self):
        """
        整體錯誤信息，存放在__all__
        """
        value_dict = self.cleaned_data
        v1 = value_dict.get('username')
        v2 = value_dict.get('age')
        print(v1, v2)

        if v1 and v2:
            if v1.startswith("j") or v2 < 0:
                raise ValidationError('不符合規則')

        return value_dict


def expansion(request):
    if request.method == "GET":
        obj = ExpansionForm()
        return render(request, "expansionByForms.html", locals())
    else:
        obj = ExpansionForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            models.UserInfo.objects.create(**obj.cleaned_data)
            return render(request, "expansionByForms.html", locals())
        else:
            if obj.errors.get("__all__"):
                errorAll = obj.errors["__all__"]
            return render(request, "expansionByForms.html", locals())
