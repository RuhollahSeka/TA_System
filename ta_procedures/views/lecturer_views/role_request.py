from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from _helpers.permissions import IsLecturer
from subjects.models import Lecturer
from ta_procedures.filters import RoleRequestFilter
from ta_procedures.models import RoleRequest
from ta_procedures.serializers.lecturer_serializers import RoleRequestSerializer


class RoleRequestViewSet(ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsLecturer,)
    serializer_class = RoleRequestSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoleRequestFilter

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return RoleRequest.objects.all()

        lecturer = Lecturer.objects.get(user=self.request.user)
        queryset = super().get_queryset()
        queryset = queryset.filter(role__course__lecturer=lecturer)
        return queryset
