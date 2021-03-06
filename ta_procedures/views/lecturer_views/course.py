from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import GenericViewSet

from _helpers.permissions import IsLecturer
from ta_procedures.filters import CourseFilter
from ta_procedures.models import Course
from ta_procedures.serializers.lecturer_serializers import CourseListSerializer, CourseSerializer


class CourseViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsLecturer,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CourseFilter
    queryset = Course.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseSerializer
