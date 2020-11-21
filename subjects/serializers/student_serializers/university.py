from rest_framework import serializers

from subjects.models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
            'name',
        )
