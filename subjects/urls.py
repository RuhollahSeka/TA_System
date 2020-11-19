from django.urls import path

from subjects import views

urlpatterns = [
    path('student-profile/', views.StudentProfileAPIView.as_view()),
]
