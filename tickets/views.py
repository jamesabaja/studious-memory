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

@api_view(['GET', 'POST'])
def PassengerList(request):
    if request.method == 'GET':
        passengers = Passenger.objects.all()
        serializer = PassengerSerializer(passengers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PassengerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def PassengerViews(request, pk):
    try:
        passengers = Passenger.objects.get(userID=pk)
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

@api_view(['GET', 'POST'])
def BusList(request):
    if request.method == 'GET':
        busses = Bus.objects.all()
        serializer = BusSerializer(busses, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def BusViews(request, pk):
    try:
        busses = Bus.objects.get(busID=pk)
    except Bus.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BusSerializer(busses)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BusSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = BusSerializer(busses, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        busses.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def TerminalList(request):
    if request.method == 'GET':
        terminals = Terminal.objects.all()
        serializer = TerminalSerializer(terminals, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TerminalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TerminalViews(request, pk):
    try:
        terminals = Terminal.objects.get(terminalID=pk)
    except Terminal.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TerminalSerializer(terminals)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TerminalSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = TerminalSerializer(terminals, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        terminals.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def TripList(request):
    if request.method == 'GET':
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def TripViews(request, pk):
    try:
        trips = Trip.objects.get(tripID=pk)
    except Driver.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TripSerializer(trips)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TripSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = TripSerializer(trips, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        trips.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)