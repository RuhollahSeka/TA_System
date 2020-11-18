from django.db import models

from _helpers.models import TimeModel
from ta_procedures.models import Role


class RoleAttachment(TimeModel):
    role = models.ForeignKey(
        to=Role,
        on_delete=models.CASCADE,
        verbose_name='وظیقه',
    )

    attachment = models.FileField(
        upload_to='files/roles/',
        verbose_name='فایل ضمیمه وظیفه',
    )
