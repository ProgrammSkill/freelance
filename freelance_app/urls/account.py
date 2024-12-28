from django.urls import include, path
from freelance_app.views.account import AuthView, AccountCreateAPIView, CheckEmailView, \
    RefreshView, AccountDetailAPIView, ChangePasswordView, MyAvatarViewSet

urlpatterns = [
    path('auth/', AuthView.as_view()),
    path('create/', AccountCreateAPIView.as_view()),
    path('check-email/', CheckEmailView.as_view()),
    path('refresh-token/', RefreshView.as_view()),
    # Профиль пользователя
    path('me/', AccountDetailAPIView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('avatar/', MyAvatarViewSet.as_view()),
]
