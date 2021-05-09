from django.contrib import admin

from ta_procedures.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass
