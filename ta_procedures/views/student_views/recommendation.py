from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ReadOnlyModelViewSet

from _helpers.permissions import IsStudent
from ta_procedures.models import Recommendation
from ta_procedures.serializers.student_serializers import RecommendationSerializer


class RecommendationReadOnlyViewSet(ReadOnlyModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsStudent,)
    serializer_class = RecommendationSerializer
    queryset = Recommendation.objects.all()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._student = None

    def initial(self, request, *args, **kwargs):
        self._student = request.user.student
        super().initial(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(student=self._student)
        return queryset
