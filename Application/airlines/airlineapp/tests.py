import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy

from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from .model_factories import *
from .serializers import *

class AirlineSerializerTest(APITestCase):
    airline1 = None
    airlineserializer = None
    
    def setUp(self):
        self.airline1 = AirlineFactory.create (pk = 1, name="airline 1")
        self.airlineserializer = AirlineSerializer(instance=self.airline1)

    def tearDown(self):
        Countries.objects.all().delete()
        Airlines.objects.all().delete()

    def test_airlineSerializer(self):
        data = self.airlineserializer.data
        self.assertEqual(set(data.keys()), set(['name', 'alias', 'iata', 'icao', 'callsign', 'active']))

    def test_airlineSerializerAirlineNameHasCorrectData(self):
        data = self.airlineserializer.data
        self.assertEqual(data['name'], 'airline 1')

class AirlineTest(APITestCase):

    airline1 = None
    airline2 = None
    good_url = ''
    bad_url = ''
    delete_url = ''

    def setUp(self):
        self.airline1 = AirlineFactory.create (pk = 1, name="airline 1")
        self.airline2 = AirlineFactory.create (pk = 2)
        self.good_url = reverse('airline_detail_api', kwargs={'pk': 1})
        self.bad_url = reverse('airline_detail_api', kwargs={'pk': 3})
        self.delete_url = reverse('airline_detail_api', kwargs={'pk': 1})
    
    def tearDown(self):
        Countries.objects.all().delete()
        Airlines.objects.all().delete()

    def test_airlineInfoReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_airlineInfoReturnCorrectField(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        data = json.loads(response.content)
        self.assertTrue('name' in data)

    def test_airlineInfoReturnCorrectName(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        data = json.loads(response.content)
        self.assertEqual(data['name'], 'airline 1')

    def test_airlineInfoReturnFailOnBadPK(self):
        response = self.client.get(self.bad_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 404)

    def test_airlineInfoDeleteIsSuccessful(self):
        response = self.client.delete(self.delete_url, format='json')
        self.assertEqual(response.status_code, 204)

class AirportTest(APITestCase):
    airport1 = None
    airport2 = None
    good_url = ''
    bad_url = ''

    def setUp(self):
        self.airport1 = AirportFactory.create (pk = 1)
        self.airport2 = AirportFactory.create (pk = 2)
        self.good_url = reverse('airport_detail_api', kwargs={'pk': 1})
        self.bad_url = reverse('airport_detail_api', kwargs={'pk': 3})

    def tearDown(self):
        Countries.objects.all().delete()
        Airports.objects.all().delete()

    def test_airportInfoReturnSuccess(self):
        response = self.client.get(self.good_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 200)

    def test_airportInfoReturnFailOnBadPK(self):
        response = self.client.get(self.bad_url, format='json')
        response.render()
        self.assertEqual(response.status_code, 404)