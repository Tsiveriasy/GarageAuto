from django.contrib import admin
from .models import Vehicle, Service, Appointment, Employee

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'license_plate', 'owner')
    search_fields = ('make', 'model', 'license_plate', 'owner')
    list_filter = ('year', 'make')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'service', 'date', 'completed')
    list_filter = ('completed', 'date', 'service')
    search_fields = ('vehicle__license_plate', 'vehicle__owner')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'position', 'hire_date', 'phone_number')
    search_fields = ('user__first_name', 'user__last_name', 'position')
    list_filter = ('position', 'hire_date')

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Nom complet'

