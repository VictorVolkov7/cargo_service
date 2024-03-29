from rest_framework import serializers

from cargo.models import Cargo
from cargo.services import distance_between
from locations.serializers import LocationSerializer
from transportation.models import Transport


class CargoCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating Cargo objects.
    """

    class Meta:
        model = Cargo
        fields = ('pk', 'pick_up', 'delivery', 'weight', 'description',)


class CargoListSerializer(serializers.ModelSerializer):
    """
    Serializer to view a list of Cargo objects.
    With calculated a nearby cars.
    """
    pick_up = LocationSerializer(read_only=True, required=False)
    delivery = LocationSerializer(read_only=True, required=False)
    nearest_cars = serializers.SerializerMethodField()

    @staticmethod
    def get_nearest_cars(cargo) -> int:
        """
        :return: the number of nearby cars.
        """
        cars = Transport.objects.all()
        pick_up_coordinates: tuple = (cargo.pick_up.lat, cargo.pick_up.lng)

        nearest_cars_count: int = 0
        for car in cars:
            car_location: tuple = (car.location.lat, car.location.lng)
            # calling a function to calculate the distance
            distance: float = distance_between(pick_up_coordinates, car_location)
            if distance <= 450:
                nearest_cars_count += 1

        return nearest_cars_count

    class Meta:
        model = Cargo
        fields = ('pk', 'pick_up', 'delivery', 'nearest_cars',)


class CargoDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for getting Cargo details by id.
    """
    pick_up = LocationSerializer(read_only=True, required=False)
    delivery = LocationSerializer(read_only=True, required=False)
    cars_list = serializers.SerializerMethodField()

    @staticmethod
    def get_cars_list(cargo) -> list:
        """
        :return: the list of the cars with distance.
        """
        cars = Transport.objects.all()
        pick_up_coordinates: tuple = (cargo.pick_up.lat, cargo.pick_up.lng)

        cars_list = []
        for car in cars:
            car_location: tuple = (car.location.lat, car.location.lng)
            # calling a function to calculate the distance
            distance: float = distance_between(pick_up_coordinates, car_location)
            cars_list.append(f'{car.number}: {distance} M')

        return cars_list

    class Meta:
        model = Cargo
        fields = ('pk', 'pick_up', 'delivery', 'weight', 'description', 'cars_list',)


class CargoUpdateSerializer(serializers.ModelSerializer):
    """
    Serializer for updating cargo details by id.
    """

    class Meta:
        model = Cargo
        fields = ('weight', 'description',)
        read_only_fields = ('pick_up', 'delivery',)
