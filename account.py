class Account:

    def __init__(self, balance):
        self.balance = balance

        def deposit(self, amount, date):
            date = date
            print("You deposited " + str(amount) + "on " + str(date))
            self.balance = self.balance + amount

        def withdrawal(self, amount, date):
            date = date
            print("You withdrew " + str(amount) + "on " + str(date))
            self.balance = self.balance - amount

        def display(self):
            return self.balance
