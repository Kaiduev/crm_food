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
        # self.assertEqual(self.table.name, 'table')


class RoleRequestsTestCase(APITestCase):

    def test_role_get(self):
        print("Test GET Role")
        client = RequestsClient()
        url = 'http://testserver/roles'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_role_post(self):
        print("Test POST Role")
        client = RequestsClient()
        url = 'http://testserver/roles'
        data = {"id": 1, "name": "waiter"}
        response = client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DepartmentRequestsTestCase(APITestCase):

    def test_department_get(self):
        print("Test GET Department")
        client = RequestsClient()
        url = 'http://testserver/departments/'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_department_post(self):
        print("Test POST Department")
        client = RequestsClient()
        url = 'http://testserver/departments'
        data = {"id": 1, "name": "kitchen" }
        response = client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MealCategoryRequestsTestCase(APITestCase):

    def test_category_get(self):
        print("Test GET Request")
        client = RequestsClient()
        url = 'http://testserver/meal/categories/'
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_post(self):
        print("Test POST Request")
        self.department = Department.objects.create(name="kitchen")
        client = RequestsClient()
        url = 'http://testserver/meal/categories/'
        data = {"id": 1, "name": "Plov", "department": self.department}
        response = client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
