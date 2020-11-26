import django_filters

from ta_procedures.models import Recommendation


class RecommendationFilter(django_filters.FilterSet):
    lecturer = django_filters.NumberFilter(field_name='course__lecturer_id')

    class Meta:
        model = Recommendation
        fields = {
            'id': ['exact', 'in'],
            'student': ['exact', 'in'],
            'course': ['exact', 'in'],
        }
