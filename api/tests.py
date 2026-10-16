from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from .models import Genre
from .serializers import GenreSerializer

class GenreTestCase(APITestCase):
    def setUp(self):
        self.genre1 = Genre.objects.create(name="Fantastika")
        self.genre2 = Genre.objects.create(name="Detektiv")
        self.genre3 = Genre.objects.create(name="Tarixiy")

    def test_get(self):
        url = reverse("genre-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        serializer = GenreSerializer(instance=[self.genre1, self.genre2, self.genre3],many=True)
        self.assertEqual(response.data, serializer.data)

