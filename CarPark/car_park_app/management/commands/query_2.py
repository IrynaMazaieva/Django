from django.core.management.base import BaseCommand, CommandError
from car_park_app.models import Driver, Car, Fuel, Refuel


class Command(BaseCommand):
    help = 'Display information on all refueling of a specific \
        driver for the last 30 days (type of fuel, amount of fuel, price)'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        name = options['username']

        try:
            driver_obj = Driver.objects.filter(driver__username=name)
            driver_obj.get()
        except Driver.DoesNotExist:
            raise CommandError("No such driver!!!")

        car = Car.objects.filter(driver=driver_obj.first()).first()
        fuel = Fuel.objects.filter(car=car).first()
        refuel = Refuel.objects.filter(car=car)

        print(fuel)
        for r in refuel:
            print(r)
