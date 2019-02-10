"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from app01.views import classes, teachers, students, test, ajax

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test', test.practice),

    url(r'^classes.html', classes.get_classes),
    url(r'^add_classes.html', classes.add_classes),
    url(r'^del_classes.html', classes.del_classes),
    url(r'^update_classes.html', classes.update_classes),
    url(r'^set_teachers.html', classes.set_teachers),

    url(r'^students.html', students.get_students),
    url(r'^add_students.html', students.add_students),
    url(r'^ajax_add_students.html', students.ajax_add_students),
    url(r'^del_students.html', students.del_students),
    url(r'^ajax_del_students.html', students.ajax_del_students),
    url(r'^update_students.html', students.update_students),
    url(r'^ajax_update_students.html', students.ajax_update_students),

    url(r'^ajax_start.html', ajax.ajax_start),
    url(r'^ajax_submit.html', ajax.ajax_submit),
    url(r'^ajax_add.html', ajax.ajax_add),
]
