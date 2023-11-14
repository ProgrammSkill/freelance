from django.urls import path, include
from .views import *

urlpatterns = [
    path('tickets/all', TicketListView.as_view(), name='tickets_all'),
]