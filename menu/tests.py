from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class MainCourseTestCase(APITestCase):

    # def test_mainCourse(self):
    #     response = self.client.get(reverse('menu:add'))
    #     print(response)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dish_page_status_code(self):
        url = reverse("menu:add")
        data = {
                "category": "Напитки",
                "allergen": [
                    "Рыба"
                ],
                "name": "Пелядевый сок",
                "nutritionalValue": 100,
                "description": "Только у нас!",
                "price": 300.00,
                "image": "/static/img/No_photo.jpg",
                "available": "true",
                "slug": "juice"
                }
        response = self.client.post(url, data, content_type="multipart/form-data")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
