from django.db import models

from _helpers.models import TimeModel
from ta_procedures.models import Role


class RoleAttachment(TimeModel):
    role = models.ForeignKey(
        to=Role,
        on_delete=models.CASCADE,
        related_name='attachments',
        verbose_name='وظیقه',
    )

    attachment = models.FileField(
        upload_to='roles/',
        verbose_name='فایل ضمیمه وظیفه',
    )

    class Meta:
        verbose_name = 'ضمیمه وظیفه'
        verbose_name_plural = 'ضمایم وظایف'
