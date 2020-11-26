import django_filters

from ta_procedures.models import CoursePermission


class CoursePermissionFilter(django_filters.FilterSet):
    lecturer = django_filters.NumberFilter(field_name='course__lecturer_id')

    class Meta:
        model = CoursePermission
        fields = {
            'id': ['exact', 'in'],
            'student': ['exact', 'in'],
            'course': ['exact', 'in'],
        }
