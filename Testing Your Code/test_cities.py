import unittest

class CityTest(unittest.TestCase):
    def test_city_countr():
        formatted_city = stuff('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile')