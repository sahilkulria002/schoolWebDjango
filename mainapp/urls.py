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
]
