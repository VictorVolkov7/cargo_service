import os

from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    """
    Custom command to fill cars from .json file.
    """
    help = "Fills cars from .json file."
    fixture_dir = 'fixtures'
    loaddata_command = 'loaddata'
    filename = 'cars'

    def handle(self, *args, **options):
        call_command(
            self.loaddata_command, os.path.join(self.fixture_dir, f'{self.filename}.json')
        )
