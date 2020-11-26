from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        )

    def validate(self, attrs):
        attrs = super().validate(attrs)
        lecturer = self.context['lecturer']

        if self.instance:
            return attrs

        course = attrs['course']
        if course.lecturer_id != lecturer.id:
            raise ValidationError('درس انتخاب شده در لیست دروس شما نمی‌باشد.')
        return attrs

    def update(self, instance, validated_data):
        validated_data.pop('student', None)
        validated_data.pop('course', None)
        return super().update(instance, validated_data)
