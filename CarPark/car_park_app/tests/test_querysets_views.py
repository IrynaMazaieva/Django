import pytest
from model_bakery import baker, recipe
from car_park_app import views, models, serializers
from unittest.mock import MagicMock
import requests
from django.urls import reverse
from django.contrib.auth.models import User, Group
from CarPark import settings


#  QUERYSETS

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

def test_q1(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    user = baker.make(User, _quantity=2)
    baker.make(models.Driver, driver=user[0])
    url = reverse('query_1-list')
    url = url + '?user=' + str(user[0].username)
    assert admin_client.get(url).status_code == 200
    assert not boss_client.get(url).status_code == 200

def test_q2(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    user = baker.make(User, _quantity=2)
    baker.make(models.Driver, driver=user[0])
    url = reverse('query_2-list')
    url = url + '?user=' + str(user[0].username)
    assert admin_client.get(url).status_code == 200
    assert boss_client.get(url).status_code == 200

def test_q3(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    user = baker.make(User, _quantity=2)
    baker.make(models.Driver, driver=user[0])
    url = reverse('query_3-list')
    assert admin_client.get(url).status_code == 200
    assert boss_client.get(url).status_code == 200

def test_q4(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    dimensions = baker.make(models.Dimensions)
    car_type = baker.make(models.CarType, dimensions=dimensions)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type, fuel_type=[fuel_type])
    url = reverse('query_4-list')
    url = url + '?car_id=' + str(car.id)
    assert admin_client.get(url).status_code == 200
    assert boss_client.get(url).status_code == 200

def test_q5(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    user = baker.make(User, _quantity=2)
    baker.make(models.Driver, driver=user[0])
    url = reverse('query_5-list')
    url = url + '?driver=' + str(user[0].username)
    assert admin_client.get(url).status_code == 200
    assert boss_client.get(url).status_code == 200

def test_q6(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    user = baker.make(User, _quantity=2)
    baker.make(models.Manager, manager=user[0])
    url = reverse('query_6-list')
    url = url + '?manager=' + str(user[0].username)
    assert admin_client.get(url).status_code == 200
    assert boss_client.get(url).status_code == 200

def test_q7(driver_client, manager_client, boss_client,
            admin_client, api_client, user_client):
    user = baker.make(models.User, _quantity=2)
    dimensions = baker.make(models.Dimensions, _quantity=2)
    car_type = baker.make(models.CarType, dimensions=dimensions[0], _quantity=10)
    fuel_type = baker.make(models.Fuel)
    car = baker.make(models.Car, car_type=car_type[0], fuel_type=[fuel_type], _quantity=10)
    driver1 = baker.make(models.Driver, car=car[0], driver=user[0])
    driver2 = baker.make(models.Driver, car=car[1], driver=user[0])
    baker.make(models.Repair, driver=driver1, _quantity=20)
    baker.make(models.Repair, driver=driver2, _quantity=20)
    manager = baker.make(models.Manager, manager=user[1])
    baker.make(models.Order, driver=[driver1], manager=manager, car=[car[0]],
                       dimensions=[dimensions[1]])
    url = reverse('query_7-list')
    url = url + '?height=3&width=2&length=1&weight=100&day=01&month=11&year=2020'
    assert admin_client.get(url).status_code == 200
    assert boss_client.get(url).status_code == 200