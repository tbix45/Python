class User:

    def __init__(self, name):
        # we assign them accordingly
        self.name = name
        # the account balance is set to $0
        self.amount = 0

    def make_withdrawal(self, amount):
        self.amount -= amount
        return self

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def transfer(self, amount, user):
        self.amount -= amount
        user.amount += amount
        print(f"User: {self.name}, Balance: {self.amount}")
        print(f"User: {user.name}, Balance: {user.amount}")
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance:{self.amount}")
        return self


guido = User("Guido van Rossum")
monty = User("Monty Python")
tom = User("Tom Bob")
# print(guido.name)  # output: Guido van Rossum
# print(monty.name)  # output: Monty Python
# guido.make_deposit(100)
# guido.make_deposit(200)
# guido.make_deposit(300)
# guido.make_withdrawal(100)
# guido.display_user_balance()
guido.make_deposit(100).make_deposit(200).make_deposit(
    300).make_withdrawal(100).display_user_balance()
# print(guido.display_user_balance)
# monty.make_deposit(100)
# monty.make_deposit(200)
# monty.make_withdrawal(200)
# monty.make_withdrawal(100)
# monty.display_user_balance()
monty.make_deposit(100).make_deposit(200).make_withdrawal(
    300).make_withdrawal(100).display_user_balance()
# tom.make_deposit(100)
# tom.make_withdrawal(200)
# tom.make_withdrawal(200)
# tom.make_withdrawal(100)
# tom.display_user_balance()
tom.make_deposit(100).make_withdrawal(200).make_withdrawal(
    300).make_withdrawal(100).display_user_balance()

guido.transfer(300, tom)
