from django.urls import include, path
from freelance_app.views.account import AuthView, AccountCreateAPIView, CheckEmailView, \
    RefreshView, AccountDetailAPIView, ChangePasswordView, MyAvatarViewSet

urlpatterns = [
    path('auth/', AuthView.as_view(), name='auth'),
    path('create/', AccountCreateAPIView.as_view(), name='account-create'),
    path('check-email/', CheckEmailView.as_view(), name='check-email'),
    path('refresh-token/', RefreshView.as_view(), name='refresh-token'),
    # Профиль пользователя
    path('me/', AccountDetailAPIView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('avatar/', MyAvatarViewSet.as_view()),
]
