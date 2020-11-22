from django.urls import path, include

urlpatterns = [
    path('subjects/', include('subjects.urls')),
    path('procedures/', include('ta_procedures.urls'))
]
