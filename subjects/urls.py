from django.urls import path

from subjects.views import user_views

urlpatterns = [
    path('student-profile/', user_views.StudentProfileAPIView.as_view()),
    path('lecturer-profile/', user_views.LecturerProfileAPIView.as_view()),
]
