from django.conf.urls import url, include
from django.contrib import admin
from .views import user, trouble

urlpatterns = [
    url(r'^base-info.html$', user.base_info),
    url(r'^edit-tag-(?P<nid>\d+).html$', user.edit_tag),
    url(r'^remove-tag.html$', user.remove_tag),
    url(r'^add-tag.html$', user.add_tag),
    url(r'^tag.html$', user.tag),
    url(r'^edit-category-(?P<nid>\d+).html$', user.edit_category),
    url(r'^remove-category.html$', user.remove_category),
    url(r'^add-category.html$', user.add_category),
    url(r'^category.html$', user.category),
    url(r'^remove-article.html$', user.remove_article),
    url(r'^edit-article-(?P<nid>\d+).html$', user.edit_article),
    url(r'^add-article.html$', user.add_article),
    url(r"^article-(?P<article_type_id>\d+)-(?P<category_id>\d+).html$", user.article, name='article'),
    url(r'^index.html$', user.index),

    # 一般用戶: 提交報帳單, 查看, 修改(未處理時), 評分(已處理時)
    url(r'^trouble-list.html$', trouble.trouble_list),
    url(r'^add-trouble.html$', trouble.add_trouble),
    url(r'^edit-trouble-(?P<nid>\d+).html$', trouble.edit_trouble),
    url(r'^remove-trouble-(?P<nid>\d+).html$', trouble.remove_trouble),
    url(r'^trouble-detail-(?P<nid>\d+).html$', trouble.trouble_detail),
    url(r'^trouble-solution-(?P<nid>\d+).html$', trouble.trouble_solution),
    # 處理者:
    url(r'^trouble-kill-list.html$', trouble.trouble_kill_list),
    url(r'^kill-trouble-(?P<nid>\d+).html$', trouble.kill_trouble),
    # root:
    url(r'^trouble-report.html$', trouble.trouble_report),
    url(r'^trouble-json-report.html$', trouble.trouble_json_report),
]
