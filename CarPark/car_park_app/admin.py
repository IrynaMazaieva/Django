from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Fuel, Car, CarType, Dimensions, Refuel, Repair, Order, Driver, Manager


class FlatPageAdmin(admin.ModelAdmin):
    fields = ('url', 'title', 'content')


class CarTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'body_type', 'carrying_capacity', 'dimensions')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class CarAdmin(admin.ModelAdmin):
    list_display = ('license_plate', 'car_type')
    search_fields = ('license_plate',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(CarType, CarTypeAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Fuel)
admin.site.register(Dimensions)
admin.site.register(Order)
admin.site.register(Driver)
admin.site.register(Refuel)
admin.site.register(Repair)
admin.site.register(Manager)
