from django.urls import path

from cargo.api_views import CargoCreateAPIView, CargoListAPIView, CargoDetailAPIView, CargoUpdateAPIView, \
    CargoDeleteAPIView
from cargo.apps import CargoConfig

app_name = CargoConfig.name

urlpatterns = [
    path('cargo/create/', CargoCreateAPIView.as_view(), name='cargo-create'),
    path('cargo/', CargoListAPIView.as_view(), name='cargo-list'),
    path('cargo/<int:pk>/', CargoDetailAPIView.as_view(), name='cargo-detail'),
    path('cargo/<int:pk>/update/', CargoUpdateAPIView.as_view(), name='cargo-update'),
    path('cargo/<int:pk>/delete/', CargoDeleteAPIView.as_view(), name='cargo-delete'),
]
