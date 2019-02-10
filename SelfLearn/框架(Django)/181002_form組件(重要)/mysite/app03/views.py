from django.shortcuts import render, redirect, HttpResponse
from django import forms
from django.forms import fields, widgets
from app01 import models
import json


class AjaxForm(forms.Form):
    price = fields.IntegerField(max_value=100)
    user_id = fields.IntegerField(
        widget=widgets.Select(choices=[(0, 'jamie'), (1, 'joker'), (2, 'jj'), ])
    )


def ajax(request):
    if request.method == 'GET':
        obj = AjaxForm()  # 生成html標籤
        return render(request, 'ajax.html', locals())
    else:
        ret = {'status': 'ok', 'msg': None}
        obj = AjaxForm(request.POST)
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

