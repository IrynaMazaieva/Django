import pytest
from model_bakery import baker
from car_park_app import models


pytestmark = pytest.mark.django_db


def test_fuel():
    fuel = baker.make(models.Fuel)
    assert str(fuel)

def test_dimensions():
    dimensions = baker.make(models.Dimensions)
    assert str(dimensions)

def test_car_type():
    car_type = baker.make(models.CarType)
    assert str(car_type)

def test_car():
    car = baker.make(models.Car)
    assert str(car)

def test_driver():
    driver = baker.make(models.Driver)
    assert str(driver)

def test_manager():
    manager = baker.make(models.Manager)
    assert str(manager)

def test_repair():
    repair = baker.make(models.Repair)
    assert str(repair)

def test_refuel():
    refuel = baker.make(models.Refuel)
    assert str(refuel)

def test_order():
    order = baker.make(models.Order)
    assert str(order)
