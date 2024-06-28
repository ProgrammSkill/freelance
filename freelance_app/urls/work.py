from django.urls import include, path
from rest_framework import routers
from ..views.work import ServiceView


router = routers.DefaultRouter()
router.register('service', ServiceView, 'service'),

urlpatterns = [
    path('', include(router.urls)),
]