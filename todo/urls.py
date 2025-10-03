from django.contrib import admin
from django.urls import path,include
from todo import views
urlpatterns = [
    path('',views.index,name='homepage'),
    path('delete/<int:pk>/',views.delete_task,name='delete')
]