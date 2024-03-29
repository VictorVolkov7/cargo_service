from rest_framework import serializers

from transportation.models import Transport


class TransportUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for transports updates.
    """

    class Meta(object):
        model = Transport
        fields = ('number', 'location', 'carrying_capacity',)
