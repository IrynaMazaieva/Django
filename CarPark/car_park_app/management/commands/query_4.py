from django.core.management.base import BaseCommand, CommandError
from car_park_app.models import Car, Order, Driver
from django.db.models import Prefetch
import time


class Command(BaseCommand):
    help = 'List the drivers who drove the given car'

    def add_arguments(self, parser):
        parser.add_argument('license_plate', type=str)

    def handle(self, *args, **options):
        license_plate = options['license_plate']

        start = time.perf_counter()
        try:
            car = Car.objects.filter(license_plate=license_plate)
            car.get()
        except Car.DoesNotExist:
            raise CommandError("No such car!!!")

        orders = Order.objects.prefetch_related(Prefetch('car', queryset=car))
        present_driver = Driver.objects.filter(car=car.get()).get()

        print("\nPresent driver: ", present_driver)

        for order in orders:
            driver = orders.get().driver.get()
            if present_driver != driver:
                print(driver)

        end = time.perf_counter()
        print("\nFinished in : {}".format((end - start)))
