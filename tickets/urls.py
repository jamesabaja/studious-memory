from django.conf.urls import url
from django.urls import path
from tickets import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    path('tickets/', views.PassengerViews),
]