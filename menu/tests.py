from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class MainCourseTestCase(APITestCase):

    def test_mainCourse(self):
        response = self.client.get(reverse('menu:add'))
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dish_page_status_code(self):
        url = reverse("menu:add")
        data = {
                "id": "15",
                "category": "Напитки",
                "allergen": "рыба",
                "name": "Пелядевый сок",
                "nutritionalValue": "100",
                "description": "Только у нас",
                "price": "5000",
                "image": "/media/photo/No_photo_zuuzXmv.jpg",
                "available": '',
                "slug": "juice"
                }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
