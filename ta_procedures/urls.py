from django.urls import path

from ta_procedures.views import lecturer_views, student_views

urlpatterns = [
    # Lecturer views
    path('lecturers/courses/', lecturer_views.CourseViewSet, name='lecturer-course-v1'),
    path('lecturers/roles/', lecturer_views.RoleViewSet, name='lecturer-role-v1'),
    path('lecturers/role-requests/', lecturer_views.RoleRequestViewSet, name='lecturer-role-request-v1'),
    path('lecturers/recommendations/', lecturer_views.RecommendationViewSet, name='lecturer-recommendation-v1'),

    # Student views
    path('students/courses/', student_views.CourseReadOnlyViewSet, name='student-course-v1'),
    path('students/roles/', student_views.RoleReadOnlyViewSet, name='student-role-v1'),
    path('students/role-requests/', student_views.RoleRequestViewSet, name='student-role-request-v1'),
    path('students/recommendations/', student_views.RecommendationReadOnlyViewSet, name='student-recommendation-v1'),
]
