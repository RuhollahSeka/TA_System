from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView

from _helpers.permissions import IsLecturer
from subjects.models import Lecturer
from subjects.serializers import LecturerProfileSerializer


class LecturerProfileAPIView(RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsLecturer,)
    serializer_class = LecturerProfileSerializer

    def get_object(self):
        user = self.request.user
        return Lecturer.objects.get(user=user)
