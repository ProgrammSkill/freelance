from drf_spectacular.plumbing import set_query_parameters
from drf_spectacular.settings import spectacular_settings
from drf_spectacular.utils import extend_schema
from drf_spectacular.views import SpectacularSwaggerView as _SpectacularSwaggerView
from rest_framework.response import Response


SERVIES_SCHEMA_URLS = {
    'Freelance Account': '/api/freelance_app/schema-account/',
    'Freelance Work': '/api/freelance_app/schema-work/'
}


class SpectacularSwaggerView(_SpectacularSwaggerView):
    """ Класс определяет пользовательский шаблон для отображения Swagger UI.  """

    template_name = 'drf-spectacular/custom_swagger_ui.html'

    @extend_schema(exclude=True)
    def get(self, request, *args, **kwargs):
        """ Переопределённый метод для создания кастомного ответа на GET-запрос к Swagger-странице. Он возвращает
        объект Response, содержащий данные для отображения на странице Swagger UI. Возвращаемые данные включают список
        доступных сервисов, название страницы Swagger, путь к статическим файлам Swagger UI, ссылку на фавиконку,
        URL-адрес схемы API в зависимости от выбранного сервиса, настройки Swagger UI, конфигурацию OAuth2, название
        шаблона JavaScript, имя заголовка CSRF и имена аутентификации схемы.  """

        return Response(
            data={
                'services': SERVIES_SCHEMA_URLS.keys(),
                'title': 'Swagger Freelance',
                'dist': self._swagger_ui_dist(),
                'favicon_href': self._swagger_ui_favicon(),
                'schema_url': self._get_schema_url(request),
                'settings': self._dump(spectacular_settings.SWAGGER_UI_SETTINGS),
                'oauth2_config': self._dump(spectacular_settings.SWAGGER_UI_OAUTH2_CONFIG),
                'template_name_js': self.template_name_js,
                'csrf_header_name': self._get_csrf_header_name(),
                'schema_auth_names': self._dump(self._get_schema_auth_names()),
            },
            template_name=self.template_name,
        )

    def _get_schema_url(self, request):
        """ Метод формирует URL-адрес схемы API, добавляя параметры запроса lang и version к базовому URL-адресу
        сервиса. """
        host = f"{request.scheme}://{request.get_host()}"
        return set_query_parameters(
            url=f"{host}{SERVIES_SCHEMA_URLS.get(self.request.query_params.get('service', 'Freelance Account'))}",
            lang=request.GET.get('lang'),
            version=request.GET.get('version')
        )