from django.db import models

from _helpers.models import TimeModel
from subjects.models import Student
from ta_procedures.models import Course


class Role(TimeModel):
    name = models.CharField(
        max_length=64,
        verbose_name='نام وظیفه',
    )

    description = models.TextField(
        verbose_name='توضیحات',
    )

    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        verbose_name='درس ارائه شده',
    )

    student = models.ForeignKey(
        to=Student,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='دستیار آموزشی',
    )

    class Meta:
        verbose_name = 'وظیفه'
        verbose_name_plural = 'وظایف'
