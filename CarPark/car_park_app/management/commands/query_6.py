from django.core.management.base import BaseCommand, CommandError
from car_park_app.models import Manager, Order
from django.db.models import Prefetch


class Command(BaseCommand):
    help = 'List the drivers who served the orders of\
         the given manager sorted by the total mileage'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        name = options['username']

        try:
            manager = Manager.objects.filter(manager__username=name).select_related('manager')
            manager.get()
        except Manager.DoesNotExist:
            raise CommandError("No such manager!!!")

        drivers = Order.objects.prefetch_related(Prefetch('manager', queryset=manager)).order_by('milleage')

        for i in drivers:
            print(i.driver.get())
