"""MyCRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from kingadmin import views

urlpatterns = [
    url(r"^$", views.app_index, name="app_index"),
    url(r'^(?P<app_name>\w+)/$', views.model_list, name="model_list"),
    url(r'^(?P<app_name>\w+)/(?P<model_name>\w+)/$', views.model_obj_list, name="model_obj_list"),
    url(r'^(?P<app_name>\w+)/(?P<model_name>\w+)/(?P<obj_id>\d+)/change/$', views.model_obj_change,
        name="model_obj_change"),
    # delete網址分為兩種/app_name/model_name/obj_id/和/app_name/model_name/objs_id/
    url(r'^(?P<app_name>\w+)/(?P<model_name>\w+)/((?P<obj_id>\d+)|(?P<objs_id>(\d+,)+))/delete/$',
        views.model_obj_delete, name="model_obj_delete"),
    url(r'^(?P<app_name>\w+)/(?P<model_name>\w+)/add/$', views.model_obj_add, name="model_obj_add"),
    url(r"^login/", views.acc_login),
]
