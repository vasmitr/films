from django.http import Http404

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
                          

from .models import Day, Seance
from .serializers import DaySerializer, SeanceSerializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer


class SeanceList(APIView):

    def get(self, request, format=None):
        day = self.request.GET.get('day')
        film = self.request.GET.get('film')
        seances = Seance.objects.all()
        
        if day:
            seances = seances.filter(day=day)
        if film:
            seances = seances.filter(film=film)

        serializer = SeanceSerializer(seances, many=True,
        context={'request': request})

        return Response(serializer.data)


class SeanceDetail(APIView):
    def get_object(self, pk):
        try:
            return Seance.objects.get(pk=pk)
        except Seance.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        seance = self.get_object(pk)
        serializer = SeanceSerializer(seance,
        context={'request': request})
        return Response(serializer.data)
