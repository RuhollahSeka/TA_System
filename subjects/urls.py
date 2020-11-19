from django.urls import path

from subjects.views import student_views, lecturer_views

urlpatterns = [
    path('student-profile/', student_views.StudentProfileAPIView.as_view()),
    path('lecturer-profile/', lecturer_views.LecturerProfileAPIView.as_view()),
]
