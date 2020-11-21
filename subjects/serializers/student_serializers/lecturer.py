from rest_framework import serializers

from subjects.models import Lecturer


class LecturerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Lecturer
        fields = (
            'id',
            'first_name',
            'last_name',
        )
        read_only_fields = (
            'id',
            'first_name',
            'last_name',
        )
