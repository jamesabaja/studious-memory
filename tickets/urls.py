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
    path('tickets/trips/', views.TripList),
    path('tickets/trips/<str:pk>/', views.TripViews),
]
urlpatterns = format_suffix_patterns(urlpatterns)