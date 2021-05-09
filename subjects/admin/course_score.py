from django.contrib import admin

from subjects.models import CourseScore


@admin.register(CourseScore)
class CourseScoreAdmin(admin.ModelAdmin):
    pass
