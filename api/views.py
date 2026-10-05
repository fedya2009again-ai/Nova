from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Genre, Book, Comment
from .serializers import GenreSerializer, BookSerializer, CommentSerializer
from .permissions import IsCommentOwner


class GenreListCreateView(ListCreateAPIView):
    serializer_class = GenreSerializer
    lookup_field = "id"
    lookup_url_kwarg = "genre_id"
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer


class GenreDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    lookup_field = "id"
    lookup_url_kwarg = "genre_id"
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer


class BookListCreateView(ListCreateAPIView):
    serializer_class = BookSerializer
    lookup_field = "id"
    lookup_url_kwarg = "book_id"
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = "id"
    lookup_url_kwarg = "book_id"
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer


class CommentListCreateView(ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        return CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer
    lookup_field = "id"
    lookup_url_kwarg = "comment_id"
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsCommentOwner]

    def get_queryset(self):
        return Comment.objects.all()

    def get_serializer_class(self):
        return CommentSerializer