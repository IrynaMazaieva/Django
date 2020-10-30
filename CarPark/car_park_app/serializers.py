from rest_framework import serializers
from django.contrib.auth.models import User
from .models import (
    Fuel,
    Dimensions,
    Manager,
    Car,
    CarType,
    Driver,
    Repair,
    Refuel,
    Order
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ['fuel_type']


class DimensionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dimensions
        fields = ['height', 'length', 'width']


class CarTypeSerializer(serializers.ModelSerializer):
    dimensions = DimensionsSerializer(read_only=True)

    class Meta:
        model = CarType
        fields = ['id', 'name', 'body_type', 'carrying_capacity', 'dimensions']


class CarTypeCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarType
        fields = ['id', 'name', 'body_type', 'carrying_capacity', 'dimensions']



class CarListSerializer(serializers.ModelSerializer):
    fuel_type = FuelSerializer(many=True)
    car_type = CarTypeSerializer()

    class Meta:
        model = Car
        fields = ['license_plate', 'millage', 'fuel_consumption', 'car_type', 'fuel_type']


class CarCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'license_plate', 'millage', 'fuel_consumption', 'car_type', 'fuel_type']


class DriverSerializer(serializers.ModelSerializer):
    driver = UserSerializer(read_only=True)
    car = CarListSerializer(read_only=True)

    class Meta:
        model = Driver
        fields = ['driver', 'car']


class DriverCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = ['driver', 'car']


class ManagerSerializer(serializers.ModelSerializer):
    manager = UserSerializer(read_only=True)

    class Meta:
        model = Manager
        fields = ['manager']


class ManagerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manager
        fields = ['manager']


class RepairSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True)

    class Meta:
        model = Repair
        fields = ['driver', 'problem', 'date_in', 'date_out', 'cost']


class RepairCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repair
        fields = ['driver', 'problem', 'date_in', 'date_out', 'cost']



class RefuelSerializer(serializers.ModelSerializer):
    car = CarListSerializer(many=True, read_only=True)

    class Meta:
        model = Refuel
        fields = ['volume', 'cost', 'car']


class RefuelCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Refuel
        fields = ['volume', 'cost', 'car']


class OrderSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True)
    driver = DriverSerializer(many=True, read_only=True)
    dimensions = DimensionsSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['time', 'milleage', 'place_from', 'place_to', 'manager', 'driver', 'dimensions']


class OrderCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['time', 'milleage', 'place_from', 'place_to', 'manager', 'driver', 'dimensions']



class Query_driver_Serializer(serializers.ModelSerializer):
    driver = DriverSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ['driver']


class Query_manager_Serializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True)

    class Meta:
        model = Order
        fields = ['manager']


class Query_7_Serializer(serializers.Serializer):
    child = CarType()
    name = serializers.CharField()
    body_type = serializers.CharField()
    dimensions = DimensionsSerializer()
    carrying_capacity = serializers.FloatField()
