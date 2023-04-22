class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def display_account_info(self):
        print(f"Balance: {self.balance}, Interest Rate: {self.int_rate}")

    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest


# create bank account1
account1 = BankAccount(0.01, 1000)

# create bank account2
account2 = BankAccount(0.02, 500)

# account1 makes 3 deposits and 1 withdrawal then yields interest and displays account info
account1.deposit(100).deposit(200).deposit(300).withdraw(
    50).yield_interest().display_account_info()

# account2 makes 2 deposits and 4 withdrawals then yields interest and displays account info
account2.deposit(200).deposit(500).withdraw(100).withdraw(50).withdraw(
    50).withdraw(50).yield_interest().display_account_info()
