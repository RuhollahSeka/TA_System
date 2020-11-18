from django.db import models

from subjects.models import Lecturer


class Course(models.Model):
    FALL_SEMESTER = 'fall'
    SPRING_SEMESTER = 'spring'
    SUMMER_SEMESTER = 'summer'

    SEMESTER_CHOICES = (
        (FALL_SEMESTER, 'ترم پاییز'),
        (SPRING_SEMESTER, 'ترم بهار'),
        (SUMMER_SEMESTER, 'ترم تابستان'),
    )

    name = models.CharField(
        max_length=128,
        verbose_name='نام درس',
    )

    course_id = models.CharField(
        max_length=16,
        verbose_name='شناسه درس',
    )

    year = models.PositiveSmallIntegerField(
        verbose_name='سال ارائه‌شدن درس',
    )

    semester = models.CharField(
        max_length=8,
        choices=SEMESTER_CHOICES,
        verbose_name='ترم ارائه‌شدن درس',
    )

    teacher = models.ForeignKey(
        to=Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='استاد درس',
    )
