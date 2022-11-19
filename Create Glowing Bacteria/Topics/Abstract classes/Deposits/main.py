from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        pass

    def add_interest(self):
        pass


# create SavingsAccount and Deposit
class SavingsAccount(Account):
    def add_money(self, amount):
        if amount < 10:
            print("Cannot add to SavingsAccount: amount too low.")
            return

        self.sum += amount


class Deposit(Account):
    def __init__(self, starting_sum, interest):
        super().__init__(starting_sum, interest)
        self.sum += starting_sum * interest

    def add_money(self, amount):
        if amount < 50:
            print("Cannot add to Deposit: amount too low.")
            return

        self.sum += amount + amount * self.interest
