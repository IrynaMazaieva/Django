import pytest
from model_bakery import baker, recipe
from car_park_app import views, models, serializers
from unittest.mock import MagicMock
import requests
from django.urls import reverse
from django.contrib.auth.models import User, Group
from CarPark import settings

pytestmark = pytest.mark.django_db

@pytest.fixture
def user_client(api_client):
    user = baker.make(User)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def manager_client(api_client):
    user = baker.make(User)
    group, _ = Group.objects.get_or_create(name=settings.MANAGER_GROUP)
    user.groups.add(group)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def driver_client(api_client):
    user = baker.make(User)
    group, _ = Group.objects.get_or_create(name=settings.DRIVER_GROUP)
    user.groups.add(group)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def boss_client(api_client):
    user = baker.make(User)
    group, _ = Group.objects.get_or_create(name=settings.BOSS_GROUP)
    user.groups.add(group)
    api_client.force_login(user)
    return api_client

@pytest.fixture
def car_url():
    return reverse('car-list')

@pytest.fixture
def car_type_url():
    return reverse('car_type-list')

@pytest.fixture
def fuel_url():
    return reverse('fuel-list')

@pytest.fixture
def driver_url():
    return reverse('driver-list')

@pytest.fixture
def manager_url():
    return reverse('manager-list')

@pytest.fixture
def dimensions_url():
    return reverse('dimensions-list')

@pytest.fixture
def repair_url():
    return reverse('repair-list')

@pytest.fixture
def refuel_url():
    return reverse('refuel-list')

@pytest.fixture
def user_url():
    return reverse('user-list')

@pytest.fixture
def order_url():
    return reverse('order-list')


# GET

def test_car_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, car_url, api_client):
    assert user_client.get(car_url).status_code == 200
    assert manager_client.get(car_url).status_code == 200
    assert driver_client.get(car_url).status_code == 200
    assert boss_client.get(car_url).status_code == 200
    assert admin_client.get(car_url).status_code == 200
    assert api_client.get(car_url).status_code == 200

def test_car_type_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, car_type_url, api_client):
    assert user_client.get(car_type_url).status_code == 200
    assert manager_client.get(car_type_url).status_code == 200
    assert driver_client.get(car_type_url).status_code == 200
    assert boss_client.get(car_type_url).status_code == 200
    assert admin_client.get(car_type_url).status_code == 200
    assert api_client.get(car_type_url).status_code == 200

def test_fuel_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, fuel_url, api_client):
    assert user_client.get(fuel_url).status_code == 200
    assert manager_client.get(fuel_url).status_code == 200
    assert driver_client.get(fuel_url).status_code == 200
    assert boss_client.get(fuel_url).status_code == 200
    assert admin_client.get(fuel_url).status_code == 200
    assert api_client.get(fuel_url).status_code == 200

def test_driver_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, driver_url, api_client):
    assert user_client.get(driver_url).status_code == 200
    assert manager_client.get(driver_url).status_code == 200
    assert driver_client.get(driver_url).status_code == 200
    assert boss_client.get(driver_url).status_code == 200
    assert admin_client.get(driver_url).status_code == 200
    assert api_client.get(driver_url).status_code == 200

def test_manager_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, manager_url, api_client):
    assert user_client.get(manager_url).status_code == 200
    assert manager_client.get(manager_url).status_code == 200
    assert driver_client.get(manager_url).status_code == 200
    assert boss_client.get(manager_url).status_code == 200
    assert admin_client.get(manager_url).status_code == 200
    assert api_client.get(manager_url).status_code == 200

def test_dimensions_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, dimensions_url, api_client):
    assert user_client.get(dimensions_url).status_code == 200
    assert manager_client.get(dimensions_url).status_code == 200
    assert driver_client.get(dimensions_url).status_code == 200
    assert boss_client.get(dimensions_url).status_code == 200
    assert admin_client.get(dimensions_url).status_code == 200
    assert api_client.get(dimensions_url).status_code == 200

def test_repair_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, repair_url, api_client):
    assert user_client.get(repair_url).status_code == 200
    assert manager_client.get(repair_url).status_code == 200
    assert driver_client.get(repair_url).status_code == 200
    assert boss_client.get(repair_url).status_code == 200
    assert admin_client.get(repair_url).status_code == 200
    assert api_client.get(repair_url).status_code == 200

def test_refuel_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, refuel_url, api_client):
    assert user_client.get(refuel_url).status_code == 200
    assert manager_client.get(refuel_url).status_code == 200
    assert driver_client.get(refuel_url).status_code == 200
    assert boss_client.get(refuel_url).status_code == 200
    assert admin_client.get(refuel_url).status_code == 200
    assert api_client.get(refuel_url).status_code == 200

def test_user_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, user_url, api_client):
    assert user_client.get(user_url).status_code == 200
    assert manager_client.get(user_url).status_code == 200
    assert driver_client.get(user_url).status_code == 200
    assert boss_client.get(user_url).status_code == 200
    assert admin_client.get(user_url).status_code == 200
    assert api_client.get(user_url).status_code == 200

def test_order_api_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, order_url, api_client):
    assert user_client.get(order_url).status_code == 200
    assert manager_client.get(order_url).status_code == 200
    assert driver_client.get(order_url).status_code == 200
    assert boss_client.get(order_url).status_code == 200
    assert admin_client.get(order_url).status_code == 200
    assert api_client.get(order_url).status_code == 200


#  POST


def test_car_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, car_url, api_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = {
        "license_plate": "BIGLACET",
        "millage": 234.0,
        "fuel_consumption": 5.5,
        "car_type": car_type.id,
        "fuel_type": [fuel_type.id],
    }
    assert user_client.post(car_url, car).status_code == 403
    assert manager_client.post(car_url, car).status_code == 403
    assert driver_client.post(car_url, car).status_code == 403
    assert boss_client.post(car_url, car).status_code == 403
    assert admin_client.post(car_url, car).status_code == 201
    assert api_client.post(car_url, car).status_code == 403

def test_car_type_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, car_type_url, api_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    car_type = serializers.CarTypeCreateSerializer(car_type).data
    assert user_client.post(car_type_url, car_type).status_code == 403
    assert manager_client.post(car_type_url, car_type).status_code == 403
    assert driver_client.post(car_type_url, car_type).status_code == 403
    assert boss_client.post(car_type_url, car_type).status_code == 403
    assert admin_client.post(car_type_url, car_type).status_code == 201
    assert api_client.post(car_type_url, car_type).status_code == 403

def test_driver_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, driver_url, api_client):
    user = baker.make(models.User)
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    driver = {
        'driver': user.id,
        'car': car.id,
    }
    assert user_client.post(driver_url, driver).status_code == 403
    assert manager_client.post(driver_url, driver).status_code == 403
    assert driver_client.post(driver_url, driver).status_code == 403
    assert boss_client.post(driver_url, driver).status_code == 403
    assert admin_client.post(driver_url, driver).status_code == 201
    assert api_client.post(driver_url, driver).status_code == 403

def test_fuel_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, fuel_url, api_client):
    fuel_type = baker.make(models.Fuel)
    fuel_type = serializers.FuelSerializer(fuel_type).data
    assert user_client.post(fuel_url, fuel_type).status_code == 403
    assert manager_client.post(fuel_url, fuel_type).status_code == 403
    assert driver_client.post(fuel_url, fuel_type).status_code == 403
    assert boss_client.post(fuel_url, fuel_type).status_code == 403
    assert admin_client.post(fuel_url, fuel_type).status_code == 201
    assert api_client.post(fuel_url, fuel_type).status_code == 403

def test_manager_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, manager_url, api_client):
    user = baker.make(User)
    manager = {
        'manager': user.id,
    }
    assert user_client.post(manager_url, manager).status_code == 403
    assert manager_client.post(manager_url, manager).status_code == 403
    assert driver_client.post(manager_url, manager).status_code == 403
    assert boss_client.post(manager_url, manager).status_code == 403
    assert admin_client.post(manager_url, manager).status_code == 201
    assert api_client.post(manager_url, manager).status_code == 403

def test_refuel_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, refuel_url, api_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    refuel = {
        'volume': 36,
        'cost': 756,
        'car': car.id,
    }
    assert user_client.post(refuel_url, refuel).status_code == 403
    assert manager_client.post(refuel_url, refuel).status_code == 403
    assert driver_client.post(refuel_url, refuel).status_code == 403
    assert boss_client.post(refuel_url, refuel).status_code == 403
    assert admin_client.post(refuel_url, refuel).status_code == 201
    assert api_client.post(refuel_url, refuel).status_code == 403

def test_repair_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, repair_url, api_client):
    user = baker.make(User)
    driver = baker.make(models.Driver, driver=user)
    repair = baker.make(models.Repair, driver=driver)
    repair = serializers.RepairCreateSerializer(repair).data
    assert user_client.post(repair_url, repair).status_code == 403
    assert manager_client.post(repair_url, repair).status_code == 403
    assert driver_client.post(repair_url, repair).status_code == 403
    assert boss_client.post(repair_url, repair).status_code == 403
    assert admin_client.post(repair_url, repair).status_code == 201
    assert api_client.post(repair_url, repair).status_code == 403

def test_order_post_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, order_url, api_client):
    user = baker.make(User, _quantity=2)
    driver = baker.make(models.Driver, driver=user[0])
    manager = baker.make(models.Manager, manager=user[1])
    dimensions = baker.make(models.Dimensions, _quantity=2)
    car_type = baker.make(models.CarType, dimensions=dimensions[0])
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    order = baker.make(models.Order, dimensions=[dimensions[1]], manager=manager,
                       driver=[driver], car=[car])
    order = serializers.OrderCreateSerializer(order).data
    assert user_client.post(order_url, order).status_code == 403
    assert manager_client.post(order_url, order).status_code == 403
    assert driver_client.post(order_url, order).status_code == 403
    assert boss_client.post(order_url, order).status_code == 403
    assert admin_client.post(order_url, order).status_code == 201
    assert api_client.post(order_url, order).status_code == 403

#  DELETE


def test_car_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, car_url, api_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    assert user_client.delete(car_url + str(car.id) + '/').status_code == 403
    assert manager_client.delete(car_url + str(car.id) + '/').status_code == 403
    assert driver_client.delete(car_url + str(car.id) + '/').status_code == 403
    assert boss_client.delete(car_url + str(car.id) + '/').status_code == 403
    assert admin_client.delete(car_url + str(car.id) + '/').status_code == 204
    assert api_client.delete(car_url + str(car.id) + '/').status_code == 403

def test_car_type_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, car_type_url, api_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    assert user_client.delete(car_type_url + str(car_type.id) + '/').status_code == 403
    assert manager_client.delete(car_type_url + str(car_type.id) + '/').status_code == 403
    assert driver_client.delete(car_type_url + str(car_type.id) + '/').status_code == 403
    assert boss_client.delete(car_type_url + str(car_type.id) + '/').status_code == 403
    assert admin_client.delete(car_type_url + str(car_type.id) + '/').status_code == 204
    assert api_client.delete(car_type_url + str(car_type.id) + '/').status_code == 403

def test_driver_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, driver_url, api_client):
    user = baker.make(models.User)
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    driver = baker.make(models.Driver, car=car, driver=user)
    assert user_client.delete(driver_url + str(driver.id) + '/').status_code == 403
    assert manager_client.delete(driver_url + str(driver.id) + '/').status_code == 403
    assert driver_client.delete(driver_url + str(driver.id) + '/').status_code == 403
    assert boss_client.delete(driver_url + str(driver.id) + '/').status_code == 403
    assert admin_client.delete(driver_url + str(driver.id) + '/').status_code == 204
    assert api_client.delete(driver_url + str(driver.id) + '/').status_code == 403

def test_fuel_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, fuel_url, api_client):
    fuel_type = baker.make(models.Fuel)
    assert user_client.delete(fuel_url + str(fuel_type.id) + '/').status_code == 403
    assert manager_client.delete(fuel_url + str(fuel_type.id) + '/').status_code == 403
    assert driver_client.delete(fuel_url + str(fuel_type.id) + '/').status_code == 403
    assert boss_client.delete(fuel_url + str(fuel_type.id) + '/').status_code == 403
    assert admin_client.delete(fuel_url + str(fuel_type.id) + '/').status_code == 204
    assert api_client.delete(fuel_url + str(fuel_type.id) + '/').status_code == 403

def test_dimensions_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, dimensions_url, api_client):
    dimensions = baker.make(models.Dimensions)
    assert user_client.delete(dimensions_url + str(dimensions.id) + '/').status_code == 403
    assert manager_client.delete(dimensions_url + str(dimensions.id) + '/').status_code == 403
    assert driver_client.delete(dimensions_url + str(dimensions.id) + '/').status_code == 403
    assert boss_client.delete(dimensions_url + str(dimensions.id) + '/').status_code == 403
    assert admin_client.delete(dimensions_url + str(dimensions.id) + '/').status_code == 204
    assert api_client.delete(dimensions_url + str(dimensions.id) + '/').status_code == 403

def test_user_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, user_url, api_client):
    user = baker.make(User)
    assert user_client.delete(user_url + str(user.id) + '/').status_code == 403
    assert manager_client.delete(user_url + str(user.id) + '/').status_code == 403
    assert driver_client.delete(user_url + str(user.id) + '/').status_code == 403
    assert boss_client.delete(user_url + str(user.id) + '/').status_code == 403
    assert admin_client.delete(user_url + str(user.id) + '/').status_code == 204
    assert api_client.delete(user_url + str(user.id) + '/').status_code == 403

def test_repair_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, repair_url, api_client):
    user = baker.make(models.User)
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    driver = baker.make(models.Driver, car=car, driver=user)
    repair = baker.make(models.Repair, driver=driver)
    assert user_client.delete(repair_url + str(repair.id) + '/').status_code == 403
    assert manager_client.delete(repair_url + str(repair.id) + '/').status_code == 403
    assert driver_client.delete(repair_url + str(repair.id) + '/').status_code == 403
    assert boss_client.delete(repair_url + str(repair.id) + '/').status_code == 403
    assert admin_client.delete(repair_url + str(repair.id) + '/').status_code == 204
    assert api_client.delete(repair_url + str(repair.id) + '/').status_code == 403

def test_refuel_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, refuel_url, api_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    refuel = baker.make(models.Refuel, car=[car])
    assert user_client.delete(refuel_url + str(refuel.id) + '/').status_code == 403
    assert manager_client.delete(refuel_url + str(refuel.id) + '/').status_code == 403
    assert driver_client.delete(refuel_url + str(refuel.id) + '/').status_code == 403
    assert boss_client.delete(refuel_url + str(refuel.id) + '/').status_code == 403
    assert admin_client.delete(refuel_url + str(refuel.id) + '/').status_code == 204
    assert api_client.delete(refuel_url + str(refuel.id) + '/').status_code == 403

def test_order_delete_status(user_client, manager_client, driver_client,
                        boss_client, admin_client, order_url, api_client):
    user = baker.make(models.User, _quantity=2)
    dimensions = baker.make(models.Dimensions, _quantity=2)
    car_type = baker.make(models.CarType, dimensions=dimensions[0])
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    driver = baker.make(models.Driver, car=car, driver=user[0])
    manager = baker.make(models.Manager, manager=user[1])
    order = baker.make(models.Order, driver=[driver], manager=manager, car=[car],
                       dimensions=[dimensions[1]])
    assert user_client.delete(order_url + str(order.id) + '/').status_code == 403
    assert manager_client.delete(order_url + str(order.id) + '/').status_code == 403
    assert driver_client.delete(order_url + str(order.id) + '/').status_code == 403
    assert boss_client.delete(order_url + str(order.id) + '/').status_code == 403
    assert admin_client.delete(order_url + str(order.id) + '/').status_code == 204
    assert api_client.delete(order_url + str(order.id) + '/').status_code == 403
