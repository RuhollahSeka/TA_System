from django.db import models

from _helpers.models import TimeModel
from subjects.models import Student
from ta_procedures.models import Course


class CourseScore(TimeModel):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='دانشجو',
    )

    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='درس پاس‌شده',
    )

    score = models.PositiveSmallIntegerField(
        verbose_name='نمره‌ی درس',
    )
