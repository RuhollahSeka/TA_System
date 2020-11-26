from rest_framework import serializers

from ta_procedures.models import CoursePermission


class CoursePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePermission
        fields = (
            'id',
            'student',
            'course',
            'add_ta',
            'remove_ta',
        )
        read_only_fields = (
            'id',
            'student',
            'course',
            'add_ta',
            'remove_ta',
        )
