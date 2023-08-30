
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('api/Book', views.BookListCreate.as_view()),
]
