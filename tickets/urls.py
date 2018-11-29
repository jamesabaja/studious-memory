from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tickets import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    path('tickets/passengers/', views.PassengerList),
    path('tickets/passengers/<str:pk>/', views.PassengerViews),
    path('tickets/busses/', views.BusList),
    path('tickets/busses/<str:pk>/', views.BusViews),
    path('tickets/terminals/', views.TerminalList),
    path('tickets/terminals/<str:pk>/', views.TerminalViews),
    path('tickets/driver/', views.DriverList),
    path('tickets/driver/<str:pk>/', views.DriverViews),
    path('tickets/trips/', views.TripList),
    path('tickets/trips/<str:pk>/', views.TripViews),
    path('tickets/rating/', views.RatingList),
    #path('tickets/rating/<#>', views.RatingViews)
    path('tickets/booking/', views  .BookingList),
    #path('tickets/rating/<#>', views.BookingViews),
    path('tickets/bus_trip/', views.Bus_TripList),
    #path('tickets/bus_trip/<#>', views.Bus_TripViews),
    path('tickets/bus_driver/', views.Bus_DriverList),
    #path('tickets/bus_driver/<#>', views.Bus_DriverViews),
    path('tickets/current_terminal/', views.CurrentTerminalList),
    #path('tickets/current_terminal/<#>', views.CurrentTerminalViews),
]
urlpatterns = format_suffix_patterns(urlpatterns)