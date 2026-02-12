# Abstraction is the process of hiding complex implementation details and showing only the essential features of an object

# Abstraction focuses on what an object does and instead of how it does it

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

# You cannot make an object out of an abstract class
# Any subclass must implement an abstract method

class Car(Vehicle):
    def move(self):
        print("Car moves on the road")

class Boat(Vehicle):
    def move(self):
        print("Boat moves on the water")

# create an abstract class

class Payment(ABC):

    @abstractmethod
    def pay(self, amount, name):
        pass
        # return f"You paid {amount} to {name}"

class CreditCard(Payment):

    def pay(self, amount, name):
        print(f"You paid {amount} to {name} using Credit Card \n")

class PayPal(Payment):

    def pay(self, amount, name):
        print(f"You paid {amount} to {name} using PayPal \n")


class BankTransfer(Payment):

    def pay(self, amount, name):
        print(f"You paid {amount} to {name} using Bank Transfer \n")

payments = [
    PayPal(),
    CreditCard(),
    PayPal(),
]

for method in payments:
    method.pay(1000, 'Alexius')


# The parent class defines what must be done.
# It defines the blueprint.
# Each payment type decide how it's own must be done.
# All of them will inherit the pay method, then decide how they want it to work.
# The system works without knowing the internal implements


# The project is to simulate a simple bank system where:
# 1: Users can create account
# 2: Deposit Money
# 3: Withdraw Money
# 4: Transfer Money
# 5: View Balance
# 6: User should be able to save data to file


# To be submitted 10am on Tuesday 17th of February