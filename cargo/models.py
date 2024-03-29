from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from locations.models import Location


class Cargo(models.Model):
    """
    Cargo model.
    """
    pick_up = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        to_field='zip',
        related_name='pick_up',
        verbose_name=_('Location pick-up')
    )
    delivery = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        to_field='zip',
        related_name='delivery',
        verbose_name=_('Location delivery')
    )
    weight = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name=_('Weight')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Description')
    )

    def __str__(self):
        return f'{self.pick_up} to {self.delivery}: {self.weight}'

    class Meta:
        verbose_name = _('Cargo')
        verbose_name_plural = _('Cargo')
