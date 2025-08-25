class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance   # use private variable

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    @property
    def is_rich(self):
        return self._balance >= 100000

    def deposit(self, amount):
        self.balance = self._balance + amount

    def withdraw(self, amount):
        if self._balance >= amount:
            self.balance = self._balance - amount
        else:
            print("No sufficient balance in account")
