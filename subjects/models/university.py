from django.db import models

from _helpers.models import TimeModel


class University(TimeModel):
    name = models.CharField(
        max_length=128,
        verbose_name='نام دانشگاه',
    )

    class Meta:
        verbose_name = 'دانشگاه'
        verbose_name = 'دانشگاه‌ها'
