import unittest
from account import Account
from bank import Bank


class BankTest(unittest.TestCase):
    def test_bank_is_initially_empty(self):
        acc = Account(0)
        bank = Bank(acc)
        self.assertEqual({}, bank.statement)
        self.assertEqual(len(bank.statement), 0)

    def test_bank_history_updates_statement(self):
        acc = Account(0)
        bank = Bank(acc)
        acc.deposit(10)
        self.assertIn(acc.deposit, bank.statement)

if __name__ == '__main__':
    unittest.main()
