import json
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User, Service
from freelance_app.serializers.work import ServiceSerializer


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
