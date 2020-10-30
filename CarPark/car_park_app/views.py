from rest_framework import viewsets
from django.db.models import Prefetch
from django.utils.timezone import now, datetime
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
from .serializers import (
    CarListSerializer, CarCreateSerializer,
    CarTypeSerializer, CarTypeCreateSerializer,
    FuelSerializer,
    UserSerializer,
    DimensionsSerializer,
    ManagerSerializer, ManagerCreateSerializer,
    DriverSerializer, DriverCreateSerializer,
    RefuelSerializer, RefuelCreateSerializer,
    RepairSerializer, RepairCreateSerializer,
    OrderSerializer, OrderCreateSerializer,
    Query_driver_Serializer,
    Query_manager_Serializer,
    Query_7_Serializer
)
from .permissions import (
    IsAdmin,
    IsDriver,
    IsManager,
    IsBoss,
    ReadOnly
)
from rest_framework.permissions import SAFE_METHODS


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    create_serializer_class = CarCreateSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class CarTypeViewSet(viewsets.ModelViewSet):
    queryset = CarType.objects.all()
    serializer_class = CarTypeSerializer
    create_serializer_class = CarTypeCreateSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class FuelViewSet(viewsets.ModelViewSet):
    queryset = Fuel.objects.all()
    serializer_class = FuelSerializer
    permission_classes = [IsAdmin | ReadOnly]


class DimensionsViewSet(viewsets.ModelViewSet):
    queryset = Dimensions.objects.all()
    serializer_class = DimensionsSerializer
    permission_classes = [IsAdmin | IsManager | ReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin | ReadOnly]


class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    create_serializer_class = DriverCreateSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer
    create_serializer_class = ManagerCreateSerializer
    permission_classes = [IsAdmin | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class RepairViewSet(viewsets.ModelViewSet):
    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    create_serializer_class = RepairCreateSerializer
    permission_classes = [IsAdmin | IsDriver | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class RefuelViewSet(viewsets.ModelViewSet):
    queryset = Refuel.objects.all()
    serializer_class = RefuelSerializer
    create_serializer_class = RefuelCreateSerializer
    permission_classes = [IsAdmin | IsDriver | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    create_serializer_class = OrderCreateSerializer
    permission_classes = [IsAdmin | IsManager | ReadOnly]

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.serializer_class
        return self.create_serializer_class


class Query_1_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q1/?user=Igor
    """

    permission_classes = [IsBoss | IsAdmin]
    serializer_class = OrderSerializer

    def get_queryset(self):
        name = self.request.query_params['user']
        driver_obj = Driver.objects.filter(driver__username=name).first()
        return Order.objects.filter(time__gte=now()).filter(driver=driver_obj)


class Query_2_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q2/?user=admin
    """
    serializer_class = RefuelSerializer
    permission_classes = [IsBoss | IsAdmin | ReadOnly]

    def get_queryset(self):
        name = self.request.query_params['user']
        driver_obj = Driver.objects.filter(driver__username=name).first()
        car = Car.objects.filter(driver=driver_obj).first()
        return Refuel.objects.filter(car=car)


class Query_3_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q3/
    """
    serializer_class = RepairSerializer
    permission_classes = [IsBoss | IsAdmin | ReadOnly]

    def get_queryset(self):
        return Repair.objects.filter(date_out__gte=now()).select_related('driver')


class Query_4_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q4/?car_id=1
    """
    serializer_class = Query_driver_Serializer
    permission_classes = [IsBoss | IsAdmin | ReadOnly]

    def get_queryset(self):
        car = self.request.query_params['car_id']
        return Order.objects.filter(car__id=car).prefetch_related(Prefetch('driver'))


class Query_5_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q5/?driver=Mykola
    """
    serializer_class = Query_manager_Serializer
    permission_classes = [IsBoss | IsAdmin | ReadOnly]

    def get_queryset(self):
        driver = self.request.query_params['driver']
        return Order.objects.filter(driver__driver__username=driver).prefetch_related(Prefetch('manager'))


class Query_6_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q6/?manager=Vasyl
    """
    serializer_class = Query_driver_Serializer
    permission_classes = [IsBoss | IsAdmin | ReadOnly]

    def get_queryset(self):
        manager = self.request.query_params['manager']
        manager = Manager.objects.filter(manager__username=manager).select_related('manager')
        return Order.objects.prefetch_related(Prefetch('manager', queryset=manager)).order_by('milleage')


class Query_7_ViewSet(viewsets.ModelViewSet):
    """
        example: http://127.0.0.1:8000/api/q7/?height=3&width=2&length=1&weight=100&day=01&month=11&year=2020
    """
    serializer_class = Query_7_Serializer
    permission_classes = [IsBoss | IsAdmin | ReadOnly]

    def get_queryset(self):
        dims = [
            float(self.request.query_params['length']),
            float(self.request.query_params['width']),
            float(self.request.query_params['height'])
        ]
        weigth = float(self.request.query_params['weight'])
        date = datetime(
            day=int(self.request.query_params['day']),
            month=int(self.request.query_params['month']),
            year=int(self.request.query_params['year'])
        )
        dims.sort()
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
        return car_list
