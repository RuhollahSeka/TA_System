from django.contrib import admin

from subjects.models import Lecturer


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    pass