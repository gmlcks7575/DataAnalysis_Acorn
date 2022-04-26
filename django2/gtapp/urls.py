# main urls.py로 부터 위임받은 urls 입니다.
from django.urls import path
from gtapp import views

urlpatterns = [
    path('insert', views.insertFunc),
    #path('insertok', views.insertokFunc),
]