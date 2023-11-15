from rest_framework.response import Response
from rest_framework import generics
from .models import *
from .serializers import *


class ExecutorRetrieveView(generics.RetrieveAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class ExecutorUpdateView(generics.UpdateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


class ExecutorCreateView(generics.CreateAPIView):
    queryset = Executor.objects.all()
    serializer_class = CreateExecutorSerializer


class ExecutorListView(generics.ListAPIView):
    queryset = Executor.objects.all()
    serializer_class = ExecutorSerializer


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer