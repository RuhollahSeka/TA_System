import django_filters

from subjects.models import Subject


class SubjectFilter(django_filters.FilterSet):
    class Meta:
        model = Subject
        fields = {
            'name': ['exact', 'contains', 'startswith'],
        }
