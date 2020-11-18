from django.db import models


class TimeModel(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='تاریخ ساخت',
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='تاریخ به‌روزرسانی',
    )

    class Meta:
        abstract = True
