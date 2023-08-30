from django.contrib import admin
from .models import Book, Author, Rating


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'author',
        'isbn_number',
        'genre',
        'description',
        'price',
        'cover_image'
    ]
    list_display = ('title','author','genre','price')
    list_filter = ('author','genre')
    search_fields = ('title','author','isbn_number')

class AuthorAdmin(admin.ModelAdmin):
    fields = [
        'full_name'
    ]
    list_display = ('full_name',)

class RatingAdmin(admin.ModelAdmin):
    fields = ['book','rating']
    list_display = ('book','rating')
    list_filter = ('rating',)
    search_fields = ('book',)





admin.site.register(Rating, RatingAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
