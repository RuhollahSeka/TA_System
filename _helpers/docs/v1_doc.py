from django.conf.urls import url
from django.urls import include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from TA_System.urls.v1_urls.api_urls import urlpatterns as api_v1

v1_schema_view = get_schema_view(
    openapi.Info(
        title='TA System V1 APIs',
        default_version='v1',
    ),
    patterns=[
        url('api/v1/', include(api_v1)),
    ],
    public=True,
)
