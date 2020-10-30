from rest_framework import routers
from django.urls import path, include

from .views import (
    CarViewSet,
    CarTypeViewSet,
    FuelViewSet,
    DimensionsViewSet,
    UserViewSet,
    DriverViewSet,
    ManagerViewSet,
    RepairViewSet,
    RefuelViewSet,
    OrderViewSet,
    Query_1_ViewSet,
    Query_2_ViewSet,
    Query_3_ViewSet,
    Query_4_ViewSet,
    Query_5_ViewSet,
    Query_6_ViewSet,
    Query_7_ViewSet
)

router = routers.DefaultRouter()
router.register(r'car', CarViewSet, basename='car')
router.register(r'car_type', CarTypeViewSet, basename='car_type')
router.register(r'fuel', FuelViewSet)
router.register(r'dimensions', DimensionsViewSet)
router.register(r'User', UserViewSet)
router.register(r'driver', DriverViewSet)
router.register(r'manager', ManagerViewSet)
router.register(r'repair', RepairViewSet)
router.register(r'refuel', RefuelViewSet)
router.register(r'order', OrderViewSet)
router.register(r'q1', Query_1_ViewSet, basename='query_1')
router.register(r'q2', Query_2_ViewSet, basename='query_2')
router.register(r'q3', Query_3_ViewSet, basename='query_3')
router.register(r'q4', Query_4_ViewSet, basename='query_4')
router.register(r'q5', Query_5_ViewSet, basename='query_5')
router.register(r'q6', Query_6_ViewSet, basename='query_6')
router.register(r'q7', Query_7_ViewSet, basename='query_7')


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
