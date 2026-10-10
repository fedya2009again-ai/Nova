
from rest_framework.viewsets import ModelViewSet
from .models import Genre, Book, Comment
from .serializers import GenreSerializer, GenreDetailSerializer, BookSerializer, CommentSerializer



class GenreModelViewSet(ModelViewSet):
    queryset = Genre.objects.all()

    def get_serializer_class(self):
        if self.kwargs.get("pk"):
            return GenreDetailSerializer
        return GenreSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer



