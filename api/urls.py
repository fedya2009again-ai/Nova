from django.urls import path
from .views import all_genres, all_books

urlpatterns = [
    path('genres/', all_genres.as_view()),
    path('genres/<int:pk>/', all_genres.as_view()),

    path('books/', all_books.as_view()),
    path('books/<int:pk>/', all_books.as_view()),
]