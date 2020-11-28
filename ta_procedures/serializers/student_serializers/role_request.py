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
            'description',
        )
        read_only_fields = (
            'id',
            'student',
            'state',
        )
        ref_name = 'StudentRoleRequestSerializer'

    def create(self, validated_data):
        student = self.context['student']
        validated_data['student'] = student
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('role', None)
        return super().update(instance, validated_data)
