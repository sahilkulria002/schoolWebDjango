from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime

# Create your models here.
class profile(models.Model):
    username = models.CharField(max_length=25,default='username')
    name = models.CharField(max_length=25, default='name')
    grade = models.IntegerField(default=0)
    roll_no = models.IntegerField(default=0)
    fname = models.CharField(max_length=50, default='')
    mname = models.CharField(max_length=50, default='')
    adress = models.CharField(max_length=200, default='')
    result = ArrayField(ArrayField(models.CharField(max_length=200,default='-'),size=3, blank=True, null=True),size=100,default=list)
    

class notifications(models.Model):
    grade_code = models.CharField(max_length=25, default='All')
    statment = models.CharField(max_length=500, default='')

class course_shedule(models.Model):
    course_title = models.CharField(max_length=50,default='')
    course_name= models.CharField(max_length=100, default='')
    grade_code = models.CharField(max_length=50, default='')
    course_teacher = models.CharField(max_length=50, default='Principle')
    course_time = models.CharField(max_length=100, default='')
    course_books = ArrayField(models.CharField(max_length=200,default=''),size=3,blank=True,null=True)
    course_content = models.CharField(max_length=1500, null=True, blank=True)

class quiz_assignment(models.Model) :
    type = models.CharField(max_length=550,default='assignment')
    title = models.CharField(max_length=500, default='assignment 1')
    course = models.CharField(max_length=100,default='MTH101')
    syllabus = models.CharField(max_length=100,null=True,blank=True)
    t_marks = models.CharField(max_length=100, default='10')
    last_date = models.DateTimeField(null=True,blank=True)
    assignment_id = models.CharField(max_length=500,default='01')
    grade = models.CharField(max_length=50, default='')

class MESSAGE(models.Model) :
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    tim = models.DateTimeField(default = datetime.now, blank=True)
    rom = models.CharField(max_length=200)
