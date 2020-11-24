from django.urls import path

from subjects.views import student_views, lecturer_views

urlpatterns = [
    # Student urls
    path('student-profile/', student_views.StudentProfileAPIView.as_view()),
    path('lecturers/', student_views.LecturerAPIView.as_view()),
    path('universities/', student_views.UniversityAPIView.as_view()),
    path('subjects/', student_views.SubjectAPIView.as_view()),

    path('lecturer-profile/', lecturer_views.LecturerProfileAPIView.as_view()),
    path('students/', lecturer_views.StudentViewSet, name='students')
]
