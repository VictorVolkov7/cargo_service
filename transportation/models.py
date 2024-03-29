from random import randint, choice
from string import ascii_uppercase

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from locations.models import Location


class Transport(models.Model):
    """
    Transport model.
    """
    number = models.CharField(
        max_length=5,
        unique=True,
        null=True,
        blank=True,
        verbose_name=_('Car number')
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        to_field='zip',
        verbose_name=_('Location'),
    )
    carrying_capacity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(1000)],
        verbose_name=_('Carrying capacity')
    )

    def __str__(self):
        return f'{self.number} - {self.carrying_capacity} kg'

    class Meta:
        verbose_name = _('Transport')
        verbose_name_plural = _('Transports')


@receiver(pre_save, sender=Transport)
def generate_random_number(sender, instance, **kwargs):
    """
    Signal for generate random car number (format "1234A") before saving.
    If number already exists, will be generated new.
    """
    if not instance.number:
        unique_number_generated = False
        while not unique_number_generated:
            random_number = str(randint(1000, 9999)) + choice(list(ascii_uppercase))
            if not Transport.objects.filter(number=random_number).exists():
                instance.number = random_number
                unique_number_generated = True


@receiver(pre_save, sender=Transport)
def generate_random_location(sender, instance, **kwargs):
    """
    Signal for generate random car location before saving.
    The list of location objects is shuffled and selected first.
    """
    if not instance.location:
        instance.location = Location.objects.order_by('?').first()
