from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet
from ..models.work import Service, Order, Tag
from ..serializers.work import ServiceSerializer, OrderSerializer, TagSerializer, TagListSerializer
from rest_framework import permissions, generics, mixins, viewsets
from ..swagger_content import work


@work.service
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


@work.order
class OrderView(ModelViewSet):
    filterset_fields = ['service_type']
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            # Просматривать заказы может и не авторизованный пользователь
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


@extend_schema(tags=['Tags'])
class TagView(mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                                 viewsets.GenericViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Tags'])
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
