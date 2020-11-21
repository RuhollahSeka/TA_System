from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from _helpers.permissions import IsLecturer
from subjects.serializers.lecturer_serializers import StudentRetrieveSerializer, StudentListSerializer


class StudentViewSet(ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsLecturer,)
    filter_backends = (DjangoFilterBackend,)

    def get_serializer_class(self):
        if self.kwargs:
            return StudentRetrieveSerializer
        return StudentListSerializer
