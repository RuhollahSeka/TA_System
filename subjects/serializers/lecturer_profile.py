from rest_framework import serializers

from subjects.models import Lecturer


class LecturerProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')

    class Meta:
        model = Lecturer

        fields = (
            'id',
            'first_name',
            'last_name',
            'username',  # TODO do we need this?
            'email',
            'phone_number',
            'resume',
            'lecturer_id',
        )

        read_only_fields = (
            'id',
            'lecturer_id',
        )
