class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.amount = 0
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"You have withdrawn {amount} from your account")
        return self.account_balance

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self.account_balance


# create three instances of User class
user1 = User("Chris", 20)
user2 = User("Dan", 30)
user3 = User("Michelle", 40)

# user1 makes 3 deposits
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_deposit(300)

# user1 makes 1 withdrawal
user1.make_withdrawal(100)
print(f"You have withdrawn {user1.account_balance.amount} from your account")

# display user1's balance
user1.display_user_balance()
print(f"User: {user1.name}, Balance: {user1.account_balance}")

# user2 makes 2 deposits of $500 and $100
user2.make_deposit(500)
user2.make_deposit(100)

# user2 makes 2 withdrawals of $200 and $100
user2.make_withdrawal(200)
user2.make_withdrawal(100)
print(f"You have withdrawn {user2.account_balance.amount} from your account")

# display user2's balance
user2.display_user_balance()
print(f"User: {user2.name}, Balance: {user2.account_balance}")

# user3 makes a deposit of $1000
user3.make_deposit(1000)

# user3 make 3 withdrawals of $100, $200, and $50
user3.make_withdrawal(100)
user3.make_withdrawal(200)
user3.make_withdrawal(50)
print(f"You have withdrawn {user3.account_balance.amount} from your account")

# display user3's balance
user3.display_user_balance()
print(f"User: {user3.name}, Balance: {user3.account_balance}")

# Transfer $150 from user1 to user3
user1.transfer_money(user3, 150)

# display user1's balance
user1.display_user_balance()
print(f"User: {user1.name}, Balance: {user1.account_balance}")

# display user3's balance
user3.display_user_balance()
print(f"User: {user3.name}, Balance: {user3.account_balance}")
