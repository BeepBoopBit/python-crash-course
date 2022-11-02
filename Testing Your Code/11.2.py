import unittest

def stuff(city_name, country_name, population):
    return city_name.title() + ', ' + country_name.title() + ' population ' + '- ' + str(population)

# Due to the naming convention that I have in the file, I'll put the class here

class CityTest(unittest.TestCase):
    def test_city_country(self):
        formatted_city = stuff('santiago', 'chile', 2000)
        self.assertEqual(formatted_city, 'Santiago, Chile population - 2000')
        
if __name__ == '__main__':
    unittest.main()
        