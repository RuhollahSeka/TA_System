# Generated by Django 3.1.2 on 2020-11-19 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subjects', '0001_initial'),
        ('ta_procedures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursescore',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ta_procedures.course', verbose_name='درس پاس\u200cشده'),
        ),
        migrations.AddField(
            model_name='coursescore',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.student', verbose_name='دانشجو'),
        ),
    ]