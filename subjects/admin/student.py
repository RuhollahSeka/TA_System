from django.contrib import admin

from subjects.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
