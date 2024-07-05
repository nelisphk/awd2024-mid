from rest_framework import serializers
from .models import *

class AirlinesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = ['pk', 'name']

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airlines
        fields = ['name', 'alias', 'iata', 'icao', 'callsign', 'active']

class AirportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = ['pk', 'name', 'city', 'country']

class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = ['pk', 'name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude', 'timezone', 'dst', 'tz_db', 'type', 'source']
    
class EquipmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = ['pk', 'name']

class EqipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planes
        fields = ['pk', 'name', 'icao', 'iata']
    
    def create(self, validated_data):
        plane = Planes(**{**validated_data})
        plane.save()
        return plane
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.icao = validated_data.get('icao', instance.icao)
        instance.iata = validated_data.get('iata', instance.iata)
        instance.icao = validated_data.get('icao', instance.icao)
        instance.save()
        return instance