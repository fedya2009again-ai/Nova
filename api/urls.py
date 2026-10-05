from django.urls import path
from .views import (GenreListCreateView, GenreDetailView, BookListCreateView, BookDetailView, CommentListCreateView, CommentDetailView)

urlpatterns = [
    path("genres/", GenreListCreateView.as_view()),
    path("genres/<int:genre_id>/", GenreDetailView.as_view()),
    path("books/", BookListCreateView.as_view()),
    path("books/<int:book_id>/", BookDetailView.as_view()),
    path("comments/", CommentListCreateView.as_view()),
    path("comments/<int:comment_id>/", CommentDetailView.as_view()),
]