from rest_framework import serializers
from .models import Genre, Book, Comment


class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title"]


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "price"]


class GenreSerializer(serializers.ModelSerializer):
    books = BookShortSerializer(source="book_set",many=True,read_only=True)
    class Meta:
        model = Genre
        fields = ["id", "name", "books"]


class GenreDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(source="book_set",many=True,read_only=True)
    class Meta:
        model = Genre
        fields = ["id", "name", "books"]


class BookSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(read_only=True)
    class Meta:
        model = Book
        fields = ["id", "title", "author", "price", "genre"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"