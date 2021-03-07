from unittest.case import TestCase

from accounts.models import Account
from accounts.models.exceptions import NotEnoughMoneyError


class TestAccounts(TestCase):

    def test_withdraw_is_working_fine(self):
        account = Account(amount=120)
        account.withdraw(10)

        self.assertEqual(account.amount, 110.0)

    def test_withdraw_not_enough_money(self):
        account = Account(amount=10)

        with self.assertRaises(NotEnoughMoneyError):
            account.withdraw(30)
