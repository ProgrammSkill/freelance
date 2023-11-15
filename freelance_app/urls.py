from django.urls import path, include
from .views import *

urlpatterns = [
    path('executors/<int:pk>', ExecutorRetrieveView.as_view(), name='executor'),
    path('executors/update/<int:pk>', ExecutorUpdateView.as_view(), name='executor_update'),
    path('executors/all', ExecutorListView.as_view(), name='executors_all'),
    path('executor/new', ExecutorCreateView.as_view(),name='executor_new'),
    path('tickets/all', TicketListView.as_view(), name='tickets_all'),
]
