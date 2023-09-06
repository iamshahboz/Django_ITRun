from .models import Book, Author, Rating
from rest_framework import serializers 

class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author_name = serializers.CharField(source='author.full_name',read_only=True)
    
    
    class Meta:
        model = Book 
        fields = ["id","title","author","author_name","isbn_number","genre","description","price","cover_image"]

class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Author 
        fields = ["id","full_name"]

class RatingSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    book_name = serializers.CharField(source = "book.title", read_only=True)

    class Meta:
        model = Rating
        fields = ['id','book_name','rating']


    

