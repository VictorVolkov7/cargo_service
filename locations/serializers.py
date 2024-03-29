from rest_framework import serializers

from locations.models import Location


class LocationSerializer(serializers.ModelSerializer):
    """
    Serializer for location model.
    """

    class Meta:
        model = Location
        fields = ('city', 'state_name', 'zip', 'lat', 'lng',)
