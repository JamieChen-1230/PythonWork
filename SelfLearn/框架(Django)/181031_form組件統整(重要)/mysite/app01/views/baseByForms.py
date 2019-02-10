from django.shortcuts import render, HttpResponse, redirect
from django import forms
from django.forms import fields, widgets
from django.core.validators import RegexValidator


class BaseForm(forms.Form):
    """
    required：是否必填
    error_messages：錯誤提示(要透過{{ obj.errors.user.0 }}調用)
    widget：訂製html插件(重要)
    label：訂製標籤名(要透過{{ obj.user.label }}調用)
    initial：默認值
    validators：自訂製驗證規則
    disabled：是否禁止編輯
    """
    name = forms.CharField(
        initial="jamie",
        max_length=32,
        min_length=3,
        required=True,
        error_messages={
            "invalid": "請輸入正確格式",  # 所有格式錯誤都用invalid
            "min_length": "請輸入最少3個字元",
        }
    )        
    age = forms.IntegerField(
        initial=18,
        max_value=100,
        min_value=0,
        error_messages={
            "invalid": "請輸入數字格式",
            "min_value": "最好會有負的年齡",
        }
    )   
    email = forms.EmailField(initial="a127925061@yahoo.com",)    
    tall = forms.DecimalField(initial=178.87,)
    file = forms.FileField(required=False,)
    # 單選
    city = fields.ChoiceField(
        choices=[(1, "台北"), (2, "台中"), (3, "高雄")],  # (value, 顯示文字)
        initial=3,  # 默認value=3
    )
    # 多選
    hobby = fields.MultipleChoiceField(
        choices=[(1, "籃球"), (2, "電動"), (3, "小說")],  # (value, 顯示文字)
        initial=[1, 2],
    )
    birth = fields.DateField(initial="2000-01-01")  # 格式：2015-09-01
    # datetime = fields.DateTimeField()  # 格式：2015-09-01 11:12
    radio = fields.ChoiceField(
        choices=[(1, 'man'), (2, 'woman')],
        widget=widgets.RadioSelect(),
        initial=1,
    )
    checkbox = fields.MultipleChoiceField(
        choices=[(1, 'man'), (2, 'woman')],
        widget=widgets.CheckboxSelectMultiple(),
        initial=[1, 2],
    )
    myField = fields.CharField(
        # 自定義正則(一)
        # validators可設置多個RegexValidator
        # RegexValidator(正則, 錯誤信息)
        validators=[RegexValidator(r"^[0-9]+$", "請輸入數字"), RegexValidator(r"^87[0-9]+$", "請以87開頭")],
        initial="87123",
    )
    # 自定義正則(二)
    # fields.RegexField(正則)，只可設置單個正則
    myField2 = fields.RegexField(
        r"^[0-9]+$",
        error_messages={
            "invalid": "請輸入數字",
        },
        initial="123456",
    )


def base(request):
    if request.method == "GET":
        obj = BaseForm()
        return render(request, "baseByForms.html", locals())
    else:
        # request.FILES用於接收files
        obj = BaseForm(request.POST, request.FILES)
        if obj.is_valid():
            print(obj.cleaned_data)
            return render(request, "baseByForms.html", locals())
        else:
            return render(request, "baseByForms.html", locals())