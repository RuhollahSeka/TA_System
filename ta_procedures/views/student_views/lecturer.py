from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView

from _helpers.permissions import IsStudent
from subjects.filters import LecturerFilter
from subjects.serializers.student_serializers import LecturerSerializer


class LecturerAPIView(ListAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsStudent,)
    serializer_class = LecturerSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LecturerFilter
