from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields
import json


class BaseForm(forms.Form):
    username = fields.CharField(
        max_length=32,
    )
    age = fields.IntegerField(
        min_value=0,
        max_value=100,
    )


def base(request):
    if request.method == "GET":
        obj = BaseForm()
        return render(request, "baseByIframe.html", locals())
    else:
        ret = {'status': 'ok', 'msg': None}
        obj = BaseForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            # ajax不能直接用redirect跳轉
            # return redirect('https://www.youtube.com/?gl=TW&hl=zh-tw')
            return HttpResponse(json.dumps(ret))
        else:
            print(obj.errors, type(obj.errors))
            ret['status'] = 'bad'
            ret['msg'] = obj.errors
            return HttpResponse(json.dumps(ret))
