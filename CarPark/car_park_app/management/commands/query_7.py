from django.core.management.base import BaseCommand
from car_park_app.models import Repair, CarType
from django.utils.timezone import datetime


class Command(BaseCommand):
    help = 'Display a list of machines that can fulfill an order for the\
         carriage of cargo weighing 400 kg and dimensions 3x2x1m for a given\
              number in the near future sorted by carrying capacity'

    def add_arguments(self, parser):
        parser.add_argument('weight', type=float)
        parser.add_argument('length', type=float)
        parser.add_argument('width', type=float)
        parser.add_argument('height', type=float)
        parser.add_argument('day', type=int)
        parser.add_argument('month', type=int)
        parser.add_argument('year', type=int)

    def handle(self, *args, **options):
        dims = sorted([options['length'], options['width'], options['height']])
        weigth = options['weight']
        date = datetime(day=options['day'], month=options['month'], year=options['year'])

        cars_not_on_repair = Repair.objects.filter(date_out__gte=date).select_related('driver')
        cars_not_on_repair_list = [i.driver for i in cars_not_on_repair]
        car_types = CarType.objects.exclude(carrying_capacity__lte=weigth).select_related('dimensions')
        car_list = []

        for model in car_types:
            model_dims = sorted([model.dimensions.length, model.dimensions.width, model.dimensions.height])

            for i in range(len(model_dims)):
                if model_dims[i] < dims[i]:
                    break
                elif i == len(model_dims) - 1:
                    for driver in cars_not_on_repair_list:
                        if driver.car.car_type != model and (model not in car_list):
                            car_list.append(model)
        print(car_list)
