from django import forms
from django.forms import fields
from django.core.exceptions import ValidationError
from django.forms import widgets


class LoginForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    username = fields.CharField(
        widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "用戶名"}),
        min_length=3,
    )
    password = fields.CharField(
        widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密碼"}),
    )
    check_code = fields.CharField(
        widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "驗證碼"}),
    )

    def clean_check_code(self):
        v1 = self.request.session["check_code"]
        v2 = self.cleaned_data["check_code"]
        if v1.upper() != v2.upper():
            raise ValidationError(message="驗證碼錯誤")
        return v2


class RegisterForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(RegisterForm, self).__init__(*args, **kwargs)
        
    username = fields.CharField(
        widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "用戶名"}),
        min_length=3,
    )
    nickname = fields.CharField(
        widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "暱稱"}),
    )
    email = fields.EmailField(
        widget=widgets.EmailInput(attrs={"class": "form-control", "placeholder": "信箱"}),
    )
    password = fields.CharField(
        widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密碼"}),
    )
    password_ck = fields.CharField(
        widget=widgets.PasswordInput(attrs={"class": "form-control", "placeholder": "密碼確認"}),
    )
    check_code = fields.CharField(
        widget=widgets.TextInput(attrs={"class": "form-control", "placeholder": "驗證碼"}),
    )

    def clean_check_code(self):
        v1 = self.request.session["check_code"]
        v2 = self.cleaned_data["check_code"]
        if v1.upper() != v2.upper():
            raise ValidationError(message="驗證碼錯誤")
        return v2

    def clean(self):
        value_dict = self.cleaned_data
        v1 = value_dict.get("password")
        v2 = value_dict.get("password_ck")
        if v1 != v2:
            raise ValidationError(message="密碼輸入不一致")
        return self.cleaned_data
