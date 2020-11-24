from rest_framework import serializers

from ta_procedures.models import RoleRequest


class RoleRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleRequest
        fields = (
            'id',
            'student',
            'role',
            'state',
        )
        read_only_fields = (
            'id',
            'student',
            'role',
        )
