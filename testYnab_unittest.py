import unittest
import ynab
from requests.models import Response

class TestYnab(unittest.TestCase):
    def test_ynab(self):
        the_response = Response()
        the_response.code = "expired"
        the_response.error_type = "expired"
        the_response.status_code = 200
        the_response._content = b'{ "key" : "a" }'

        print(the_response.json())




