# Generated by Django 3.2.11 on 2022-06-20 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0029_auto_20220620_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='MESSAGE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
                ('tim', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('rom', models.CharField(max_length=200)),
            ],
        ),
    ]
