from django.shortcuts import render, redirect
from django.views import View
from .models import Vehicle, Service, Appointment
from .forms import AppointmentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Vehicle, Service, Employee
from django.shortcuts import render, redirect
from django.views import View
from .forms import AppointmentForm, VehicleForm

class HomeView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'home.html', {'services': services})

class ServicesView(View):
    def get(self, request):
        services = Service.objects.all()
        return render(request, 'services.html', {'services': services})



class AppointmentView(View):
    def get(self, request):
        appointment_form = AppointmentForm()
        vehicle_form = VehicleForm()
        vehicles = Vehicle.objects.all()
        return render(request, 'appointment.html', {
            'appointment_form': appointment_form,
            'vehicle_form': vehicle_form,
            'vehicles': vehicles
        })

    def post(self, request):
        if 'vehicle_submit' in request.POST:
            vehicle_form = VehicleForm(request.POST)
            if vehicle_form.is_valid():
                vehicle_form.save()
                return redirect('appointment')
        else:
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                return redirect('home')
        
        appointment_form = AppointmentForm()
        vehicle_form = VehicleForm()
        vehicles = Vehicle.objects.all()
        return render(request, 'appointment.html', {
            'appointment_form': appointment_form,
            'vehicle_form': vehicle_form,
            'vehicles': vehicles
        })


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    

class StaffView(LoginRequiredMixin, View):
    def get(self, request):
        employees = Employee.objects.all().order_by('user__last_name', 'user__first_name')
        return render(request, 'staff.html', {'employees': employees})

