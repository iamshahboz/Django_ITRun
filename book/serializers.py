from .models import Book, Author, Rating 
from rest_framework import serializers 

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ["title","author","isbn_number","genre","description","price","cover_image"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author 
        fields = ["full_name"] # ["__all__"]

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating 
        fields = ["book","rating"]
    

