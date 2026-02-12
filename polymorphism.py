# Polymorphism allows different classes to use the same method name but behave differently

# Method overloading; Python allows operators to behave differently depending on the data type

# Payment system where different payment methods to use the same method name 'Pay', but in the end the 'Pay' will behave differently

class Payment:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount


    def Pay(self):
        return f"You paid {self.amount} to {self.name}"

class PayPal(Payment):

    def Pay(self, amount, name):
        return f"You paid {amount} to {name} via PayPal"


pal = PayPal('Pal', 20000, 10000)
print(pal.Pay(amount=10000, name="Pal"))