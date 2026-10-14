from rest_framework.viewsets import ModelViewSet
from .models import Genre, Book, Comment
from .serializers import GenreSerializer, GenreDetailSerializer, BookSerializer, CommentSerializer


class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.prefetch_related("book_set").only('id','name')

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return GenreDetailSerializer
        return GenreSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.select_related("genre").defer("price")
    serializer_class = BookSerializer
    search_fields = ["title", "author"]


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.select_related("book", "user").defer("text")
    serializer_class = CommentSerializer
