import io

import mock
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files import File

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from menu.models import Category, Allergen


class MainCourseTests(APITestCase):

    def setUp(self):

        file_mock = mock.MagicMock(spec=File)
        file_mock.name = "No_photo.jpg"

        user_test1 = User.objects.create_user(username='SpongeBob', password='SquarePants')
        user_test1.save()
        user_test2 = User.objects.create_user(username='Patrick', password='Star')
        user_test2.save()

        Category.objects.create(name="Напитки", slug="drinks")
        Allergen.objects.create(name="Рыба")

        image = io.BytesIO()
        Image.new("RGB", (150, 150)).save(image, "JPEG")
        image.seek(0)

        image_file = SimpleUploadedFile("No_photo.jpg", image.getvalue())

        self.data = {
            "category": "Напитки",
            "allergen":  "Рыба",
            "image": image_file,
            "name": "Бульон",
            "nutritionalValue": 300,
            "description": "Чтобы ничего не пропадало",
            "price": 500.00,
            "available": True,
            "slug": "water"
        }

        self.user_test1_token = Token.objects.create(user=user_test1)
        self.user_test2_token = Token.objects.create(user=user_test2)

    def test_add_dish(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.post(reverse('menu:add'), self.data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dish_list(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test1_token.key)
        response = self.client.get(reverse('menu:add'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
