from django.db import models

from _helpers.models import TimeModel
from subjects.models import Student
from ta_procedures.models import Course


class Recommendation(TimeModel):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        related_name='recommendations',
        verbose_name='دانشجو',
    )

    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='درس',
    )

    text = models.TextField(
        verbose_name='متن',
    )

    class Meta:
        verbose_name = 'توصیه'
        verbose_name_plural = 'توصیه‌ها'
