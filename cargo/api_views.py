from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import generics

from cargo.filters import CargoWeightFilter
from cargo.models import Cargo
from cargo.serializers import CargoCreateSerializer, CargoListSerializer, CargoDetailSerializer, CargoUpdateSerializer


@extend_schema(
    summary="API endpoint for cargo creation."
)
class CargoCreateAPIView(generics.CreateAPIView):
    """
    API endpoint for cargo creation.
    """
    serializer_class = CargoCreateSerializer


@extend_schema(
    summary="API endpoint to view a list of Cargo with count of the nearest cars."
)
class CargoListAPIView(generics.ListAPIView):
    """
    API endpoint to view a list of Cargo.
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CargoWeightFilter


@extend_schema(
    summary="API endpoint for viewing cargo details with all vehicles with distance to the cargo."
)
class CargoDetailAPIView(generics.RetrieveAPIView):
    """
    API endpoint to view a cargo detail.
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoDetailSerializer


@extend_schema(
    summary="API endpoint for updating a cargo."
)
class CargoUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating a cargo.
    """
    queryset = Cargo.objects.all()
    serializer_class = CargoUpdateSerializer


@extend_schema(
    summary="API endpoint for deleting a cargo."
)
class CargoDeleteAPIView(generics.DestroyAPIView):
    """
    API endpoint for deleting a cargo.
    """
    queryset = Cargo.objects.all()
