from django.urls import path
from .views import HomeView, ServicesView, AppointmentView, ContactView, StaffView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('services/', ServicesView.as_view(), name='services'),
    path('appointment/', AppointmentView.as_view(), name='appointment'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('staff/', StaffView.as_view(), name='staff'),
]

