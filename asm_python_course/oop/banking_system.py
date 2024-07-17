# Define a class for a BankAccount
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited ${amount}. New balance: ${self.__balance}"

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds!"
        self.__balance -= amount
        return f"Withdrew ${amount}. New balance: ${self.__balance}"

    def get_balance(self):
        return f"Current balance: ${self.__balance}"

# Get user input to create a bank account
owner = input("Enter the account owner's name: ")
account = BankAccount(owner)

# Interact with the account
while True:
    action = input("Do you want to 'deposit', 'withdraw', 'check balance', or 'quit' to exit: ").lower()
    if action == 'quit':
        break
    elif action == 'deposit':
        amount = float(input("Enter the amount to deposit: "))
        print(account.deposit(amount))
    elif action == 'withdraw':
        amount = float(input("Enter the amount to withdraw: "))
        print(account.withdraw(amount))
    elif action == 'check balance':
        print(account.get_balance())
    else:
        print("Invalid action")
