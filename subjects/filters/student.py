import django_filters

from subjects.models import Student


class StudentFilter(django_filters.FilterSet):

    class Meta:
        model = Student
        fields = {
            'role': ['exact', 'in'],
        }
