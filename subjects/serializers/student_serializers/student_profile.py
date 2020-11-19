from rest_framework import serializers

from subjects.models import Student, CourseScore


class StudentProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    # scores = serializers.SerializerMethodField()

    # @staticmethod
    # def get_scores(student: Student):
    #     # TODO send more data in this field
    #     course_scores = CourseScore.objects.filter(
    #         student=student
    #     ).select_related('course__subject').values('score', 'course__subject__name')
    #
    #     return {
    #         course_score['course__subject__name']: course_score['score'] for course_score in course_scores
    #     }

    class Meta:
        model = Student

        fields = (
            'id',
            'first_name',
            'last_name',
            'username',  # TODO do we need this?
            'email',
            'phone_number',
            'resume',
            'university',
            'student_id',
            'scores',
            'roles',
        )

        read_only_fields = (
            'id',
            'university',
            'student_id',
            'scores',
            'roles',
        )
