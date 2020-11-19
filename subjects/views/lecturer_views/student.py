from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from _helpers.permissions import IsLecturer
from subjects.serializers.lecturer_serializers import StudentRetrieveSerializer, StudentListSerializer


class StudentViewSet(ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsLecturer,)

    def get_serializer_class(self):
        if self.kwargs:
            return StudentRetrieveSerializer
        return StudentListSerializer
