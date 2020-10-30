from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Fuel(models.Model):
    fuel_type = models.CharField(max_length=30)

    def __str__(self):
        return self.fuel_type


class Dimensions(models.Model):
    height = models.FloatField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)

    def __str__(self):
        return '{}*{}*{}'.format(
            self.height,
            self.length,
            self.width
        )


class CarType(models.Model):
    BODY_TYPE = [
        ('C', 'Passenger car'),
        ('B', 'Bus'),
        ('T', 'Truck'),
    ]

    body_type = models.CharField(max_length=1, choices=BODY_TYPE, default='C')
    name = models.CharField(max_length=30)
    carrying_capacity = models.IntegerField(default=0)
    dimensions = models.ForeignKey(Dimensions, on_delete=models.CASCADE)

    def __str__(self):
        return 'Name - {}, body type - {}, carrying capacity - {}, dimensions - {}'.format(
            self.name,
            self.body_type,
            self.carrying_capacity,
            self.dimensions,
        )


class Car(models.Model):
    car_type = models.ForeignKey(CarType, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10)
    millage = models.FloatField(default=0)
    fuel_type = models.ManyToManyField(Fuel)
    fuel_consumption = models.FloatField(default=0)

    def __str__(self):
        return '{}, {}, milleage - {}, consumption - {}'.format(
            self.car_type,
            self.license_plate,
            self.millage,
            self.fuel_consumption,
        )


class Driver(models.Model):
    car = models.OneToOneField(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='driver')

    def __str__(self):
        return str(self.driver)


class Manager(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.manager)


class Repair(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='repair', null=True, blank=False)
    problem = models.TextField(verbose_name="Malfunction in ...")
    date_in = models.DateField(verbose_name='Repair date')
    date_out = models.DateField(verbose_name='Repair completion date')
    cost = models.FloatField(default=0)

    def __str__(self):
        return '{}, problem - {}, \ndate in: {}, \ndate out: {}, \ncost: {}'.format(
            self.driver,
            self.problem,
            self.date_in,
            self.date_out,
            self.cost,
        )

class Refuel(models.Model):
    car = models.ManyToManyField(Car)
    volume = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    date = models.DateField('Date of refuel', default=now)

    def __str__(self):
        return 'Volume - {}, cost - {}, date: {}'.format(
            self.volume,
            self.cost,
            self.date,
        )


class Order(models.Model):
    car = models.ManyToManyField(Car)
    driver = models.ManyToManyField(Driver)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    dimensions = models.ManyToManyField(Dimensions)
    weight = models.FloatField(default=0)
    place_from = models.TextField('Place from')
    place_to = models.TextField('Place to')
    milleage = models.FloatField('Total distance', default=0)
    time = models.DateField('Order completion date')

    def __str__(self):
        return 'Manager - {}, \nweight: {}, \nfrom: {}, to: {}, milleage - {}, date: {}'.format(
            self.manager,
            self.weight,
            self.place_from,
            self.place_to,
            self.milleage,
            self.time,
        )
