from django.core.management.base import BaseCommand, CommandError
from car_park_app.models import Driver, Order
from django.utils.timezone import now


class Command(BaseCommand):
    help = 'List future delivery tasks for a given driver'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        name = options['username']

        try:
            driver_obj = Driver.objects.filter(driver__username=name).first()
        except Driver.DoesNotExist:
            raise CommandError("No such driver!!!")

        orders = Order.objects.filter(time__gte=now()).filter(driver=driver_obj)

        print(orders)
