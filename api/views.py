from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .models import Genre, Book
from django.forms import model_to_dict

class all_genres(APIView):
    def get(self, request: Request):
        genres = Genre.objects.all()
        genres_list = []
        for genre in genres:
            genres_list.append(
                {
                    "id": genre.id,
                    "name": genre.name
                }
            )
        return Response(genres_list)

    def post(self, request):
        genre = Genre.objects.create(**request.data)
        return Response(model_to_dict(genre))

class all_books(APIView):
    def get(self, request: Request):
        books = Book.objects.all()
        books_list = []
        for book in books:
            books_list.append(
                {
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "price": book.price,
                    "genre": book.genre.name
                }
            )
        return Response(books_list)

    def post(self, request):
        genre = Genre.objects.get(name=request.data["genre"])
        book = Book.objects.create(
            title=request.data["title"],
            author=request.data["author"],
            price=request.data["price"],
            genre=genre
        )
        return Response(model_to_dict(book))









