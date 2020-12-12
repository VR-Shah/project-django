from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('reg/',views.reg,name="reg"),
    path('charts/',views.charts,name="charts"),
    path('index/',views.index,name="index"),
]
