import requests
import unittest

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)


class RequestTest(unittest.TestCase):
    def test_status_Code(self):
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main()