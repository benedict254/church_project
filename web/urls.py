from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'), 
    path('ministries/',views.ministries,name='ministries'),
    path('prayer/',views.prayer,name='prayer'),
    path('gallary/',views.gallary,name='gallary'),
    path('events/',views.events,name='events'),
    path('signup/',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
]
