from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Item

class ItemAPITestCase(APITestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='password')
        

        self.url = '/items/'


        self.client = APIClient()

    def test_create_item_unauthorized(self):

        data = {'item_name': 'Test Item'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_item_authorized(self):

        self.client.login(username='testuser', password='password')
        
        data = {'item_name': 'Test Item'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Expecting 201, as item is created
