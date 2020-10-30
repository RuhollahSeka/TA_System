from django.contrib.auth.models import User
from django.db import models


class TimeConfig(models.Model):

    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
    )

    weekday = models.CharField(
        max_length=4,
    )

    start_time = models.TimeField(
        verbose_name='ساعت شروع',
    )

    end_time = models.TimeField(
        verbose_name='ساعت پایان',
    )
