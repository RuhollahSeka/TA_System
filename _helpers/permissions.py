from rest_framework.permissions import BasePermission

from subjects.models import Student, Lecturer


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return super().has_permission(request, view) and user and user.is_superuser


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        student = Student.objects.filter(user=user).first()
        return super().has_permission(request, view) and student


class IsLecturer(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        lecturer = Lecturer.objects.filter(user=user).first()
        return super().has_permission(request, view) and lecturer
