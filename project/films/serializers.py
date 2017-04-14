from rest_framework import serializers

from .models import Film, Tag, STARS

class FilmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Film
        fields = ('name', 'rating', 'image', 'base_price',
                  'relise_date', 'tags')

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name',)
