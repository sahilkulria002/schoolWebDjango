# Generated by Django 3.2.11 on 2022-06-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_rename_grade_notifications_grade_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_shedule',
            name='course_teacher',
            field=models.CharField(default='Principle', max_length=50),
        ),
        migrations.AddField(
            model_name='course_shedule',
            name='course_time',
            field=models.CharField(default='', max_length=100),
        ),
    ]
