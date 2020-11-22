from rest_framework import serializers

from subjects.models import Student


class StudentRetrieveSerializer(serializers.ModelSerializer):  # TODO start year
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'average_score',
            'email',
            'phone_number',
            'resume',
            'university',
            'scores',
            'roles',
        )
        read_only_fields = (
            'id',
            'first_name',
            'last_name',
            'average_score',
            'email',
            'phone_number',
            'resume',
            'university',
            'scores',
            'roles',
        )


class StudentListSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Student
        fields = (
            'id',
            'first_name',
            'last_name',
            'average_score',
        )
        read_only_fields = (
            'id',
            'first_name',
            'last_name',
            'average_score',
        )
