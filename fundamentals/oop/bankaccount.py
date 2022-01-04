class BankAccount:

    all_accounts = []

    def __init__(self, balance=0, int_rate=0.05):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance <= 0:
            print("Insufficient funds: Chargin a $5 fee.")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def yield_interest(self):
        if self.balance <= 0:
            return self
        else:
            print(f"You earned ${(self.balance * self.int_rate)}(s) interest.")
            self.balance += (self.balance * self.int_rate)
            return self

    def display_account_info(self):
        print(f"Interest rate: {self.int_rate}, Balance: {self.balance}")
        return self
# ====================================================================
# bonus

    @classmethod
    def all_accounts_info(cls):
        for account in cls.all_accounts:
            account.display_account_info()


# ====================================================================
checking = BankAccount()
checking.deposit(200).deposit(200).deposit(200).withdraw(
    100).yield_interest().display_account_info()
checking2 = BankAccount(int_rate=0.07, balance=200)
checking2.deposit(2000).deposit(300).withdraw(300).withdraw(
    100).withdraw(100).withdraw(200).yield_interest().display_account_info()

BankAccount.all_accounts_info()
# checking.deposit(200)
# checking.deposit(200)
# checking.withdraw(100)
# checking.display_account_info()
# checking.yield_interest()
# checking.display_account_info()
