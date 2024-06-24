from django.conf import settings
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken as _RefreshToken
from rest_framework_simplejwt.utils import datetime_from_epoch
from freelance_app.common_utils import get_client_ip
from freelance_app.models.user import UserOutstandingToken


""" Этот код отвечает за генерацию токенов для аутентификации пользователей в приложении. Он использует \
библиотеку rest_framework_simplejwt для работы с токенами JWT и модель UserOutstandingToken для хранения \
информации о выпущенных токенах. """

class RefreshToken(_RefreshToken):
    @classmethod
    def for_user(cls, user, request=None):
        """ Этот метод устанавливает идентификатор пользователя в токене и сохраняет информацию о токене в базе данных,
        включая IP-адрес, пользовательский агент и идентификатор устройства, если они доступны в запросе. Это позволяет
         отслеживать активные токены пользователя. """
        user_id = getattr(user, api_settings.USER_ID_FIELD)
        if not isinstance(user_id, int):
            user_id = str(user_id)

        token = cls()
        token[api_settings.USER_ID_CLAIM] = user_id

        device_id = 0
        user_ip = None
        user_agent = None
        if request:
            # Получение информации о запросе: IP-адрес, пользовательский агент и идентификатор устройства
            device_id = int(request.META.get('HTTP_X_DEVICE_ID', 0))
            user_ip = get_client_ip(request)
            user_agent = request.META['HTTP_USER_AGENT']

        UserOutstandingToken.objects.create(
            user=user,
            jti=token[api_settings.JTI_CLAIM],
            token=str(token),
            created_at=token.current_time,
            expires_at=datetime_from_epoch(token['exp']),
            device_id=device_id,
            ip_address=user_ip,
            mac_address=None,
            user_agent=user_agent,
        )
        return token


class ClientRefreshToken(RefreshToken):
    """ Класс определяет параметры для подписи и проверки токена, такие как алгоритм подписи, ключ подписи, URL для
    получения открытого ключа (JWK_URL) и другие параметры, необходимые для работы с токенами аутентификации клиента. """

    _token_backend = TokenBackend(
        api_settings.ALGORITHM,
        settings.CLIENT_SIGNING_KEY,  # api_settings.SIGNING_KEY,
        api_settings.VERIFYING_KEY,
        api_settings.AUDIENCE,
        api_settings.ISSUER,
        api_settings.JWK_URL,
        api_settings.LEEWAY,
        api_settings.JSON_ENCODER,
    )


def get_token_class(request):
    """ Функция используется для определения класса токена в зависимости от типа аутентификации (обычная или на стороне
    клиента). """
    try:
        JWTAuthentication().authenticate(request)
        return ClientRefreshToken
    except InvalidToken:
        return RefreshToken

def get_token(request, user):
    """ Функция используется для получения токена для конкретного пользователя и запроса (регистрация и авторизация). """
    return get_token_class(request).for_user(user, request)

