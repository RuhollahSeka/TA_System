from django.urls import path
from rest_framework.routers import SimpleRouter

from ta_procedures.views import lecturer_views, student_views

lecturer_router = SimpleRouter()
lecturer_router.register(
    prefix='lecturers/courses',
    viewset=lecturer_views.CourseViewSet,
    basename='lecturer-course-v1',
)
lecturer_router.register(
    prefix='lecturers/roles',
    viewset=lecturer_views.RoleViewSet,
    basename='lecturer-role-v1',
)
lecturer_router.register(
    prefix='lecturers/role-requests',
    viewset=lecturer_views.RoleRequestViewSet,
    basename='lecturer-role-request-v1',
)
lecturer_router.register(
    prefix='lecturer/recommendations',
    viewset=lecturer_views.RecommendationViewSet,
    basename='lecturer-recommendation-v1',
)

student_router = SimpleRouter()
student_router.register(
    prefix='students/courses',
    viewset=student_views.CourseReadOnlyViewSet,
    basename='student-course-v1',
)
student_router.register(
    prefix='students/roles',
    viewset=student_views.RoleReadOnlyViewSet,
    basename='student-role-v1',
)
student_router.register(
    prefix='students/role-requests',
    viewset=student_views.RoleRequestViewSet,
    basename='student-role-request-v1',
)
student_router.register(
    prefix='students/recommendations',
    viewset=student_views.RecommendationReadOnlyViewSet,
    basename='student-recommendation-v1',
)

urlpatterns = [

]

urlpatterns = urlpatterns + lecturer_router.urls + student_router.urls
