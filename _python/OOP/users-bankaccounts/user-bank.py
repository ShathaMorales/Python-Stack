class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.2, balance=0)
        self.accounts = []

    # updated User class make_deposit method
    def make_deposit(self, amount):
        self.account.balance += amount

    # updated User class make_withdrawal method
    def make_withdrawal(self, amount):
        self.account.balance -= amount

    # updated user_display_balance in class User
    def display_user_balance(self):
        print(f"{self.name}'s balance is: {self.account.balance}")

    # to allow a user to have multiple accounts
    def add_account(self, int_rate=0.2, balance=0):
        self.accounts.append(BankAccount(int_rate, balance))
