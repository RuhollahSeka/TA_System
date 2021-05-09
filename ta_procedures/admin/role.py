from django.contrib import admin

from ta_procedures.models import Role


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    pass
