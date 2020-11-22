from drf_yasg import openapi
from drf_yasg.views import get_schema_view

v1_schema_view = get_schema_view(
    openapi.Info(
        title='TA System V1 APIs',
        default_version='v1',
    ),
    urlconf='TA_System.urls.v1_urls.api_urls',
    public=True,
)
