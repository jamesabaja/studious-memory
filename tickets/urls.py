from django.conf.urls import url
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tickets import views

urlpatterns = [
    #url(r'^$', views.HomePageView.as_view(), name='home'),
    path('tickets/', views.PassengerList),
    path('tickets/<str:pk>/', views.PassengerViews),
]
urlpatterns = format_suffix_patterns(urlpatterns)