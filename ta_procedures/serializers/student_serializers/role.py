from rest_framework import serializers

from ta_procedures.models import Role, RoleAttachment


class RoleAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAttachment
        fields = (
            'id',
            'attachment',
        )
        read_only_fields = (
            'id',
            'attachment',
        )


class BaseRoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'course',
            'student',
        )


class RoleListSerializer(BaseRoleSerializer):
    class Meta:
        model = Role
        fields = BaseRoleSerializer.Meta.fields
        read_only_fields = BaseRoleSerializer.Meta.fields
        ref_name = 'StudentRoleListSerializer'


class RoleRetrieveSerializer(BaseRoleSerializer):
    attachments = RoleAttachmentSerializer(many=True)

    class Meta:
        model = Role
        fields = BaseRoleSerializer.Meta.fields + ('description', 'attachments',)
        read_only_fields = BaseRoleSerializer.Meta.fields + ('description', 'attachments',)
