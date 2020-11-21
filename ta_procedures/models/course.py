from django.db import models

from _helpers.models import TimeModel
from subjects.models import Lecturer, University, Subject


class Course(TimeModel):
    FALL_SEMESTER = 'fall'
    SPRING_SEMESTER = 'spring'
    SUMMER_SEMESTER = 'summer'

    SEMESTER_CHOICES = (
        (FALL_SEMESTER, 'ترم پاییز'),
        (SPRING_SEMESTER, 'ترم بهار'),
        (SUMMER_SEMESTER, 'ترم تابستان'),
    )

    university = models.ForeignKey(
        to=University,
        on_delete=models.CASCADE,
        verbose_name='دانشکاه',
    )

    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        verbose_name='درس',
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

    lecturer = models.ForeignKey(
        to=Lecturer,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='استاد درس',
    )

    description = models.TextField(
        verbose_name='توضیحات',
    )
