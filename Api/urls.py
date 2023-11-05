from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from Api.views import InitialApi, Home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'Api'
urlpatterns = [
    # Api docs(swagger) related urls
    path('api_schema', SpectacularAPIView.as_view(), name="api_schema"),
    path('', SpectacularSwaggerView.as_view(
        template_name='swagger-ui.html',
        url_name='Api:api_schema'), name='api-docs'),
    path('initial/', InitialApi.as_view(), name="home"),
    path('auth/get_token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('home/', Home.as_view(), name='home'),
]
