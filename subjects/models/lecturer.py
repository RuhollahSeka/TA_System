from django.contrib.auth.models import User
from django.db import models

from _helpers.models import TimeModel


class Lecturer(TimeModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
    )

    lecturer_id = models.CharField(
        max_length=16,
        verbose_name='شناسه استادی',
    )

    phone_number = models.CharField(
        max_length=16,
        verbose_name='شماره تلفن',
    )

    resume = models.FileField(
        upload_to='files/resume/lecturers/',
        verbose_name='فایل رزومه استاد',
    )
