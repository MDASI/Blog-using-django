from django.http import HttpResponse
from newsapi import NewsApiClient
from Login import models
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from Login.forms import DetailForm
#####################################
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def Index(request):

    newsapi = NewsApiClient(api_key ='3e269940254a4a37aa612b4c22986c0c')
    top = newsapi.get_top_headlines(sources ='techcrunch')

    l = top['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'news/Newss.html', context ={"mylist":mylist})
    ########################################################################################

def news(request):
    newsapi = NewsApiClient(api_key ='3e269940254a4a37aa612b4c22986c0c')
    all_articles = newsapi.get_everything(q='cricket',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2020-12-01',
                                      to='2020-12-12')

    l = all_articles['articles']
    desc =[]
    news =[]
    img =[]

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'news/Newss.html', context ={"mylist":mylist})
    ################

    ########################################################################################
def showResult(request):
  s="<h1>result is</h1>"
  return HttpResponse(s)
def greeting(request):
    s=render(request,'home/home.html')
    return (s)
def about(request):
    s=render(request,'home/about.html')
    return (s)
def contact(request):
    s=render(request,'home/contact.html')
    return (s)
def login(request):
    s=render(request,'Login/index.html')
    return (s)
def signup(request):
    s=render(request,'Login/register.html')
    return (s)
#from Login.forms import NewBookForm, Searchform



#################### index#######################################
def register(request):
    if request.method == 'POST':
        form =UserRegisterForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login/home-U')
    else:
        form = UserRegisterForm()
    return render(request, 'Login/register.html', {'form': form})


########### register here #####################################


################ login forms###################################################
def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request)
            messages.success(request, f' wecome {username} !!')
            return redirect('Login/home-U')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'Login/index.html', {'form':form, 'title':'log in'})
