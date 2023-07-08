from django.contrib import admin
from django.urls import path
from graphapp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
       path("", views.index,name='home'),
       #path("", views.ulogin,name='login'),
       path("login/", views.ulogin,name='login'),
       path("signup", views.signupp,name='signup'),
       #path("home", views.index,name='home'),
       path("logout", views.LogoutPage,name='logout'),
       path("upload/",views.upload, name="upload")
] 

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)