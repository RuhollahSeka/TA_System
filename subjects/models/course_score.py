from django.db import models

from subjects.models import Student, Course


class CourseScore(models.Model):
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
