from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet

from _helpers.permissions import IsLecturer
from ta_procedures.filters import RecommendationFilter
from ta_procedures.serializers.lecturer_serializers import RecommendationSerializer


class RecommendationViewSet(ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsLecturer,)
    serializer_class = RecommendationSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RecommendationFilter

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._lecturer = None

    def initial(self, request, *args, **kwargs):
        self._lecturer = request.user.lecturer
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(course__lecturer=self._lecturer)
        return queryset

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['lecturer'] = self._lecturer
        return context
