import django_filters

from ta_procedures.models import Course


class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields = {
            'id': ['exact', 'in'],
            'course_id': ['exact', 'in', 'contains'],
            'university': ['exact', 'in'],
            'subject': ['exact', 'in'],
            'lecturer': ['exact', 'in'],
        }
