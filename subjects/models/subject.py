from django.db import models

from _helpers.models import TimeModel


class Subject(TimeModel):
    name = models.CharField(
        max_length=128,
        verbose_name='نام درس',
    )

    class Meta:
        verbose_name = 'عنوان درس'
        verbose_name_plural = 'عناوین دروس'
