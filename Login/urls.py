from django.conf.urls import url
from Login import views

urlpatterns=[
     url('News',views.Index),
     url('home-U',views.greeting),
     url('about',views.about),
     url('contact',views.contact),
     url('login-i',views.login),
     url('sign-up',views.signup),
     #url('edit',views.edit),
     #url('loginuser',views.userLogin),
     #url('logout',views.userLogout),
     url('log-in',views.Login),
     url('register-u',views.register),
     url('news-u',views.news),

]
