from celery import shared_task

from locations.models import Location
from transportation.models import Transport


@shared_task
def transport_update_locations():
    """
    Updates the transport locations table in the database.
    :return:
    """
    cars = Transport.objects.all()

    for car in cars:
        car.location = Location.objects.order_by('?').first()
        car.save()
