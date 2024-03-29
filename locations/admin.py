from django.contrib import admin
from import_export import resources

from locations.models import Location


class LocationResource(resources.ModelResource):
    """
    Resource (django-import-export) for Location model
    to fill in data from a csv file.
    """

    class Meta:
        model = Location


# register location model in django admin
admin.site.register(Location)
