from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView
from freelance.settings import SPECTACULAR_ACCOUNT_SETTINGS, SPECTACULAR_WORK_SETTINGS
from freelance_app.swagger_content import SpectacularSwaggerView


urlpatterns = [
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'),
    path('schema-account/', SpectacularAPIView.as_view(custom_settings=SPECTACULAR_ACCOUNT_SETTINGS),
         name='schema_account'),
    path('account/', include('freelance_app.urls.account')),
    path('schema-work/', SpectacularAPIView.as_view(custom_settings=SPECTACULAR_WORK_SETTINGS),
         name='schema_work'),
    path('work/', include('freelance_app.urls.work')),
]