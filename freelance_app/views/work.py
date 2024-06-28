
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet

from ..models.work import Service
from ..serializers.work import ServiceSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from ..swagger_content import service


@service.service
class ServiceView(ModelViewSet):
    filterset_fields = ['service_type']
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            # Просматривать услуги может и не авторизованный пользователь
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
