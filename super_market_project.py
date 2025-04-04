


''' ########### generate a bill for a supermarket purchase #################### '''

from datetime import datetime    
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
while True: #it keep on asking to enter the customer name
    # Store available items with prices in a list of tuples
    products = [
        ("Apples", 2.50),
        ("Milk", 1.20),
        ("Bread", 1.00),
        ("Eggs", 3.00),
        ("Rice", 5.50)
        ]

# Store purchased items (as a list of tuples: name, quantity, total price)
    cart = []
    name=input("enter customer Name:")
    print("\n=====hi"+ " " + name +" " + "Welcome to the Supermarket =====")
# Display available products with option numbers
    print("Select items by entering the option number:\n")
    for index, (item, price) in enumerate(products, start=1):
        print(f"Option {index}: {item} - ${price:.2f}")

# User selects items
    while True:
        option = input("\nEnter the option number (or type '0' to finish): ").strip()

        if option == "0":
            break  # Exit when user is done

        if not option.isdigit():  # Validate input before converting
            print("Invalid input! Please enter a valid number.")
            continue

        option = int(option) - 1  # Convert to index

        if 0 <= option < len(products):  # Check if option is valid
            item, price = products[option]

            while True:
                quantity = input(f"Enter quantity for {item}: ").strip()
                if not quantity.isdigit():
                    print("Invalid quantity! Please enter a valid number.")
                    continue

                quantity = int(quantity)
                if quantity > 0:
                    total_price = price * quantity
                    cart.append((item, quantity, total_price))
                    break
                else:
                    print("Quantity must be greater than 0.")

        else:
            print("Invalid option! Please select a valid number.")

# Print the final bill in a proper bill format
    print("\n" + "="*40)
    print("              Supermarket Bill")
    print("="*40)
    print(f"{'Item':<15}{'Qty':<5}{'Price':>8}")
    print("-"*40)

    total_cost = 0
    for item, quantity, total_price in cart:
        print(f"{item:<15}{quantity:<5}${total_price:>8.2f}")
        total_cost += total_price

    print("-"*40)
    print(f"{'Total':<20}${total_cost:>8.2f}")
    print("="*40)
    print("customer name : " + name )
    print("billing D/T : " + now)
    print("\n Thank you for shopping with us! 😊")
    restart = input("Would you like to process another customer? (yes/no): ").strip().lower()
    if restart != "yes":
        print("\n👋 Have a great day! Goodbye!\n")
        break  # Exit loop if user enters anything other than 'yes'
