from rest_framework import serializers

from subjects.models import Student


class StudentProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

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
        )

        read_only_fields = (
            'id',
            'university',
            'student_id',
        )
