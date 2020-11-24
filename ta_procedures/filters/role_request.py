import django_filters

from ta_procedures.models import RoleRequest


class RoleRequestFilter(django_filters.FilterSet):
    class Meta:
        model = RoleRequest
        fields = {
            'id': ['exact', 'in'],
            'student': ['exact', 'in'],
            'role': ['exact', 'in'],
            'state': ['exact'],
        }
