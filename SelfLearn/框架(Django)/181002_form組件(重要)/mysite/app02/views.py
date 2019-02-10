from django.shortcuts import render
from django import forms
from django.forms import fields, widgets
from app01 import models


class DetailedForm(forms.Form):
    """
    required：是否必填
    error_messages：錯誤提示(要透過{{ obj.errors.user.0 }}調用)
    widget：訂製html插件(重要)
    label：訂製標籤名(要透過{{ obj.user.label }}調用)
    initial：默認值
    validators：自訂製驗證規則
    disabled：是否禁止編輯
    """
    user = fields.CharField(
        required=True,
        max_length=12,  # 最大長度
        min_length=3,  # 最小長度
        error_messages={},
        widget=widgets.TextInput(attrs={'n': 123}),  # 參數為自定義屬性
        label="用戶名",
        initial='請輸入用戶名',
        disabled=True,
    )
    age = fields.IntegerField(
        label="年齡",
        max_value=1000,  # 最大值
        min_value=0,  # 最小值
        error_messages={
            'max_value': '太大了',
        }
    )
    email = fields.EmailField(
        label="信箱",
    )
    smath = fields.DecimalField()  # 小數
    file = fields.FileField()
    city = fields.ChoiceField(
        choices=[(1, "上海"), (2, "北京"), (3, "南京")],  # (value, 顯示文字)
        initial=3,  # 默認value=3
    )
    hobby = fields.MultipleChoiceField(
        choices=[(1, "籃球"), (2, "電動"), (3, "小說")],  # (value, 顯示文字)
        initial=[1, 2],
    )
    # date = fields.DateField()  # 格式：2015-09-01
    # datetime = fields.DateTimeField()  # 格式：2015-09-01 11:12
    radio = fields.ChoiceField(
        choices=[(1, 'man'), (2, 'woman')],
        widget=widgets.RadioSelect(),
    )
    check = fields.MultipleChoiceField(
        choices=[(1, 'man'), (2, 'woman')],
        widget=widgets.CheckboxSelectMultiple(),
    )
    from django.core.validators import RegexValidator
    my = fields.CharField(
        # 自定義正則一
        # validators可設置多個RegexValidator
        # RegexValidator(正則, 錯誤信息)
        validators=[RegexValidator(r"^[0-9]+$", "請輸入數字"), RegexValidator(r"^87[0-9]+$", "請以87開頭")],
    )
    # 自定義正則二
    # fields.RegexField(正則)，只可設置單個正則
    my2 = fields.RegexField(
        r"^[0-9]+$",
        error_messages={
            "invalid": "請輸入數字",
        }
    )


def detailed_form(request):
    if request.method == "GET":
        obj = DetailedForm()
        return render(request, 'detailed_form.html', locals())
    else:
        # 文件存在request.FILES
        obj = DetailedForm(request.POST, request.FILES)
        obj.is_valid()
        print(obj.cleaned_data)
        return render(request, 'detailed_form.html', locals())


class DynamicForm(forms.Form):
    price = fields.IntegerField()
    # 因為是靜態字段，所以在程序啟動時就會給一塊內存去加載，除非重啟，否則不會動態更改
    user_id = fields.IntegerField(
        # widget=widgets.Select(choices=[(0, 'jamie'), (1, 'joker'), (2, 'jj'), ])
        # widget=widgets.Select(choices=models.UserInfo.objects.values_list('id', 'username'))
        widget=widgets.Select()  # 因為init會加載，所以不用再這邊查models
    )

    def __init__(self, *args, **kwargs):
        # super一定要寫在上面，用來拷貝所有的靜態字段複製給self.fields
        super(DynamicForm, self).__init__(*args, **kwargs)
        # 每次調用obj時就會執行一次init，所以在此更新choices，實現動態更新
        self.fields['user_id'].widget.choices = models.UserInfo.objects.values_list('id', 'username')


def dynamic_form(request):
    obj = DynamicForm()
    return render(request, 'dynamic_form.html', locals())
