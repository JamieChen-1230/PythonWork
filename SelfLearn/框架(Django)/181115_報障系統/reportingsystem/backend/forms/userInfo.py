from django import forms
from django.forms import fields
from django.forms import widgets
from repository import models


class InfoForm(forms.Form):
    title = fields.CharField(
        widget=widgets.TextInput(attrs={"class": 'form-control', "placeholder": "博客標題"})
    )

    site = fields.CharField(
        max_length=32,
        min_length=3,
        widget=widgets.TextInput(attrs={"class": 'form-control', "placeholder": "博客地址，請輸入3-32的英文組合"})
    )

    theme = fields.ChoiceField(
        choices=[("0", "default"), ("1", "warm")],
        widget=widgets.RadioSelect(),
    )