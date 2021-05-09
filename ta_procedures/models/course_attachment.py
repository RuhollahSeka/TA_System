from django.db import models

from _helpers.models import TimeModel
from ta_procedures.models import Course


class CourseAttachment(TimeModel):
    course = models.ForeignKey(
        to=Course,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='درس',
    )

    attachment = models.FileField(
        upload_to='courses/',
        verbose_name='فایل ضمیمه درس',
    )

    class Meta:
        verbose_name = 'ضمیمه درس'
        verbose_name_plural = 'ضمیمه‌های دروس'
