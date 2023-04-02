from rest_framework.test import APITestCase
from rest_framework import status

from user.models import User, Employee


class UserTestCase(APITestCase):

    def setUp(self):
        data = {
            'email': 'random.user@gmail.com',
            'name': 'Madara',
            'password': '123'
        }
        response = self.client.post('/api/register/', data)
        self.user = User.objects.get(email=response.data['email'])

        response = self.client.post('/api/login/', {
            'email': 'random.user@gmail.com',
            'password': '123'
        })
        self.token = response.data['token']

    def test_user_data(self):
        self.assertEqual(self.user.email, 'random.user@gmail.com')

    def test_fail_email_login(self):
        response = self.client.post('/api/login/', {
            'email': 'some.user@gmail.com',
            'password': '123'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_fail_password_login(self):
        response = self.client.post('/api/login/', {
            'email': 'random.user@gmail.com',
            'password': '1234'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_success_login(self):
        response = self.client.post('/api/login/', {
            'email': 'random.user@gmail.com',
            'password': '123'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_fail_register_request(self):
        data = {
            'email': 'random.user@gmail.com',
            'name': 'Madara',
            'password': '123'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_success_register_request(self):
        data = {
            'email': 'another.user@gmail.com',
            'name': 'Minato',
            'password': '123'
        }
        response = self.client.post('/api/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_fail_get_users_request(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_success_get_users_request(self):
        response = self.client.get('/api/users/', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
