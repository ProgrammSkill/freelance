from django.urls import include, path
from rest_framework import routers
from ..views.work import ServiceView, OrderView, TagListView, TagView

router = routers.DefaultRouter()
router.register('service', ServiceView, 'service'),
router.register('order', OrderView, 'order'),
router.register('tag', TagView, 'tag'),

urlpatterns = [
    path('', include(router.urls)),
    path('tags/', TagListView.as_view(), name='tags_all'),
]