from django.urls import path
from .views import GenreListCreateView, GenreDetailView, BookListCreateView, BookDetailView


urlpatterns = [
    path("genres/", GenreListCreateView.as_view()),
    path("genres/<int:pk>/", GenreDetailView.as_view()),

    path("books/", BookListCreateView.as_view()),
    path("books/<int:pk>/", BookDetailView.as_view()),
]