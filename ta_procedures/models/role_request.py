from django.db import models

from _helpers.models import TimeModel
from subjects.models import Student
from ta_procedures.models import Role


class RoleRequest(TimeModel):
    STATE_PENDING = 'pending'
    STATE_ACCEPTED = 'accepted'
    STATE_REJECTED = 'rejected'

    STATE_CHOICES = (
        (STATE_PENDING, 'در حال انتظار'),
        (STATE_ACCEPTED, 'تایید شده'),
        (STATE_REJECTED, 'رد شده'),
    )

    student = models.ForeignKey(
        to=Student,
        on_delete=models.CASCADE,
        verbose_name='دانشجو',
    )

    role = models.ForeignKey(
        to=Role,
        on_delete=models.CASCADE,
        verbose_name='وظیفه',
    )

    state = models.CharField(
        max_length=8,
        default=STATE_PENDING,
        choices=STATE_CHOICES,
        verbose_name='وضعیت درخواست',
    )

    description = models.TextField(
        verbose_name='توضیحات',
    )
