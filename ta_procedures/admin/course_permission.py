from django.contrib import admin

from ta_procedures.models import CoursePermission


@admin.register(CoursePermission)
class CoursePermissionAdmin(admin.ModelAdmin):
    pass
