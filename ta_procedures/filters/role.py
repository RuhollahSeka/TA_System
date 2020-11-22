import django_filters

from ta_procedures.models import Role


class RoleFilter(django_filters.FilterSet):
    class Meta:
        model = Role
        fields = {
            'id': ['exact', 'in'],
            'course': ['exact', 'in'],
            'course_id': ['exact', 'in', 'contains', 'startswish'],
            'lecturer': ['exact', 'in'],
            'lecturer_name': ['exact', 'contains', 'in', 'startswish'],
            'student': ['isnull'],
        }
