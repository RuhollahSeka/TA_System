import django_filters

from subjects.models import University


class UniversityFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields = {
            'name': ['exact', 'contains', 'startswith'],
        }
