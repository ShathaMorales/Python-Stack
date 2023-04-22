class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"You have withdrawn {amount} from your account")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self


# Create three instances of User class
user1 = User("Chris", 20)
user2 = User("Dan", 30)
user3 = User("Michelle", 40)

# User1 makes 3 deposits
user1.make_deposit(100).make_deposit(200).make_deposit(300)

# User1 makes 1 withdrawal
user1.make_withdrawal(100)

# Display user1's balance
user1.display_user_balance()

# User2 makes 2 deposits of $500 and $100
user2.make_deposit(500).make_deposit(100)

# User2 makes 2 withdrawals of $200 and $100
user2.make_withdrawal(200).make_withdrawal(100)

# Display user2's balance
user2.display_user_balance()

# User3 makes a deposit of $1000
user3.make_deposit(1000)

# User3 make 3 withdrawals of $100, $200, and $50
user3.make_withdrawal(100).make_withdrawal(200).make_withdrawal(50)

# Display user3's balance
user3.display_user_balance()

# Transfer $150 from user1 to user3
user1.transfer_money(user3, 150)

# Display user1's balance
user1.display_user_balance()

# Display user3's balance
user3.display_user_balance()
