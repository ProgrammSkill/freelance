from urllib.parse import urlencode
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import User


class AuthViewTests(APITestCase):

    @classmethod
    def setUpTestData(cls):
        # Создание тестового пользователя
        cls.user = User.objects.create_user(
            username='test',
            email='test@gmail.com',
            password='L31!83Qaa',
            phone='+79913131822',
            first_name='Иван',
            surname='Иванов',
            patronymic='Иванович'
        )

    def test_authenticate_with_username(self):
        """Тестирование авторизации по имени пользователя"""
        url = reverse('auth')
        query_params = urlencode({'login_params': 'username'})  # Кодируем параметры запроса
        url = f"{url}?{query_params}"  # Формируем полный URL с параметрами
        headers = {
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = self.client.post(url,
                                    {'username': 'test', 'password': 'L31!83Qaa'},
                                    **headers)  # Передача заголовка

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_authenticate_with_email(self):
        """Тестирование авторизации по электронной почте"""
        url = reverse('auth')
        query_params = urlencode({'login_params': 'email'})  # Кодируем параметры запроса
        url = f"{url}?{query_params}"  # Формируем полный URL с параметрами
        headers = {
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = self.client.post(url, {'email': 'test@gmail.com', 'password': 'L31!83Qaa'},
                                    **headers)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_authenticate_with_invalid_credentials(self):
        """Тестирование авторизации с неверными учетными данными"""
        url = reverse('auth')
        query_params = urlencode({'login_params': 'username'})  # Кодируем параметры запроса
        url = f"{url}?{query_params}"  # Формируем полный URL с параметрами
        headers = {
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = self.client.post(url,
                                    {'username': 'testuser', 'password': 'wrongpassword'}, **headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Логин или пароль неверный')

    def test_authenticate_with_nonexistent_user(self):
        """Тестирование авторизации с несуществующим пользователем"""
        url = reverse('auth')  # Убедитесь, что используете правильное имя URL
        query_params = urlencode({'login_params': 'username'})  # Кодируем параметры запроса
        url = f"{url}?{query_params}"  # Формируем полный URL с параметрами
        headers = {
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = self.client.post(url,
                                    {'username': 'nonexistent', 'password': 'testpassword'}, **headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Логин или пароль неверный')

    def test_authenticate_without_login_params(self):
        """Тестирование авторизации без указания параметров входа"""
        url = reverse('auth')
        headers = {
            'HTTP_USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

        response = self.client.post(url, {'username': 'test', 'password': 'L31!83Qaa'}, **headers)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('login_params', response.data)