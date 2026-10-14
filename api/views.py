from rest_framework.viewsets import ModelViewSet
from .models import Genre, Book, Comment
from .serializers import GenreSerializer, GenreDetailSerializer, BookSerializer, BookDetailSerializer, CommentSerializer


class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.prefetch_related("book_set")

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return GenreDetailSerializer
        return GenreSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.select_related("genre")
    serializer_class = BookSerializer
    search_fields = ["title", "author"]


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.select_related("book", "user")
    serializer_class = CommentSerializer


