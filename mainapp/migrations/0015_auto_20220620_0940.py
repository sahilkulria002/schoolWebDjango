# Generated by Django 3.2.11 on 2022-06-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_quiz_assignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_assignment',
            name='ob_marks',
        ),
        migrations.AddField(
            model_name='quiz_assignment',
            name='result',
            field=models.CharField(default='Result has not decleared yet', max_length=50),
        ),
    ]