import django_filters

from subjects.models import Lecturer


class LecturerFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(field_name='user__first_name')
    last_name = django_filters.CharFilter(field_name='user__last_name')

    class Meta:
        model = Lecturer
        fields = {
            'id': ['exact', 'in'],
            'first_name': ['exact', 'contains', 'startswith'],
            'last_name': ['exact', 'contains', 'startswith'],
        }
