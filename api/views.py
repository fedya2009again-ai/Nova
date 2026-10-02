from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class GenreListCreateView(ListCreateAPIView):
    serializer_class = GenreSerializer
    lookup_field = "id"
    lookup_url_kwarg = "genre_id"

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer

class GenreDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = GenreSerializer
    lookup_field = "id"
    lookup_url_kwarg = "genre_id"

    def get_queryset(self):
        return Genre.objects.all()

    def get_serializer_class(self):
        return GenreSerializer

class BookListCreateView(ListCreateAPIView):
    serializer_class = BookSerializer
    lookup_field = "id"
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer


class BookDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    lookup_field = "id"
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Book.objects.all()

    def get_serializer_class(self):
        return BookSerializer



# class all_genres(APIView):
#     def get(self, request: Request, pk: int = None):
#         if pk is None:
#             genres = Genre.objects.all()
#             serializer = GenreSerializer(genres, many=True)
#             return Response(serializer.data)
#         else:
#             genre = get_object_or_404(Genre, pk=pk)
#             return Response(GenreSerializer(genre).data)
#
#     def post(self, request, pk: int = None):
#         if pk:
#             return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         serializer = GenreSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         genre = serializer.save()
#         return Response(GenreSerializer(genre).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request, pk: int = None):
#         if pk is None:
#             return Response({"message": "Method PUT not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         genre = get_object_or_404(Genre, pk=pk)
#         serializer = GenreSerializer(data=request.data, instance=genre)
#         serializer.is_valid(raise_exception=True)
#         return Response(GenreSerializer(serializer.save()).data)
#
#     def delete(self, request, pk: int = None):
#         if pk is None:
#             return Response({"message": "id required"}, status=status.HTTP_400_BAD_REQUEST)
#         genre = get_object_or_404(Genre, pk=pk)
#         genre.delete()
#         return Response({"message": "Genre delete successful"}, status=status.HTTP_204_NO_CONTENT)
#
# class all_books(APIView):
#     def get(self, request: Request, pk: int = None):
#         if pk is None:
#             books = Book.objects.all()
#             serializer = BookSerializer(books, many=True)
#             return Response(serializer.data)
#         else:
#             book = get_object_or_404(Book, pk=pk)
#             return Response(BookSerializer(book).data)
#
#     def post(self, request, pk: int = None):
#         if pk:
#             return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         book = serializer.save()
#         return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request, pk: int = None):
#         if pk is None:
#             return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(data=request.data, instance=book)
#         serializer.is_valid(raise_exception=True)
#         return Response(BookSerializer(serializer.save()).data)
#
#     def delete(self, request, pk: int = None):
#         if pk is None:
#             return Response({"message": "id required"}, status=status.HTTP_400_BAD_REQUEST)
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response({"message": "Book delete successful"}, status=status.HTTP_204_NO_CONTENT)








