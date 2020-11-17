from django.db import models

from subjects.models import Student, Subject


class SubjectScore(models.Model):
    user_profile = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='حساب کاریری'
    )

    subject = models.ForeignKey(
        to=Subject,
        on_delete=models.CASCADE,
        verbose_name='درس پاس‌شده',
    )

    score = models.PositiveSmallIntegerField(
        verbose_name='نمره‌ی درس',
    )
