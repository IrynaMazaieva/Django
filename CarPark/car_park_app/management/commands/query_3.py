from django.core.management.base import BaseCommand
from car_park_app.models import Repair
from django.utils.timezone import now


class Command(BaseCommand):
    help = 'Display a list of drivers whose cars are currently being repaired'

    def handle(self, *args, **options):

        drivers = Repair.objects.filter(date_out__gte=now()).select_related('driver')
        for i in drivers:
            print(i)
