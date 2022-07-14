from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user=<str:username>/', views.profilepage, name='profilepage'),
    path('course/<str:coursetitle>/', views.coursedetails,name='coursedetails'),
    path('send', views.send, name='send'),
    path('inh1', views.inh1, name='inh1'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('asdf<str:but_id>/', views.menu2fun2, name='menu2fin2'),
    path('super', views.supersahil, name='supersahil'),
    path('gen_notification', views.gen_notification, name='gen_notification'),
    path('gen_quiz', views.gen_quiz, name='gen_quiz'),
    path('get_q_info', views.get_q_info, name = 'get_q_info'),
    path('save_result', views.save_result, name='save_result'),
    path('delete/<str:n_id>/',views.delete, name='delete'),
    path('deletequiz/<str:q_id>/', views.deletequiz, name='deletequiz'),
    path('deleteuser/<str:username>/', views.deleteuser, name='deleteuser'),
]
