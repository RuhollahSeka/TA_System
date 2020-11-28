from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

from _helpers.permissions import IsStudent
from subjects.filters import UniversityFilter
from subjects.models import University
from subjects.serializers.student_serializers import UniversitySerializer


class UniversityAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsStudent,)
    serializer_class = UniversitySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UniversityFilter
    queryset = University.objects.all()
