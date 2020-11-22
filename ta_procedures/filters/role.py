import django_filters

from ta_procedures.models import Role


class RoleFilter(django_filters.FilterSet):
    course_id = django_filters.CharFilter(field_name='course__course_id')
    course_id__in = django_filters.BaseInFilter(field_name='course__course_id')
    course_id__contains = django_filters.CharFilter(field_name='course__course_id', lookup_expr='contains')
    course_id__startswith = django_filters.CharFilter(field_name='course__course_id', lookup_expr='startswith')

    lecturer_name = django_filters.CharFilter(field_name='lecturer__name')
    lecturer_name__contains = django_filters.CharFilter(field_name='lecturer__name', lookup_expr='contains')
    lecturer_name__startswith = django_filters.CharFilter(field_name='lecturer__name', lookup_expr='startswith')

    class Meta:
        model = Role
        fields = {
            'id': ['exact', 'in'],
            'course': ['exact', 'in'],
            'lecturer': ['exact', 'in'],
            'student': ['isnull'],
        }
