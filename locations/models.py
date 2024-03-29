from django.db import models
from django.utils.translation import gettext_lazy as _


class Location(models.Model):
    """
    Location Model.
    """
    city = models.CharField(
        max_length=50,
        verbose_name=_('City')
    )
    state_name = models.CharField(
        max_length=70,
        verbose_name=_('State Name')
    )
    zip = models.CharField(
        max_length=6,
        unique=True,
        verbose_name=_('Zip Code')
    )
    lat = models.DecimalField(
        max_digits=7,
        decimal_places=5,
        verbose_name=_('Latitude')
    )
    lng = models.DecimalField(
        max_digits=8,
        decimal_places=5,
        verbose_name=_('Longitude')
    )

    def __str__(self):
        return f'{self.zip} - {self.city} {self.state_name}'

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
