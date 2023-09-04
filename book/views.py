from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework import generics 
from .models import Book, Author, Rating
from .serializers import  BookSerializer, AuthorSerializer



def homepage(request):
    return HttpResponse("This is homepage")

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = BookSerializer

class BookAction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().order_by("-id")
    serializer_class = BookSerializer

class AuthorListCreate(generics.ListCreateAPIView):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = AuthorSerializer

class AuthorAction(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all().order_by("-id")
    serializer_class = AuthorSerializer













