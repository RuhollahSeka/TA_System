from django.contrib import admin
from django.urls import path, include

from TA_System.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('TA_System.urls.v1_urls.api_urls')),
    path('docs/v1/', include('TA_System.urls.v1_urls.doc_urls')),
    # dashboard
    path('', index)
]
