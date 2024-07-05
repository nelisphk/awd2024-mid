from django.contrib import admin
from .models import *

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'iso_code', 'dafif_code')
    ordering = ['name']

admin.site.register(Countries, CountriesAdmin)

class PlanesAdmin(admin.ModelAdmin):
    list_display = ('name', 'iata', 'icao')
    ordering = ['name']

admin.site.register(Planes, PlanesAdmin)

class AirlinesAdmin(admin.ModelAdmin):
    list_display = ('name', 'alias', 'iata', 'icao', 'callsign', 'active', 'country')
    ordering = ['name']

admin.site.register(Airlines, AirlinesAdmin)

class AirportsAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'country', 'iata', 'icao', 'latitude', 'longitude', 'altitude', 'timezone', 'dst', 'tz_db', 'type', 'source')
    ordering = ['name']

admin.site.register(Airports, AirportsAdmin)

class Equipment_listInLine(admin.TabularInline):
    model = Equipment_list
    extra = 1

class RoutesAdmin(admin.ModelAdmin):
    list_display = ('airline_id', 'from_airport', 'to_airport', 'codeshare', 'stops')
    inlines = [Equipment_listInLine]

admin.site.register(Routes, RoutesAdmin)