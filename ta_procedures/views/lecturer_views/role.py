from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from _helpers.permissions import IsLecturer
from ta_procedures.filters import RoleFilter
from ta_procedures.models import Role
from ta_procedures.serializers.lecturer_serializers import RoleListSerializer, RoleSerializer


class RoleViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsLecturer,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RoleFilter
    queryset = Role.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET' and not self.kwargs:
            return RoleListSerializer
        return RoleSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        files = self.request.FILES
        context['files'] = files
        return context
