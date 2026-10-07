from django.urls import path
from .views import GenreModelViewSet, BookModelViewSet, CommentModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('genre', GenreModelViewSet, basename='genre')
router.register('book', BookModelViewSet, basename='book')
router.register('comment', CommentModelViewSet, basename='comment')

urlpatterns = router.urls

# urlpatterns = [
#     path("genres/", GenreListCreateView.as_view()),
#     path("genres/<int:genre_id>/", GenreDetailView.as_view()),
#     path("books/", BookListCreateView.as_view()),
#     path("books/<int:book_id>/", BookDetailView.as_view()),
#     path("comments/", CommentListCreateView.as_view()),
#     path("comments/<int:comment_id>/", CommentDetailView.as_view()),
# ]