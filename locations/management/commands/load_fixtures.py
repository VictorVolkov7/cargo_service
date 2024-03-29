import tablib
from import_export import resources

from django.core.management import BaseCommand

from locations.models import Location


class Command(BaseCommand):
    """
    Load fixtures from csv file
    """
    help = 'Loads data from fixtures dir'
    fixtures_dir = './fixtures/'
    filename = 'uszips.csv'

    def handle(self, *args, **options):
        location_resource = resources.modelresource_factory(model=Location)()
        dataset = tablib.Dataset().load(open(self.fixtures_dir + self.filename).read(), format='csv', headers=True)
        result = location_resource.import_data(dataset, dry_run=True)
        print(result.has_errors())
        result = location_resource.import_data(dataset, dry_run=False)


