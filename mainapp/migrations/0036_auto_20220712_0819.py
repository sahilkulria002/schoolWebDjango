# Generated by Django 3.2.13 on 2022-07-12 02:49

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0035_quiz_assignment_assignment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='q_marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_id', models.CharField(default='01', max_length=500)),
                ('course', models.CharField(default='MTH101', max_length=100)),
                ('MM', models.IntegerField(default=10)),
                ('result', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='-', max_length=200), blank=True, null=True, size=3), blank=True, null=True, size=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='quiz_assignment',
            name='content',
        ),
        migrations.RemoveField(
            model_name='quiz_assignment',
            name='result',
        ),
    ]
