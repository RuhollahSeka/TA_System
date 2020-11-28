from django.db import transaction
from rest_framework import serializers

from ta_procedures.models import CourseAttachment, Course


class CourseAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAttachment
        fields = (
            'id',
            'attachment',
        )


class BaseCourseSerializer(serializers.ModelSerializer):
    university_name = serializers.CharField(source='university.name', read_only=True, label='نام دانشگاه')
    subject_name = serializers.CharField(source='subject.name', read_only=True, label='نام درس')

    class Meta:
        fields = (
            'id',
            'university_name',
            'subject_name',
            'course_id',
            'year',
            'semester',
        )


class CourseSerializer(BaseCourseSerializer):
    attachments = CourseAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = BaseCourseSerializer.Meta.fields + ('description', 'attachments',)
        read_only_fields = BaseCourseSerializer.Meta.fields + ('attachments',)

    def save(self, **kwargs):
        with transaction.atomic():
            course = super().save(**kwargs)
            files = self.context['files']
            for file in files.values:
                CourseAttachment.objects.create(
                    course=course,
                    attachment=file,
                )
        return course


class CourseListSerializer(BaseCourseSerializer):
    class Meta:
        model = Course
        fields = BaseCourseSerializer.Meta.fields
        read_only_fields = BaseCourseSerializer.Meta.fields
        ref_name = 'LecturerCourseListSerializer'
