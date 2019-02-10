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
from django.conf.urls import url
from crm import views

urlpatterns = [
    url(r'^$', views.dashboard, name="sales_dashboard"),
    url(r'^stu_enrollment/$', views.stu_enrollment, name="stu_enrollment"),
    url(r'^enrollment/(?P<enrollment_id>\d+)/$', views.enrollment, name="enrollment"),
    url(r'^enrollment/(?P<enrollment_id>\d+)/file_upload/$',
        views.enrollment_file_upload, name="enrollment_file_upload"),
    url(r'^stu_enrollment/(?P<enrollment_id>\d+)/contract_audit/$',
        views.enrollment_contract_audit, name="enrollment_contract_audit"),
]
