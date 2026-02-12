# Personal Assignment: Build a mobile banking flow in python using OOP concepts that you've learnt

class Account:
    def __init__(self, name):
        self.name = name

    def welcome(self, name):
        print(f"Welcome {name} to your account!")

    def menuOptions(self):
        pass


class User(Account): # made use of inheritance

    def __init__(self, name, balance, accountNumber):
        super().__init__(name) # made use of the super method to inherit the properties in the parent class
        self.__balance = balance # made use of encapsulation to make the balance private
        self.__accountNumber = accountNumber

    def getBalance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        self.__balance -= amount
        return self.__balance

print('WELCOME TO CODAR BANKING \n How may we help you? \n')
userInput = input()


