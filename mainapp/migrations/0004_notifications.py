# Generated by Django 3.2.11 on 2022-06-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20220618_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.CharField(default='All', max_length=25)),
                ('statment', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
