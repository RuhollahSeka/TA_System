from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from _helpers.models import TimeModel
from subjects.models import University


class Student(TimeModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
    )

    university = models.ForeignKey(
        to=University,
        on_delete=models.CASCADE,
        verbose_name='دانشگاه'
    )

    student_id = models.CharField(
        max_length=16,
        verbose_name='شناسه دانشجویی',
    )

    phone_number = models.CharField(
        max_length=16,
        verbose_name='شماره تلفن',
    )

    resume = models.FileField(
        upload_to='resume/students/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name='فایل رزومه استاد',
    )

    average_score = models.FloatField(
        null=True,
        blank=True,
        verbose_name='معدل',
    )

    @property
    def scores(self):
        from subjects.models import CourseScore
        course_scores = CourseScore.objects.filter(
            student=self,
        ).extra(
            select={
                'course__subject__name': 'name',
            }
        ).select_related('course__subject').values('score', 'course__subject__name', 'course_id')

        return course_scores

    @property
    def roles(self):
        from ta_procedures.models import Role
        roles = Role.objects.filter(
            student=self
        ).extra(
            select={
                'name': 'role_name',
                'course__subject__name': 'course_name',
                'id': 'role_id',
            }
        ).select_related('course__subject').values('name', 'course__subject__name', 'course_id', 'id')

        return roles

    class Meta:
        verbose_name = 'داتشجو'
        verbose_name_plural = 'دانشجویان'
