from rest_framework import serializers
from rest_framework.serializers import Serializer

from currency.models import Meteo


class MeteoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meteo
        fields = '__all__'

class WeatherSerializer(SerializerSerializer):
class WeatherSerializer(SerializerSerializer):
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
