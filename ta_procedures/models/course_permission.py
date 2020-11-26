from django.db import models

from _helpers.models import TimeModel
from subjects.models import Student
from ta_procedures.models import Course


class CoursePermission(TimeModel):
    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        related_name='permissions',
        verbose_name='دانش‌جو',
    )

    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='permissions',
        verbose_name='درس',
    )

    add_ta = models.BooleanField(
        default=False,
        verbose_name='دسترسی انتخاب دستیار',
    )

    remove_ta = models.BooleanField(
        default=False,
        verbose_name='دسترسی حذف دستیار',
    )
