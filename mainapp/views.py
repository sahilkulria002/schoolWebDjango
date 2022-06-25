from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import MESSAGE, profile,notifications,course_shedule, quiz_assignment
from django.contrib.auth.models import User, auth
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from json import dumps

# Create your views here.
def home(request, but_id='school') :
    # if request.user.is_authenticated:
    #     prfle = profile.objects.get(username=request.user.username)
    #     if prfle.photo:
    #         photo = prfle.photo.url
    #     else :
    #         photo='/static/images/empty.png'
    #     grade = str(prfle.grade)
    #     name = prfle.name
    # else :
    #     photo='/static/images/empty.png'
    #     name = None
    #     grade = None
    # buttons = ['School', 'Events', 'Science Projects', 'Extra curricular', 'Summer', 'Student Achievements']
    # q_links=['Children`s Day 2018', 'Youtube']
    # announcements = ['announcement 1']
    # topass = {
    #     'hed1' : ['Home', 'contact us', 'About us'],
    #     'hed2' : 'Thr boss',
    #     'photo': photo,
    #     'name' :name,
    #     'grade' : grade,
    #     'buttons' : buttons,
    #     'q_links' : q_links,
    #     'announcements' : announcements,
    #     'but_id' : but_id
    # }
    # return render(request, 'home.html', topass)
    dicti = {
        'school': ['Principal`s words : ','some',["/static/images/all/img1.jpg","/static/images/all/img4.jpg","/static/images/all/img2.jpg","/static/images/all/img3.jpg","/static/images/all/img5.jpg"]],
    }    
    ls = ','.join(dicti[but_id][2])
    return render(request, 'events.html', {'ls' : ls, 'but_id' : but_id, 'info' : dicti[but_id], 'lst':dicti[but_id][2]})


def menu2fun2(request, but_id) :
    dicti = {
        'school': ['Principal`s words : ','some',["/static/images/all/img1.jpg","/static/images/all/img4.jpg","/static/images/all/img2.jpg","/static/images/all/img3.jpg","/static/images/all/img5.jpg"]],
        'events': ['Cultural Events :','some2',["/static/images/event1.jpg","/static/images/event2.jpg","/static/images/event3.jpg","/static/images/event4.jpg","/static/images/event5.jpg",]],
        'projects': ['Science Projects :','some3',["/static/images/project1.jpg","/static/images/project2.jpg","/static/images/project3.jpg","/static/images/project4.jpg","/static/images/project5.jpg",]],
        'extra': ['Extra curricular Activities : ','some4',["/static/images/extra2.jpg","/static/images/extra1.jpg","/static/images/extra3.jpg","/static/images/extra4.jpg","/static/images/extra5.jpg",]],
        'summer': ['Summer Programmes : ','some5',["/static/images/summer1.jpg","/static/images/summer2.jpg","/static/images/summer3.jpg","/static/images/summer4.jpg","/static/images/summer5.jpg",]],
        'online-studies': ['Online Studies : ','som62',["/static/images/online1.jpg","/static/images/online2.jpg","/static/images/online3.jpg","/static/images/online4.jpg","/static/images/online5.jpg",]],
    }
    ls = ','.join(dicti[but_id][2])
    return render(request, 'events.html', {'ls' : ls, 'but_id' : but_id, 'info' : dicti[but_id], 'lst':dicti[but_id][2]})

def register(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        name = request.POST['name']
        grade = request.POST['grade']
        roll_no = request.POST['roll_no']
        photo = request.FILES['photo']
        password = request.POST['password']
        password2 = request.POST['password2']
        fname = request.POST['fname']
        mname = request.POST['mname']
        adress = request.POST['adress']
        
        if username == '' or name  == '' or  roll_no  == '' or password  == '' :
            messages.info(request,'Please fill all the details')
            return redirect(register)
        else :
            if User.objects.filter(username=username).exists() :
                messages.info(request, 'username already exists')
                return redirect(register)
            elif password != password2 :
                messages.info(request, 'Password not matched')
                return redirect(register)
            else :
                user = User.objects.create_user(username=username, password=password)
                userprofile = profile.objects.create(username=username,name=name,grade=grade, roll_no=roll_no, fname=fname, mname=mname, adress=adress, photo=photo)
                user.save()
                userprofile.save()
                auth.login(request,user)
                return redirect('/?username='+username)

    else :
        classes = [1,2,3,4,5,6,7,8,9,10]
        return render(request, 'register.html', {'classes':classes,'islogin' : False})

def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is None :
            messages.info(request,'invalid credentials')
            return redirect(login)
        else :
            auth.login(request, user)
            return redirect('/user=z/?username='+username+'/')
    return render(request,'register.html',{'islogin' : True})

def logout(request) :
    auth.logout(request)
    return redirect('/')

def profilepage(request,username) :
    username=request.user.username
    prfle = profile.objects.get(username=username)
    grade_query = str(prfle.grade)+','
    notf = notifications.objects.filter(Q(grade_code__contains=grade_query) | Q(grade_code__contains='ll'))
    notfs = []
    for n in reversed(notf) :
        notfs.append(n.statment)
    courses = course_shedule.objects.filter(Q(grade_code__contains=grade_query) | Q(grade_code__contains='ll'))
    coursetitle = []
    course_just_title = []
    for course in courses :
        coursetitle.append([course.course_title, course.course_name, course.course_teacher])
        course_just_title.append(course.course_title)
    qz_ass_obs = quiz_assignment.objects.filter(course__in = course_just_title)
    quizes_and_assignments = []
    res = []
    for item in qz_ass_obs:
        if item.last_date > timezone.now() :
            quizes_and_assignments.append([item.title, item.course, item.last_date, True])  #### true that deadine is not over
        else :
            quizes_and_assignments.append([item.title, item.course, item.last_date, False])
        if item.result :
            res.append(item.result)
    quizes_and_assignments.reverse()
    if prfle.photo :
        photo = prfle.photo
        photo = photo.url
    else :
        photo = '/media/images/empty.png'
    details = [['Username :' ,username],[
        'Name :' ,  prfle.name],[
        'Roll No. :' , prfle.roll_no],[
        'Class :' , prfle.grade],[
        'Father Name :' , prfle.fname],[
        'Mother Name :' , prfle.mname],[
        'Address :' , prfle.adress]]
    topass = {
        'details':details,
        'photo' : photo,
        'coursetitle' : coursetitle,
        'notfs' : notfs,
        'name':prfle.name,
        'quizes' : quizes_and_assignments,
        'res' : res,
    }
    return render(request, 'profilepage.html',topass)

def coursedetails(request,coursetitle) :
    username=request.user.username
    prfle = profile.objects.get(username=username)
    if prfle.photo :
        photo = prfle.photo
        photo = photo.url
    else :
        photo = '/media/images/empty.png'
    course = course_shedule.objects.get(course_title=coursetitle)
    quiz_obs = quiz_assignment.objects.filter(Q(course = coursetitle) & Q(type = 'quiz'))
    assignment_obs = quiz_assignment.objects.filter(Q(course = coursetitle) & Q(type = 'assignment'))
    quizes = []
    assignments = []
    for quiz in quiz_obs :
        quizes.append(quiz)
    for assignment in assignment_obs :
        assignments.append(assignment)
    topass = {
        'name' : prfle.name,
        'photo' : photo,
        'course_name' : course.course_name,
        'grade' : prfle.grade,
        'title' :course.course_title,
        'teacher' :course.course_teacher,
        'books' : course.course_books,
        'time' : course.course_time,
        'content' : course.course_content,
        'quizes' : reversed(quizes),
        'assignments' : reversed(assignments)
    }
    return render(request, 'coursedetails.html',topass)

def inh1(request) :
    return render(request, 'inh1.html')


def send(request) :
    username = request.POST['username']
    message = request.POST['message']
    room_id = request.POST['room_id']
    if message != '':
        n_message = MESSAGE.objects.create(user=username,text=message,rom=room_id)
        n_message.save()
    return HttpResponse('Message sent')

def getMessages(request,room) :
    msgs = MESSAGE.objects.filter(rom=room)
    a = list(msgs.values())
    a.reverse()
    return JsonResponse({'messages' : a})

