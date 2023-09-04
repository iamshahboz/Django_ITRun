from .models import Book, Author, Rating 
from rest_framework import serializers 

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Book 
        fields = ["id","title","author","isbn_number","genre","description","price","cover_image"]

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Author 
        fields = ["id","full_name"]
    

