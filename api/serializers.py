from rest_framework import serializers
from .models import Genre, Book


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ["id"]
        extra_kwargs = {"name": {"required": True}}


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ["id"]
        depth = 1
        extra_kwargs = {
            "title": {"required": True},
            "author": {"required": True},
            "price": {"required": True},
            "genre": {"required": True}
        }










