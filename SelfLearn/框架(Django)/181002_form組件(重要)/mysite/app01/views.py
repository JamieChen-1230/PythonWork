from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields
from app01 import models


# ----------------------------------基礎表單組件(form)----------------------------------
class Mybasisform(forms.Form):
    user = fields.CharField(
        # required=True 表不能為空
        max_length=18, min_length=6, required=True,
        # 錯誤信息
        error_messages={
            'required': '用戶名不能為空',
            'max_length': '太長拉~',
            'min_length': '太短拉~',
        }
    )
    pwd = fields.CharField(
        min_length=10, required=True,
        error_messages={
            'required': '密碼不能為空',
            'min_length': '太短拉~',
        }
    )
    age = fields.IntegerField(
        required=True,
        error_messages={
            'required': '年齡不能為空',
            'invalid': '必須為數字格式',  # invalid 所有的格式錯誤都是用它
        }
    )
    email = fields.EmailField(
        required=True,
        error_messages={
            'required': '信箱不能為空',
            'invalid': '信箱格式錯誤',  # invalid 所有的格式錯誤都是用它
        }
    )


def basis_form(request):
    if request.method == 'GET':
        f1 = Mybasisform()  # 可以透過form對象自動生成html表單
        return render(request, 'basis_form.html', locals())
    else:
        # 1.檢查是否為空
        # 2.檢查格式是否正確
        f1 = Mybasisform(request.POST)  # 會自動跟類裡面相同name的進行驗證
        judge = f1.is_valid()  # 判斷是否全部驗證成功
        if judge:
            print('驗證成功', f1.data)  # 已經驗證過的數據
            return HttpResponse('ok', f1.data)
        else:
            print('驗證失敗', f1.errors)  # 錯誤
            return render(request, 'basis_form.html', locals())


# ----------------------------------基礎form組件結合sql應用----------------------------------
class UserForm(forms.Form):
    username = fields.CharField(required=True, max_length=32)
    email = fields.EmailField(required=True, max_length=32)


def users(request):
    user_list = models.UserInfo.objects.all()
    return render(request, 'basis_form&sql/users.html', locals())


def add_user(request):
    if request.method == "GET":
        obj = UserForm()
        return render(request, 'basis_form&sql/add_user.html', locals())
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            # 須讓sql欄位名與form組件欄位名相同才可這樣創建
            models.UserInfo.objects.create(**obj.cleaned_data)
            return redirect("/app01/users.html/")
        else:
            return render(request, 'basis_form&sql/add_user.html', locals())


def edit_user(request, nid):
    if request.method == "GET":
        user_obj = models.UserInfo.objects.filter(id=nid).values('username', 'email').first()
        # print(user_obj)
        obj = UserForm(user_obj)
        return render(request, "basis_form&sql/edit_user.html", locals())
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            models.UserInfo.objects.filter(id=nid).update(**obj.cleaned_data)
            return redirect("/app01/users.html/")
        else:
            return render(request, 'basis_form&sql/edit_user.html', locals())
