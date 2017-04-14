from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Seat, Ticket
from .serializers import SeatSerializer, TicketSerializer


class SeatList(APIView):
    def get(self, request, format=None):
        seance = self.request.GET.get('seance')
        seats = Seat.objects.all()
        if seance:
            seats = seats.filter(seance=seance)
            
        serializer = SeatSerializer(seats, many=True,
        context={'request': request})
        return Response(serializer.data)


class SeatDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Seat.objects.get(pk=pk)
        except Seat.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        seat = self.get_object(pk)
        serializer = SeatSerializer(seat,
        context={'request': request})
        return Response(serializer.data)


class TicketList(APIView):
    def get(self, request, format=None):
        owner = self.request.user
        tickets = Ticket.objects.all().filter(owner=owner)
        serializer = TicketSerializer(tickets, many=True,
        context={'request': request})
        return Response(serializer.data)


class TicketDetail(APIView):
    
    def get_object(self, pk):
        try:
            return Ticket.objects.get(pk=pk)
        except Ticket.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        ticket = self.get_object(pk)
        serializer = SeatSerializer(ticket,
        context={'request': request})
        return Response(serializer.data)
