from django.test import TestCase
from .models import Airport
from .utils import find_airport


class AirportTests(TestCase):

    def test_find_airport(self):
        airport = Airport(name='HONINGTON', icao='EGXH',
                          latitude=52.342611, longitude=0.772939)
        airport.save()
        airport = Airport(name='WELSHPOOL', icao='EGCW',
                          latitude=52.628611, longitude=-3.153333)
        airport.save()
        airport = Airport(name='CRANFIELD', icao='EGTC',
                          latitude=52.072222, longitude=-0.616667)
        airport.save()
        airport = Airport(name='KEMBLE', icao='EGBP',
                          latitude=51.668056, longitude=-2.056944)
        airport.save()
        airports = Airport.objects.all()
        self.assertIs(airports.count(), 4)

        (found, nearest) = find_airport(airports, 52, 1)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, 'HONINGTON')

        
