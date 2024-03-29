import django_filters

from cargo.models import Cargo


class CargoWeightFilter(django_filters.FilterSet):
    """
    Custom Filter for searching Cargo objects based on their weight.
    """
    country = django_filters.RangeFilter(field_name="weight")

    class Meta:
        model = Cargo
        fields = ('weight',)


class NearestCarsFilter(django_filters.FilterSet):
    """
    Custom Filter for searching nearest cars to the load.
    """
    pass
