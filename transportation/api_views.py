from rest_framework import generics

from transportation.models import Transport
from transportation.serializers import TransportUpdateSerializer


class TransportUpdateAPIView(generics.UpdateAPIView):
    """
    API endpoint for updating transport details.
    """
    queryset = Transport.objects.all()
    serializer_class = TransportUpdateSerializer
