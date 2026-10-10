
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
    books = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ["id", "name", "books"]

    def get_books(self, obj):
        return BookShortSerializer(Book.objects.filter(genre=obj),many=True).data


class GenreDetailSerializer(serializers.ModelSerializer):
    books = BookDetailSerializer(many=True, read_only=True, source="book_set")

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
