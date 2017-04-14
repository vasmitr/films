from rest_framework import serializers

from .models import Day, Seance


class DaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Day
        fields = ('number', 'weekend', 'weekend_markup')


class SeanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seance
        fields = ('pk', 'start', 'end', 'film',
                  'day', 'time_markup',)
