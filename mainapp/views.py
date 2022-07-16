from datetime import datetime
from re import L
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
                userprofile = profile.objects.create(username=username,name=name,grade=grade, roll_no=roll_no, fname=fname, mname=mname, adress=adress)
                user.save()
                userprofile.save()
                auth.login(request,user)
                return redirect('/?username='+username)

    else :
        classes = [1,2,3,4,5,6,7,8]
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
    if username == 'supersahil' :
        return redirect(supersahil)
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
    for item in qz_ass_obs:
        if item.last_date > timezone.now() :
            quizes_and_assignments.append([item.title, item.course, item.last_date, True])  #### true that deadine is not over
        else :
            quizes_and_assignments.append([item.title, item.course, item.last_date, False])
    quizes_and_assignments.reverse()
    a = prfle.result
    q_res = []
    for i in a :
        quiz = quiz_assignment.objects.get(id = i[0])
        q_res.append([quiz.course, quiz.title, i[1], i[2], quiz.t_marks])

    details = [['Username :' ,username],[
        'Name :' ,  prfle.name],[
        'Roll No. :' , prfle.roll_no],[
        'Class :' , prfle.grade],[
        'Father Name :' , prfle.fname],[
        'Mother Name :' , prfle.mname],[
        'Address :' , prfle.adress]]
    topass = {
        'details':details,
        'coursetitle' : coursetitle,
        'notfs' : notfs,
        'name':prfle.name,
        'quizes' : quizes_and_assignments,
        'q_res' : q_res,
    }
    return render(request, 'profilepage.html',topass)


def supersahil(request) :
    n_list = []
    n_obj = notifications.objects.all()
    for ob in reversed(n_obj) :
        n_list.append([ob.grade_code, ob.statment,ob.id])
    q_list = []
    q_obj = quiz_assignment.objects.all()
    for ob in reversed(q_obj) :
        q_list.append([ob.grade, ob.course, ob.title, ob.id, ob.id  ])
    user_list = []
    user_obj = profile.objects.all()
    for ob in user_obj :
        user_list.append([ob.username, ob.name, ob.grade, ob.fname])
    return render(request, 'super.html', {'n_list' : n_list, 'q_list' : q_list, 'user_list' : user_list})

def coursedetails(request,coursetitle) :
    username=request.user.username
    prfle = profile.objects.get(username=username)
    course = course_shedule.objects.get(course_title=coursetitle)
    quiz_obs = quiz_assignment.objects.filter(Q(course = coursetitle) & Q(type = 'quiz'))
    assignment_obs = quiz_assignment.objects.filter(Q(course = coursetitle) & Q(type = 'assignment'))
    quizes = []
    assignments = []
    for quiz in quiz_obs :
        quizes.append(quiz)
    for assignment in assignment_obs :
        assignments.append(assignment)
    a = prfle.result
    q_res = []
    for i in a :
        quiz = quiz_assignment.objects.get(id = i[0])
        if quiz.course == coursetitle :
            q_res.append([quiz.course, quiz.title, i[1], i[2], quiz.t_marks])
    topass = {
        'name' : prfle.name,
        'course_name' : course.course_name,
        'grade' : prfle.grade,
        'title' :course.course_title,
        'teacher' :course.course_teacher,
        'books' : course.course_books,
        'time' : course.course_time,
        'content' : course.course_content,
        'quizes' : reversed(quizes),
        'assignments' : reversed(assignments),
        'q_res' : q_res,
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

def gen_notification(request) :
    n_grade = request.POST['grade_code']
    n_text = request.POST['n_text']
    if n_grade != '' and n_text != '' :
        new_notification = notifications.objects.create(grade_code = n_grade, statment = n_text)
        new_notification.save()
        msg = messages.info(request, 'Notification saved successfully')
    else :
        msg = messages.info(request, 'Invalid Notification')

    return redirect(supersahil)

def gen_quiz(request) :
    type = request.POST['type']
    title = request.POST['title']
    course = request.POST['course']
    MM = request.POST['MM']
    date = request.POST['date']
    syllabus = request.POST['syllabus']
    grade = request.POST['q_grade']

    if MM==''  or date == '' or grade == '':
        return HttpResponse('Invalid details')
    else :
        new_quiz = quiz_assignment.objects.create(type=type, title=title,
        course=course,syllabus=syllabus,t_marks=MM, last_date=date, grade = grade)
        new_quiz.save()
        return HttpResponse('Quiz/Assignment is created')

def get_q_info(request) :
    q_id = request.POST['q_id_input']
    if quiz_assignment.objects.filter(id = q_id).exists() :
        quiz = quiz_assignment.objects.get(id = q_id)
    else :
        msg = messages.info(request, 'quiz/assignment with this id does not exist')
        return redirect(supersahil)
    q_class = int(quiz.grade)

    q_title = quiz.title
    q_course = quiz.course
    class_students = profile.objects.filter(grade = q_class)
    st_list = []
    for i in class_students :
        st_list.append([i.name, i.roll_no, i.username])
    st_list = sorted(st_list, key= lambda x : x[1])
    topass = {
        'title' : q_title,
        'course' : q_course,
        'st_list' : st_list,
        'grade' : q_class,
        'q_id' : q_id,
        'MM' : quiz.t_marks
    }
    return render(request, 'result.html', topass)
    
def save_result(request) :
    # user = profile.objects.get(username='kim')
    grade = request.POST['q_grade_output']
    q_id = request.POST['q_id']
    class_students = profile.objects.filter(grade = grade)
    st_list = []
    for i in class_students :
        # st_list.append(i.username)
        user=i.username
        marks = request.POST[user+'marks']
        remark = request.POST[user+'remark']
        res = i.result
        if not res :
            res = []
        a = [q_id, marks, remark]
        res.append(a)
        i.result = res
        i.save()

    topass= {
        # 'lst' : ls,
        'grade' : grade,
        'marks' : marks,
        'remark' : remark
    }
    # return render(request, 'test.html', topass)
    msg = messages.info(request, 'Result for quiz/assignment with id : ' + q_id + ' is updated successfully')
    return redirect(supersahil)

def delete(request, n_id) :
    notf = notifications.objects.get(id = n_id)
    notf.delete()
    return redirect(supersahil)

def deletequiz(request, q_id) :
    quiz = quiz_assignment.objects.get(id = q_id)
    quiz.delete()
    return redirect(supersahil)

def deleteuser(request,username) :
    prfle = profile.objects.get(username=username)
    prfle.delete()
    return redirect(supersahil)