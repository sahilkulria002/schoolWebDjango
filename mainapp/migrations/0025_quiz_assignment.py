# Generated by Django 3.2.11 on 2022-06-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='quiz_assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='assignment', max_length=550)),
                ('syllabus', models.CharField(blank=True, max_length=100, null=True)),
                ('t_marks', models.IntegerField(default=10)),
                ('last_date', models.DateTimeField(blank=True, null=True)),
                ('content', models.CharField(default='Name : ', max_length=500)),
                ('result', models.CharField(default='h', max_length=1000)),
            ],
        ),
    ]
