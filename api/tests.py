from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import json


# Create your tests here.

class KeyValueStoreTest(APITestCase):
    end_point = '/values/'
    content_type = 'application/json'
    databases = {}

    def test_empty_post(self):
        client = APIClient()
        data = {}
        response = client.post(self.end_point, json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'body can not be empty'})

    def test_new_data_post(self):
        client = APIClient()
        data = {'key1': 'value1', 'key2': 'value2'}
        response = client.post(self.end_point, json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, data)

    def test_no_new_data_post(self):
        client = APIClient()
        data = {'key1': 'value1'}
        response = client.post(self.end_point, json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {})

    def test_retrieve_data(self):
        client = APIClient()
        response = client.get(self.end_point)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'key1': 'value1', 'key2': 'value2'})

    def test_retrieve_data_with_key(self):
        client = APIClient()
        data = {'keys': 'key1,key3,new_key'}
        response = client.get(self.end_point, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'key1': 'value1'})

    def test_update_with_empty_body(self):
        client = APIClient()
        data = {}
        response = client.patch(self.end_point, json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'error': 'body can not be empty'})

    def test_update_with_not_empty_body(self):
        client = APIClient()
        data = {'key1': 'new value1'}
        response = client.patch(self.end_point, json.dumps(data), content_type=self.content_type)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, data)
