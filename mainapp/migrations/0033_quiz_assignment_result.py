# Generated by Django 3.2.11 on 2022-06-23 04:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0032_delete_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz_assignment',
            name='result',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='-', max_length=200), blank=True, null=True, size=3), blank=True, null=True, size=100),
        ),
    ]
