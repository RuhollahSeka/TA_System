from rest_framework import serializers

from ta_procedures.models import Recommendation


class RecommendationSerializer(serializers.ModelSerializer):
    lecturer_name = serializers.CharField(source='course.lecturer.user.first_name', read_only=True, label='نام استاد')

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
            'student',
            'course',
            'text',
            'lecturer_name',
        )
        ref_name = 'StudentRecommendationSerializer'
