from django.urls import path

from transportation.api_views import TransportUpdateAPIView
from transportation.apps import TransportationConfig

app_name = TransportationConfig.name

urlpatterns = [
    path('transport/<int:pk>/update/', TransportUpdateAPIView.as_view(), name='transport-update')
]
