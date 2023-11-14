from django.urls import path, include
from .views import *

urlpatterns = [
    path('executors/<int:pk>', ExecutorRetrieveView.as_view(), name='executor'),
    path('tickets/all', TicketListView.as_view(), name='tickets_all'),
]
