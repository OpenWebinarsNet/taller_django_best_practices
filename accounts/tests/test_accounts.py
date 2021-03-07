from rest_framework import status
from rest_framework.test import APITestCase

from accounts.models import Account


class TestAccounts(APITestCase):

    def setUp(self) -> None:
        self._create_accounts()

    def test_list_accounts(self):
        response = self.client.get('/accounts/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        accounts = response.json()

        self.assertEqual(len(accounts), Account.objects.count())

    def _create_accounts(self):
        Account.objects.create(amount=130.0)
