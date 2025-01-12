# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from ..models import User, Service
#
# class UserTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='test',
#             email='test@gmail.com',
#             password='L31!83Qaa',
#             phone='+79913131822',
#             first_name='Иван',
#             surname='Иванов',
#             patronymic='Иванович'
#         )
#
# class ServiceTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             username='test',
#             email='test@gmail.com',
#             password='L31!83Qaa',
#             phone='+79913131822',
#             first_name='Иван',
#             surname='Иванов',
#             patronymic='Иванович'
#         )
#         self.client.login(username='test',  password='L31!83Qaa')
#         self.url = reverse('service-list')
#         self.service_data = {
#             'service_type': 'web_development',
#             'name': 'Web Development Service',
#             'desk': 'This is a test service for web development.',
#             'price': 1000,
#             'executor': self.user.id
#         }
#
#         # Проверка успешного входа
#         self.assertTrue(self.client.login(username='test', password='L31!83Qaa'))
#
#     def test_create_service(self):
#         response = self.client.post(self.url, self.service_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Service.objects.count(), 1)
#         self.assertEqual(Service.objects.get().name, 'Web Development Service')
#
#     def test_get_service_list(self):
#         self.client.post(self.url, self.service_data)
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)

    # def test_update_service(self):
    #     service = Service.objects.create(**self.service_data)
    #     update_data = {
    #         'service_type': 'marketing',
    #         'name': 'Updated Service',
    #         'desk': 'Updated description.',
    #         'price': 1500,
    #         'executor': self.user.id
    #     }
    #     response = self.client.put(reverse('service-detail', args=[service.id]), update_data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     service.refresh_from_db()
    #     self.assertEqual(service.name, 'Updated Service')
    #
    # def test_delete_service(self):
    #     print(**self.service_data)
    #     service = Service.objects.create(**self.service_data)
    #     response = self.client.delete(reverse('service-detail', args=[service.id]))
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Service.objects.count(), 0)

# class OrderTests(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(
#             email='test@example.com',
#             username='testuser',
#             password='testpassword',
#             phone='1234567890'
#         )
#         self.client.login(username='testuser', password='testpassword')
#         self.order_url = reverse('order-list')
#         self.order_data = {
#             'service_type': 'web_development',
#             'customer': self.user.id,
#             'service': None,  # Здесь нужно указать существующий сервис
#         }
#
#     def test_create_order(self):
#         # Сначала создаем сервис, чтобы связать его с заказом
#         service = Service.objects.create(
#             service_type='web_development',
#             name='Web Development Service',
#             desk='This is a test service for web development.',
#             price=1000,
#             executor=self.user
#         )
#         self.order_data['service'] = service.id
#         response = self.client.post(self.order_url, self.order_data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Order.objects.count(), 1)
#
#     def test_get_order_list(self):
#         service = Service.objects.create(
#             service_type='web_development',
#             name='Web Development Service',
#             desk='This is a test service for web development.',
#             price=1000,
#             executor=self.user
#         )
#         self.order_data['service'] = service.id
#         self.client.post(self.order_url, self.order_data)
#         response = self.client.get(self.order_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#
#     def test_update_order(self):
#         service = Service.objects.create(
#             service_type='web_development',
#             name='Web Development Service',
#             desk='This is a test service for web development.',
#             price=1000,
#             executor=self.user
#         )
#         order = Order.objects.create(
#             service_type='web_development',
#             customer=self.user,
#             service=service
#         )
#         update_data = {
#             'service_type': 'marketing',
#             'customer': self.user.id,
#             'service': service.id
#         }
#         response = self.client.put(reverse('order-detail', args=[order.id]), update_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_delete_order(self):
#         service = Service.objects.create(
#             service_type='web_development',
#             name='Web Development Service',
#             desk='This is a test service for web development.',
#             price=1000,
#             executor=self.user
#         )
#         order = Order.objects.create(
#             service_type='web_development',
#             customer=self.user,
#             service=service
#         )
#         response = self.client.delete(reverse('order-detail', args=[order.id]))
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Order.objects.count(), 0)

import json
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User, Service
from freelance_app.serializers.work import ServiceSerializer, OrderSerializer


class ServiceViewSetTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='test@example.com', password='123456')
        self.client.login(username='test', password='123456')
        self.service = Service.objects.create(
            service_type='web_development',
            name='Website Development',
            desk='Website development services',
            price=1000,
            executor=self.user
        )
        self.assertTrue(self.client.login(username='test', password='123456'))

    def test_get_all_services(self):
        response = self.client.get(reverse('service-list'))
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_service(self):
        response = self.client.get(reverse('service-detail', args=[self.service.id]))
        serializer = ServiceSerializer(self.service)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_create_service(self):
        data = {
            'service_type': 'marketing',
            'name': 'Marketing Services',
            'desk': 'Marketing services for businesses',
            'price': 2000,
            'executor': self.user.id
        }
        response = self.client.post(reverse('service-list'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Service.objects.filter(name='Marketing Services').exists())

    def test_update_service(self):
        data = {
            'name': 'Updated Website Development',
            'desk': 'Updated website development services',
            'price': 1500
        }
        print(self.service.id)
        response = self.client.put(reverse('service-detail', args=[self.service.id]), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.service.refresh_from_db()
        self.assertEqual(self.service.name, 'Updated Website Development')
        self.assertEqual(self.service.desk, 'Updated website development services')
        self.assertEqual(self.service.price, 1500)

    def test_delete_service(self):
        response = self.client.delete(reverse('service-detail', args=[self.service.id]))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Service.objects.filter(id=self.service.id).exists())
