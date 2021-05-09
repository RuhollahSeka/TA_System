from django.contrib import admin

from subjects.models import University


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    pass
