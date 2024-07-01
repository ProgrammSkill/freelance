from django.urls import include, path
from rest_framework import routers
from ..views.work import ServiceView, OrderView

router = routers.DefaultRouter()
router.register('service', ServiceView, 'service'),
router.register('order', OrderView, 'order'),

urlpatterns = [
    path('', include(router.urls)),
]