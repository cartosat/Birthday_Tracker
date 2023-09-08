from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from Api.views import InitialApi

app_name = 'Api'
urlpatterns = [
    # Api docs(swagger) related urls
    path('api_schema', SpectacularAPIView.as_view(), name="api_schema"),
    path('', SpectacularSwaggerView.as_view(
        template_name='swagger-ui.html',
        url_name='Api:api_schema'), name='api-docs'),
    path('greet/', InitialApi.as_view(), name="home"),
]
