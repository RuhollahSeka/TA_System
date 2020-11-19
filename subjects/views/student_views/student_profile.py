from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView

from _helpers.permissions import IsStudent
from subjects.models import Student
from subjects.serializers.student_serializers import StudentProfileSerializer


class StudentProfileAPIView(RetrieveUpdateAPIView):
    authentication_classes = (TokenAuthentication,)  # TODO change this
    permission_classes = (IsStudent,)
    serializer_class = StudentProfileSerializer

    def get_object(self):
        user = self.request.user
        return Student.objects.get(user=user)
