
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homepage, name='homepage'),
    path('api/Book', views.BookListCreate.as_view()),
    path('api/Book/<int:pk>',views.BookAction.as_view()),
    

    ###
    path('api/Author',views.AuthorListCreate.as_view()),
    path('api/Author/<int:pk>',views.AuthorAction.as_view()),
]
