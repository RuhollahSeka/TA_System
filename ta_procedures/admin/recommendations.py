from django.contrib import admin

from ta_procedures.models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    pass
