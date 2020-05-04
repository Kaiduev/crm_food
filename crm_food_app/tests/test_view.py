from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, RequestsClient, APIRequestFactory
from django.urls import path, include
from crm_food_app.models import *


class TableRequestsTestCase(APITestCase):

    def test_table_get(self):
        print("Test GET Table")
        client = RequestsClient()
        url = 'http://testserver/tables'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_table_post(self):
        print("setup post")
        client = APIClient()
        url = 'http://testserver/tables'
        data = {'name': 'Table№1'}
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
