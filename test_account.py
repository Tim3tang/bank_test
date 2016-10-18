import unittest
from account import Account
from bank import Bank


class AccountTest(unittest.TestCase):
    def test_account_balance_empty(self):
        acc = Account(0)
        self.assertEqual(0, acc.display)

    def test_deposit_adds_to_balance(self):
        acc = Account(0)
        acc.deposit(10)
        self.assertEqual(10, acc.display)

    def test_withdrawal_reduces_balance(self):
        acc = Account(10)
        acc.withdrawal(5)
        self.assertEqual(5, acc.display)
        
if __name__ == '__main__':
    unittest.main()
