from kingadmin.sites import site
from crm import models
from kingadmin.admin_base import BaseKingAdmin
from django.shortcuts import redirect
print("kingadmin in crm......")


class UserProfileAdmin:
    readonly_fields = ["password"]


class CustomerAdmin(BaseKingAdmin):
    list_display = ["id", "name", "source", "contact_type", "contact", "consultant", "consult_content", "status", "date"]
    list_filter = ["source", "consultant", "status", "date"]
    search_fields = ["contact", "consultant__name"]
    readonly_fields = ["contact"]
    filter_horizontal = ["consult_courses"]
    list_per_page = 4

    actions = ["change_status"]

    def change_status(self, request, querysets):
        querysets.update(status=1)


site.register(models.CustomerInfo, CustomerAdmin)
site.register(models.Role)
site.register(models.Menus)
site.register(models.UserProfile, UserProfileAdmin)
site.register(models.Course)
site.register(models.CourseRecord)
site.register(models.Student)
