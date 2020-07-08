import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from menu.models import MainCourse
from menu.serializers import MainCourseSerializer


class MainCourseTestCase(APITestCase):

    def setUP(self):
        self.user = User.objects.create_user(username="SpongeBob", password="SquarePants")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHENTICATION="Token " + self.token)

    # def test_mainCourse(self):
    #     # factory = APIRequestFactory()
    #     # user = User.objects.get(username='olivia')
    #     # view = AccountDetail.as_view()
    #
    #     # Make an authenticated request to the view...
    #     # request = factory.get(reverse('menu:add'))
    #     # force_authenticate(request, user=user)
    #     # response = view(request)
    #     client = APIClient()
    #     client.login(username='admin', password='admin')
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
