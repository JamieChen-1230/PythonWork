from django.contrib import admin
from app01 import models


admin.site.register(models.UserInfo)

admin.site.register(models.Staff)
admin.site.register(models.Part)
admin.site.register(models.Tag)

admin.site.register(models.Staff2)
admin.site.register(models.Tag2)
admin.site.register(models.Staff2ToTag2)


