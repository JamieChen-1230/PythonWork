from django import forms
from django.forms import fields
from django.forms import widgets
from repository import models


class TroubleMaker(forms.Form):
    title = fields.CharField(
        max_length=32,
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    detail = fields.CharField(
        widget=widgets.Textarea(attrs={"id": "detail", "class": "kind-content"})
    )


class TroubleKiller(forms.Form):
    title = fields.CharField(
        max_length=32,
        required=False,
        widget=widgets.TextInput(attrs={"class": "form-control", "disabled": "disabled"})
    )

    detail = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={"id": "detail", "class": "kind-content"})
    )

    solution = fields.CharField(
        widget=widgets.Textarea(attrs={"id": "solution", "class": "kind-content"})
    )


class TroubleDetail(forms.Form):
    title = fields.CharField(
        max_length=32,
        required=False,
        widget=widgets.TextInput(attrs={"class": "form-control", "disabled": "disabled"})
    )

    user = fields.CharField(
        required=False,
        widget=widgets.TextInput(attrs={"class": "form-control", "disabled": "disabled"})
    )

    detail = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={"id": "detail", "class": "kind-content"})
    )


class TroubleSolution(forms.Form):
    title = fields.CharField(
        max_length=32,
        required=False,
        widget=widgets.TextInput(attrs={"class": "form-control", "disabled": "disabled"})
    )

    detail = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={"id": "detail", "class": "kind-content"})
    )

    solution = fields.CharField(
        required=False,
        widget=widgets.Textarea(attrs={"id": "solution", "class": "kind-content"})
    )

    pj = fields.IntegerField(
        widget=widgets.RadioSelect(choices=models.Trouble.pj_choices)
    )
