from rest_framework import serializers

from subjects.models import Lecturer


class LecturerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', read_only=True, label='نام استاد')
    last_name = serializers.CharField(source='user.last_name', read_only=True)

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
