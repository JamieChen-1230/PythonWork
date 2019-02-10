from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields, widgets
from app01 import models


class DynamicForm(forms.Form):
    # 因為屬性是靜態字段，所以在程序啟動時就會給一塊內存去加載，除非重啟，否則不會動態更改
    username = fields.IntegerField(
        # widget=widgets.Select(choices=[(0, 'jamie'), (1, 'joker'), (2, 'jj'), ])
        # widget=widgets.Select(choices=models.UserInfo.objects.values_list('id', 'username'))
        widget=widgets.Select(),
    )
    age = fields.IntegerField(
        initial=18,
        min_value=1,
    )

    def __init__(self, *args, **kwargs):
        # super一定要寫在上面，用來拷貝所有的靜態字段複製給self.fields
        super(DynamicForm, self).__init__(*args, **kwargs)
        # 每次調用obj時就會執行一次init，所以在此更新choices，實現動態更新
        self.fields["username"].widget.choices = models.UserInfo.objects.all().values_list("id", "username")


def dynamic(request):
    if request.method == "GET":
        obj = DynamicForm()
        return render(request, "dynamicByForms.html", locals())
    else:
        obj = DynamicForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            # 把id轉換成對應的username
            obj.cleaned_data["username"] = models.UserInfo.objects.get(id=obj.cleaned_data["username"]).username
            print(obj.cleaned_data["username"])
            # 須讓sql欄位名與form組件欄位名相同才可這樣創建
            models.UserInfo.objects.create(**obj.cleaned_data)
            return render(request, "dynamicByForms.html", locals())
        else:
            return render(request, "dynamicByForms.html", locals())
