from datetime import datetime    
now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
name=input("enter your Name:")
print("\n=====hi"+ " " + name +" " + "Welcome to the ATM =====\n")
print("access D/T : " + now)

def show_menu():
    """Displays the ATM menu options."""
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    print("====================")
    

def check_balance(balance):
    """Displays the current balance."""
    print(f"\nYour current balance is: ${balance:.2f}")

def deposit(balance):
    """Allows the user to deposit money."""
    amount = float(input("Enter the amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"\n${amount:.2f} deposited successfully!")
    else:
        print("\nInvalid amount! Please enter a positive number.")
    return balance  

def withdraw(balance):
    """Allows the user to withdraw money if enough balance is available."""
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("\nInsufficient balance! Cannot withdraw.")
    elif amount <= 0:
        print("\nInvalid amount! Please enter a positive number.")
    else:
        balance -= amount
        print(f"\n${amount:.2f} withdrawn successfully!")
    return balance 

def atm():
    balance = 1000.00  
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)  # Update balance after deposit
        elif choice == "3":
            balance = withdraw(balance)  # Update balance after withdrawal
        elif choice == "4":
            print("\nThank you for using the ATM! Goodbye. 😊")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 4.")

# Run the ATM program
atm()
