import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class Test_case_1(APITestCase):
    def test_1(self):
        url = reverse('get_session')
        response = self.client.post(url)
        self.assertIsNotNone(response.cookies['sessionid'].value)


if __name__ == '__main__':
    unittest.main()
