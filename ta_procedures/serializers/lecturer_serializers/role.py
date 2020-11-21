from django.db import transaction
from rest_framework import serializers

from ta_procedures.models import Role, RoleAttachment


class RoleAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleAttachment
        fields = (
            'id',
            'attachment',
        )


class RoleSerializer(serializers.ModelSerializer):
    attachments = RoleAttachmentSerializer(many=True)

    class Meta:
        model = Role
        fields = (
            'id',
            'name',
            'description',
            'course',
            'student',
            'attachments',
        )
        read_only_fields = (
            'id',
            'attachments',
        )

    def create(self, validated_data):
        with transaction.atomic():
            role = super().create(validated_data)
            files = self.context['files']
            for file in files.values:
                RoleAttachment.objects.create(
                    role=role,
                    attachment=file,
                )
        return role


class RoleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = (
            'id',
            'name',
            'course',
            'student',
        )
        read_only_fields = (
            'id',
            'name',
            'course',
            'student',
        )
