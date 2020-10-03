from django.shortcuts import render,redirect
from .models import *
from .forms import LoginForm,PrayerForm
from django.contrib import messages
from .forms import ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator


def prayer(request):
    pray = Prayer.objects.all()
    if request.method == "GET":
        form = PrayerForm()
    else:
        form = PrayerForm(request.POST)
        if form.is_valid():
            form.save()
            prayer_item = form.save(commit=False)
            prayer_item.save()
        else:
            form = PrayerForm()
    return render(request,'web/prayer.html',{'form':form,'pray':pray})

def home(request):
    objs = Home_1.objects.all()
    obj = Home.objects.all()
    title = 'homepage'
    return render(request,'web/home.html',{'title':title,'obj':obj,'objs':objs})


def base(request):
    title = 'homepage'
    return render(request,'web/base.html',{'title':title})


def about(request):
    abt = About.objects.all()
    head = 'aboutpage'
    return render(request,'web/about.html',{'head':head,'abt':abt})


def ministries(request):
    min = 'ministries'
    form = Ministries.objects.all()
    context ={'min':min,'form':form}
    return render(request,'web/ministries.html',context)


def gallary(request):
    gall = Gallary.objects.all()
    gal = 'gallery'
    context = {'gal':gal,'gall':gall}
    return render(request,'web/gallary.html',context)


def events(request):
    event = 'Events'
    obj = Events.objects.all()
    paginator = Paginator(obj,2)
    page = request.GET.get('page')
    obj = paginator.get_page(page)
    return render(request,'web/events.html',{'event':event,'obj':obj})

def signup(request):
    title = 'open an account'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('about')

    else:
        form = UserCreationForm()
    return render(request,'web/signup.html',{'form':form,'title':title})

