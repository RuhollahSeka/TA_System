from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from _helpers.models import TimeModel
from subjects.models import University


class Student(TimeModel):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
    )

    university = models.ForeignKey(
        to=University,
        on_delete=models.CASCADE,
        verbose_name='دانشگاه'
    )

    student_id = models.CharField(
        max_length=16,
        verbose_name='شناسه دانشجویی',
    )

    phone_number = models.CharField(
        max_length=16,
        verbose_name='شماره تلفن',
    )

    resume = models.FileField(
        upload_to='resume/students/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
        verbose_name='فایل رزومه استاد',
    )
