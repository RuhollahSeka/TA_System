from rest_framework import serializers

from ta_procedures.models import Course, CourseAttachment


class CourseAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAttachment
        fields = (
            'id',
            'attachment',
        )


class BaseCourseSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name')
    subject_name = serializers.CharField(source='subject.name')
    lecturer_first_name = serializers.CharField(source='lecturer.user.first_name')
    lecturer_last_name = serializers.CharField(source='lecturer.user.last_name')

    class Meta:
        fields = (
            'id',
            'university_name',
            'subject_name',
            'course_id',
            'year',
            'semester',
            'lecturer',
            'lecturer_first_name',
            'lecturer_last_name',
        )
        read_only_fields = (
            'id',
            'university_name',
            'subject_name',
            'course_id',
            'year',
            'semester',
            'lecturer',
            'lecturer_first_name',
            'lecturer_last_name',
        )


class CourseListSerializer(BaseCourseSerializer):
    class Meta:
        model = Course
        fields = BaseCourseSerializer.Meta.fields
        read_only_fields = BaseCourseSerializer.Meta.read_only_fields
        ref_name = 'StudentCourseListSerializer'


class CourseRetrieveSerializer(BaseCourseSerializer):
    attachments = CourseAttachmentSerializer(many=True)

    class Meta:
        model = Course
        fields = BaseCourseSerializer.Meta.fields + ('description', 'attachments',)
        read_only_fields = BaseCourseSerializer.Meta.read_only_fields + ('description', 'attachments',)
