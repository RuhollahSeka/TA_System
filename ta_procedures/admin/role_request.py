from django.contrib import admin

from ta_procedures.models import RoleRequest


@admin.register(RoleRequest)
class RoleRequestAdmin(admin.ModelAdmin):
    pass
