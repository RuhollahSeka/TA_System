from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ta_procedures.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    lecturer_name = serializers.CharField(source='course.lecturer.name', read_only=True, label='نام ارائه دهنده')

    class Meta:
        model = Recommendation
        fields = (
            'id',
            'student',
            'course',
            'text',
            'lecturer_name',
        )
        read_only_fields = (
            'id',
            'lecturer_name',
        )
        ref_name = 'LecturerRecommendationSerializer'

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
