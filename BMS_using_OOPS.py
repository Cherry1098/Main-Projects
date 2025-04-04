'''############# Day14  task : BMS using OOPS ################ 21/03/25'''

from datetime import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.__balance = balance  # Encapsulation (private attribute)
        self.transactions = []  # Store transaction history

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(f"{datetime.now()} - Deposited ${amount:.2f}")
            return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(f"{datetime.now()} - Withdrawn ${amount:.2f}")
            return f"Withdrawn ${amount:.2f}. Remaining balance: ${self.__balance:.2f}"
        return "Insufficient balance or invalid amount."

    def check_balance(self):
        return f"Current Balance: ${self.__balance:.2f}"

    def mini_statement(self):
        return "\n".join(self.transactions[-5:])  # Last 5 transactions with timestamps


class BankUser:
    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.accounts = []

    def create_account(self, account_number, initial_deposit=0):
        new_account = BankAccount(account_number, self.name, initial_deposit)
        self.accounts.append(new_account)
        return f"Account {account_number} created successfully with balance ${initial_deposit:.2f}"

    def login(self, entered_password):
        return self.__password == entered_password


# Example Usage
users = {}

name = input("Enter your name: ")
password = input("Create a password: ")
users[name] = BankUser(name, password)
print(f"User {name} registered successfully.")

entered_name = input("Enter username to login: ")
entered_password = input("Enter password: ")

if entered_name in users and users[entered_name].login(entered_password):
    print("Login successful!")
    acc_number = input("Enter new account number: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    print(users[entered_name].create_account(acc_number, initial_deposit))
    
    while True:
        print("\n1. Check Balance\n2. Deposit Money\n3. Withdraw Money\n4. Mini Statement\n5. Exit")
        choice = input("Enter your choice: ")
        account = users[entered_name].accounts[0]  # Assuming single account per user

        if choice == "1":
            print(account.check_balance())
        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            print(account.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(amount))
        elif choice == "4":
            print("Mini Statement:")
            print(account.mini_statement())
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice. Try again.")
else:
    print("Invalid credentials. Login failed.")