from django import forms
from django.forms import fields
from django.forms import widgets
from repository import models


class ArticleForm(forms.Form):
    title = fields.CharField(
        widget=widgets.TextInput(attrs={"class": 'form-control', "placeholder": "文章標題"})
    )
    summary = fields.CharField(
        widget=widgets.Textarea(attrs={"class": 'form-control', "placeholder": "文章簡介", "row": "3"})
    )
    content = fields.CharField(
        widget=widgets.Textarea(attrs={"class": 'kind-content', "placeholder": "文章內容"})
    )

    article_type_id = fields.IntegerField(
        widget=widgets.RadioSelect(choices=models.Article.type_choices)
    )

    category_id = fields.ChoiceField(
        choices=[],
        widget=widgets.RadioSelect
    )

    tags = fields.MultipleChoiceField(
        choices=[],
        widget=widgets.CheckboxSelectMultiple
    )

    def __init__(self, request, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        blog_id = request.session['user_info']['blog__nid']
        self.fields['category_id'].choices = models.Category.objects.filter(blog_id=blog_id).values_list('nid',
                                                                                                         'title')
        self.fields['tags'].choices = models.Tag.objects.filter(blog_id=blog_id).values_list('nid', 'title')



