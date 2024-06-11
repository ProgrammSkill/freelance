from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import generics, status
from .models import *
from .serializers import *
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class IsExecutor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ExecutorRetrieveView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Executor'])
class ExecutorUpdateView(generics.UpdateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer
    permission_classes = (IsExecutor,)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            return Executor.objects.filter(user=user)

        raise PermissionDenied()


@extend_schema(tags=['Executor'])

class ExecutorCreateView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


@extend_schema(tags=['Executor'])
class ExecutorListView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


@extend_schema(tags=['Customer'])
class CustomerRetrieveView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Customer'])
class CustomerUpdateView(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Customer'])
class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CreateCustomerSerializer


@extend_schema(tags=['Customer'])
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@extend_schema(tags=['Service'])
class ServiceRetrieveView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Service'])
class ServiceUpdateView(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Service'])
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = CreateServiceSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Service'])
class ServiceListView(generics.ListAPIView):
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = Service.objects.all()
        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        executor = params.get('executor', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        return queryset


@extend_schema(tags=['Order'])
class OrderRetrieveView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly

    def get_queryset(self):
        queryset = Order.objects.all()
        params = self.request.query_params

        service_type = params.get('service', None)
        price = params.get('price', None)
        customer = params.get('customer', None)

        if service_type:
            queryset = queryset.filter(service_type=service_type)

        if price:
            queryset = queryset.filter(price__lte=price)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        return queryset


@extend_schema(tags=['Order'])
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Order'])
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Order'])
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@extend_schema(tags=['Tag'])
class TagRetrieveView(generics.RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Tag'])
class TagUpdateView(generics.UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Tag'])
class TagCreateView(generics.CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = CreateTagSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Tag'])
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


@extend_schema(tags=['Ordering'])
class OrderingRetrieveView(generics.RetrieveAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Ordering'])
class OrderingUpdateView(generics.UpdateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Ordering'])
class OrderingCreateView(generics.CreateAPIView):
    queryset = Ordering.objects.all()
    serializer_class = CreateOrderingSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Ordering'])
class OrderingListView(generics.ListAPIView):
    queryset = Ordering.objects.all()
    serializer_class = OrderingSerializer


@extend_schema(tags=['Message'])
class MessageRetrieveView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Message'])
class MessageUpdateView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Message'])
class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Message'])
class MessageListView(generics.ListAPIView):
    serializer_class = MessageSerializer

    def get_queryset(self):
        queryset = Message.objects.all()
        params = self.request.query_params

        executor = params.get('executor', None)
        customer = params.get('customer', None)
        from_date = params.get('from_date', None)
        to_date = params.get('to_date', None)

        if executor:
            queryset = queryset.filter(executor__id=executor)

        if customer:
            queryset = queryset.filter(customer__id=customer)

        if from_date:
            queryset = queryset.filter(msg__gte=from_date)

        if to_date:
            queryset = queryset.filter(msg__lte=to_date)

        return queryset


@extend_schema(tags=['Ticket'])
class TicketRetrieveView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Ticket'])
class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Ticket'])
class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = CreateTicketSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Ticket'])
class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


@extend_schema(tags=['Review'])
class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Review'])
class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Review'])
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Review'])
class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@extend_schema(tags=['Authoring'])
class AuthoringRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Authoring'])
class AuthoringUpdateView(generics.UpdateAPIView):
    queryset = Authoring.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Authoring'])
class AuthoringCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = CreateAuthoringSerializer
    permission_class = permissions.IsAuthenticatedOrReadOnly


@extend_schema(tags=['Authoring'])
class AuthoringListView(generics.ListAPIView):
    queryset = Authoring.objects.all()
    serializer_class = AuthoringSerializer