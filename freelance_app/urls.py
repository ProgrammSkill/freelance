from django.urls import path, include
from .views import *

urlpatterns = [
    path('executors/<int:pk>', ExecutorRetrieveView.as_view(), name='executor'),
    path('executors/update/<int:pk>', ExecutorUpdateView.as_view(), name='executor_update'),
    path('executors/all', ExecutorListView.as_view(), name='executors_all'),
    path('executor/new', ExecutorCreateView.as_view(), name='executor_new'),

    path('customers/<int:pk>', ExecutorRetrieveView.as_view(), name='customer'),
    path('customers/update/<int:pk>', ExecutorUpdateView.as_view(), name='customer_update'),
    path('customers/all', ExecutorListView.as_view(), name='customers_all'),
    path('customer/new', ExecutorCreateView.as_view(), name='customer_new'),

    path('services/<int:pk>', ServiceRetrieveView.as_view(), name='service'),
    path('services/update/<int:pk>', ServiceUpdateView.as_view(), name='service_update'),
    path('services/all', ServiceListView.as_view(), name='customers_all'),
    path('service/new', ServiceCreateView.as_view(), name='servicer_new'),

    path('orders/<int:pk>', OrderRetrieveView.as_view(), name='order'),
    path('orders/update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('orders/all', OrderListView.as_view(), name='orders_all'),
    path('order/new', OrderCreateView.as_view(), name='order_new'),

    path('tags/<int:pk>', TagRetrieveView.as_view(), name='tag'),
    path('tags/update/<int:pk>', TagUpdateView.as_view(), name='tag_update'),
    path('tags/all', TagListView.as_view(), name='tags_all'),
    path('tag/new', TagCreateView.as_view(), name='tag_new'),

    path('orderings/<int:pk>', OrderingRetrieveView.as_view(), name='ordering'),
    path('orderings/update/<int:pk>', OrderingUpdateView.as_view(), name='ordering_update'),
    path('orderings/all', OrderingListView.as_view(), name='orderings_all'),
    path('ordering/new', OrderingCreateView.as_view(), name='ordering_new'),

    path('messages/<int:pk>', MessageRetrieveView.as_view(), name='message'),
    path('messages/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('messages/all', MessageListView.as_view(), name='messages_all'),
    path('message/new', MessageCreateView.as_view(), name='message_new'),

    path('tickets/<int:pk>', TicketRetrieveView.as_view(), name='message'),
    path('tickets/update/<int:pk>', TicketUpdateView.as_view(), name='message_update'),
    path('tickets/all', TicketListView.as_view(), name='tickets_all'),
    path('ticket/new', TicketCreateView.as_view(), name='message_new'),

    path('reviews/<int:pk>', ReviewRetrieveView.as_view(), name='review'),
    path('reviews/update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
    path('reviews/all', ReviewListView.as_view(), name='reviews_all'),
    path('review/new', ReviewCreateView.as_view(), name='review_new'),

    path('authoring/<int:pk>', AuthoringRetrieveView.as_view(), name='authoring'),
    path('authoring/update/<int:pk>', AuthoringUpdateView.as_view(), name='authoring_update'),
    path('authoring/all', AuthoringListView.as_view(), name='authoring_all'),
    path('authoring/new', AuthoringCreateView.as_view(), name='authoring_new'),
]
