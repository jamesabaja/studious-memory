from django.conf.urls import url
from tickets import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
]