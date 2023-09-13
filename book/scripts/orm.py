from book.models import Book, Author
from django.db import connection
def run():
    # get the objects of the book
#     books = Book.objects.filter()
#     print(books)
#     print(connection.queries)


    # get the author
    # author = Author.objects.all()
    # print(author)
    # print(connection.queries)

    # you can create an instance this way
    # Book.objects.create(
    #     title = 'book added with create method',
    #     author = Author.objects.get(full_name="Lio Messi"),
    #     isbn_number = 32334312,
    #     genre = Book.GenreChoices.SCI_FICTION,
    #     description = "How do know about that, call that this",
    #     price = 21
          #cover_image = 'path/to/your/cover/image.jpg'

    # )
    
    # you can grab the foreign key field from parent model which does not have this field in it
    books = Book.objects.first()
    print(books.ratings.all())
    






    