from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from _helpers.permissions import IsStudent
from subjects.models import Student
from ta_procedures.filters import RoleRequestFilter
from ta_procedures.models import RoleRequest
from ta_procedures.serializers.student_serializers import RoleRequestSerializer


class RoleRequestViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsStudent,)
    serializer_class = RoleRequestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoleRequestFilter

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._student = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)
        self._student = Student.objects.filter(user=request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(student=self._student)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['student'] = self._student
        return context

    def perform_destroy(self, role_request: RoleRequest):
        if role_request.state != RoleRequest.STATE_PENDING:
            return Response(
                data='فقط درخواست‌های در حال انتظار را می‌توان پاک کرد.',
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().perform_destroy(role_request)
