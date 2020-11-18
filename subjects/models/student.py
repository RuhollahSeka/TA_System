from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        verbose_name='کاربر',
    )

    student_id = models.CharField(
        max_length=16,
        verbose_name='شناسه دانشجویی',
    )

    phone_number = models.CharField(
        max_length=16,
        verbose_name='شماره تلفن',
    )

    # TODO add extension validator and double check the path
    resume = models.FileField(
        upload_to='files/resume/lecturers/',
        verbose_name='فایل رزومه استاد',
    )
