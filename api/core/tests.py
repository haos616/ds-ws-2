from django.urls import reverse
from django.utils import timezone

from rest_framework.test import APITestCase
from rest_framework import status


class AccountTests(APITestCase):
    def test_get_time(self):
        url = reverse('api-time')
        start_date = timezone.now()
        response = self.client.get(url)
        end_date = timezone.now()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(response.data, start_date)
        self.assertLess(response.data, end_date)
