from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from _helpers.permissions import IsStudent
from ta_procedures.filters import RoleFilter
from ta_procedures.models import Role
from ta_procedures.serializers.student_serializers import RoleRetrieveSerializer, RoleListSerializer


class RoleReadOnlyViewSet(ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsStudent,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoleFilter
    queryset = Role.objects.all()

    def get_serializer_class(self):
        if self.kwargs:
            return RoleRetrieveSerializer
        return RoleListSerializer
