from django.conf.urls import url
from .views import home, account


urlpatterns = [
    url(r'^login.html', account.login),
    url(r'^logout.html', account.logout),
    url(r'^register.html', account.register),
    url(r'^updown.html', account.updown),
    url(r'^check_code.html$', account.check_code),
    url(r'^receive_content.html$', account.receive_content),
    url(r'^all/(?P<article_type_id>\d+).html$', home.index, name='index'),
    url(r'^(?P<site>\w+)/(?P<condition>((tag)|(category)|(date)))/(?P<val>\w+-?\w*).html$', home.allocation),   # filter
    url(r'^(?P<site>\w+)/(?P<nid>\d+).html$', home.detail),
    url(r'^(?P<site>\w+).html$', home.home),
    url(r'^', home.index),
]
