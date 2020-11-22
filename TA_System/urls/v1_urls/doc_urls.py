from django.urls import path, re_path

from _helpers.docs import v1_schema_view

urlpatterns = [
    re_path(r'swagger(?P<format>\.json|\.yaml)$', v1_schema_view.without_ui(cache_timeout=0), name='v1-schema-json'),
    path('swagger/', v1_schema_view.with_ui('swagger', cache_timeout=0), name='v1-schema-swagger-ui'),
    path('redoc/', v1_schema_view.with_ui('redoc', cache_timeout=0), name='v1-schema-redoc-ui'),
]
