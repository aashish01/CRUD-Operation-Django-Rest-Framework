from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    #path('add', views.add, name='add'),
   # path('list', views.list, name='list'),
    path('', views.all, name='all'),
    path('rest/', views.itemList.as_view()),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delt/<int:id>', views.delt, name='delt'),
]