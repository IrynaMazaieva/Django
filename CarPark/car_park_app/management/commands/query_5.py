from django.core.management.base import BaseCommand, CommandError
from car_park_app.models import Driver, Order
import time


class Command(BaseCommand):
    help = 'Display a list of managers who assigned orders to a given driver'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        name = options['username']

        start = time.perf_counter()

        try:
            driver = Driver.objects.filter(driver__username=name)
            driver.get()
        except Driver.DoesNotExist:
            raise CommandError("No such driver!")

        # managers = Order.objects.prefetch_related(Prefetch('driver', queryset=driver)).select_related('manager')

        managers = Order.objects.filter(driver=driver.get()).select_related('manager')  # this variant is faster

        for i in managers:
            print(i.manager)

        end = time.perf_counter()
        print("\nFinished in : {}".format((end - start)))
