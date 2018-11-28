from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import RequestContext, Template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tickets.models import Passenger, Bus, Terminal, Driver, Trip, Rating, Booking, Bus_Trip, Bus_Driver, CurrentTerminal
from tickets.serializers import PassengerSerializer, BusSerializer, TerminalSerializer,DriverSerializer,TripSerializer,RatingSerializer,BookingSerializer,Bus_TripSerializer,Bus_DriverSerializer,CurrentTerminalSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def PassengerViews(request, pk):
    try:
        passengers = Passenger.objects.get(userID = pk)
    except Passenger.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassengerSerializer(passengers)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PassengerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = PassengerSerializer(passengers, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        passengers.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

