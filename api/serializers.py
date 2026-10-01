from rest_framework import serializers
from .models import Genre, Book


class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)

    def update(self, instance:Genre, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    author = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    genre_id = serializers.IntegerField()

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance:Book, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.price = validated_data.get("price", instance.price)
        instance.genre_id = validated_data.get("genre_id", instance.genre_id)
        instance.save()
        return instance











