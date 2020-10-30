from django.db import models

from users.models import Teacher


class Subject(models.Model):
    ODD_SEMESTER = 'odd'
    EVEN_SEMESTER = 'even'
    SUMMER_SEMESTER = 'summer'

    SEMESTER_CHOICES = (
        (ODD_SEMESTER, 'ترم فرد'),
        (EVEN_SEMESTER, 'ترم زوج'),
        (SUMMER_SEMESTER, 'ترم تابستان'),
    )

    name = models.CharField(
        max_length=128,
        verbose_name='نام درس',
    )

    subject_id = models.CharField(
        max_length=16,
        verbose_name='شناسه درس',
    )

    year = models.PositiveSmallIntegerField(
        verbose_name='سال ارائه شدن درس',
    )

    semester = models.CharField(
        max_length=8,
        choices=SEMESTER_CHOICES,
        verbose_name='ترم ارائه شدن درس',
    )

    teacher = models.ForeignKey(
        to=Teacher,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='استاد درس',
    )
