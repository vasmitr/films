from rest_framework import serializers

from seances.serializers import SeanceSerializer
from .models import Ticket, Seat


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    seance = SeanceSerializer()
    class Meta:
        model = Seat
        fields = ('pk', 'number', 'seance', 'row_markup',
                  'reserved')


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    seat = SeatSerializer(many=True)
    
    class Meta:
        model = Ticket
        fields = ('pk', 'seat', 'film',
                  'price')
