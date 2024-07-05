import factory
from random import *
from django.test import TestCase
from django.conf import settings
from django.core.files import File

from .models import *

class CountryFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Airline%d' % n+str(1))
    iso_code = "TST"
    dafif_code = "TESTCODE"

    class Meta:
        model = Countries

class AirlineFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: 'Airline%d' % n+str(1))
    alias = factory.Faker('sentence', nb_words=1)
    iata = "TS"
    icao = "TST"
    callsign = "Test Callsign"
    active = choice(['Y', 'N'])
    country = factory.SubFactory(CountryFactory)

    class Meta:
        model = Airlines

class AirportFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('sentence', nb_words=2)
    city = factory.Faker('sentence', nb_words=1)
    country = factory.SubFactory(CountryFactory)
    iata = "ABC"
    icao = "ABCD"
    latitude = 10.44
    longitude = 10.44
    altitude = 5000
    timezone = factory.Faker('sentence', nb_words=1)
    dst = choice(['E', 'A', 'S', 'O', 'Z', 'N', 'U'])
    tz_db = "test_tz"
    type = "airport"
    source = "MyAirports"

    class Meta:
        model = Airports