from django.contrib import admin
from app01 import models


admin.site.register(models.Classes)
admin.site.register(models.Students)
admin.site.register(models.Teachers)
