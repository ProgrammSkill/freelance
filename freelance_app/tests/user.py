from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from freelance_app.models.user import User


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
        print(User.objects.filter(email='test@gmail.com').exists())

        """Тестирование авторизации по имени пользователя"""
        url = reverse('auth')
        response = self.client.post(url,
                                    {'username': 'test', 'password': 'L31!83Qaa', 'login_params': 'username'})
        print(response.data)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_authenticate_with_email(self):
        """Тестирование авторизации по электронной почте"""
        url = reverse('auth')
        response = self.client.post(url, {'email': 'test', 'password': 'L31!83Qaa',
                                          'login_params': 'email'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_authenticate_with_invalid_credentials(self):
        """Тестирование авторизации с неверными учетными данными"""
        url = reverse('auth')
        response = self.client.post(url,
                                    {'username': 'testuser', 'password': 'wrongpassword', 'login_params': 'username'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Логин или пароль неверный')

    def test_authenticate_with_nonexistent_user(self):
        """Тестирование авторизации с несуществующим пользователем"""
        url = reverse('auth')  # Убедитесь, что используете правильное имя URL
        response = self.client.post(url,
                                    {'username': 'nonexistent', 'password': 'testpassword', 'login_params': 'username'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['message'], 'Логин или пароль неверный')

    def test_authenticate_without_login_params(self):
        """Тестирование авторизации без указания параметров входа"""
        url = reverse('auth')
        response = self.client.post(url, {'username': 'testuser', 'password': 'testpassword'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('login_params', response.data)