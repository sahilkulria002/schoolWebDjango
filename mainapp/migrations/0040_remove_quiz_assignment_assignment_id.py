# Generated by Django 3.2.13 on 2022-07-16 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0039_alter_profile_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_assignment',
            name='assignment_id',
        ),
    ]
