import django_filters

from subjects.models import Lecturer


class LecturerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='user__first_name')
    first_name__contains = django_filters.CharFilter(field_name='user__first_name', lookup_expr='contains')
    first_name__startswith = django_filters.CharFilter(field_name='user__first_name', lookup_expr='startswith')

    last_name = django_filters.CharFilter(field_name='user__last_name')
    last_name__contains = django_filters.CharFilter(field_name='user__last_name', lookup_expr='contains')
    last_name__startswith = django_filters.CharFilter(field_name='user__last_name', lookup_expr='startswith')

    class Meta:
        model = Lecturer
        fields = {
            'id': ['exact', 'in'],
        }
