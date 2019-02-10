from kingadmin.sites import site
from student import models
from kingadmin.admin_base import BaseKingAdmin
print("kingadm in student.....")


class TestAdmin(BaseKingAdmin):
    list_display = ["name"]


site.register(models.Test, TestAdmin)
