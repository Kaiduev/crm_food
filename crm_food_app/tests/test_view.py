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
        print("Test POST table")
        client = RequestsClient()
        url = 'http://testserver/tables'
        data = {"id": 1, "name": "Table№1"}
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_table_put(self):
        print("Setup EDIT Table")
        self.table = Table.objects.create(name="Table№1")
        url = '/tables/1'
        response = self.client.get(url)
        data = {"name": "table"}
        factory = APIRequestFactory()
        response_put = factory.post(url, data=data, format='json')
        self.assertEqual(self.table.name, 'table')


class RoleRequestsTestCase(APITestCase):

    def test_role_get(self):
        print("Test GET Role")
        client = RequestsClient()
        url = 'http://testserver/roles'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

