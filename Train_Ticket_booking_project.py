# --------------------- PROJECT : RAILWAY TICKET BOOKING -----------------------
import random

class Train():
    def __init__(self, train_num, source, destination, seats, coach_types):
        self.train_num = train_num
        self.source = source
        self.destination = destination
        self.seats = seats  # Total seats in train
        self.coach_types = coach_types  # Dictionary of available coaches
        
        # Berth allocation system
        self.berths = {
            "Lower": seats // 5,
            "Middle": seats // 5,
            "Upper": seats // 5,
            "Side Lower": seats // 10,
            "Side Upper": seats // 10
        }

    def display_info(self):
        print(f"Train Number: {self.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Available Seats: {self.seats}")
        print(f"Coaches Available: {', '.join(self.coach_types)}")
        print("Berth Availability:", self.berths)
        print()

    def book_tickets(self, num_tickets, berth_preferences):
        if num_tickets > self.seats:
            return None  # Not enough seats available

        pnr_list = []
        allocated_berths = []
        allocated_coaches = []

        for i in range(num_tickets):
            preferred_berth = berth_preferences[i]
            
            # Assign berth based on preference or fallback to available berth
            if self.berths.get(preferred_berth, 0) > 0:
                berth = preferred_berth
            else:
                berth = next((b for b in self.berths if self.berths[b] > 0), None)
            
            if berth is None:  # No berths available
                return None  

            # Allocate a coach randomly from available types
            coach = random.choice(self.coach_types)

            # Reduce available seats
            self.seats -= 1
            self.berths[berth] -= 1

            # Generate PNR
            pnr = random.randint(100000, 999999)
            pnr_list.append(pnr)
            allocated_berths.append(berth)
            allocated_coaches.append(coach)

        return pnr_list, allocated_berths, allocated_coaches


class Passenger:
    def __init__(self, name, age, gender, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Phone Number: {self.phone}")

class Ticket:
    def __init__(self, train, source, destination, passengers, pnr, berth, coach):
        self.train = train
        self.source = source
        self.destination = destination
        self.passengers = passengers
        self.pnr = pnr
        self.berth = berth
        self.coach = coach

    def display_info(self):
        print(f"Train Number: {self.train.train_num}")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"PNR: {self.pnr}")
        print(f"Coach: {self.coach}")
        print(f"Berth: {self.berth}")
        for passenger in self.passengers:
            passenger.display_info()
        print()

class Account:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password


# Class called Account is defined with a constructor that takes two arguments: username and password. These arguments are used to initialize instance variables with the same names. The class also defines a method called check_password which takes a single argument password and returns a boolean indicating whether the input password matches the stored password.

accounts = [
    Account("user1", "password1"),
    Account("user2", "password2")
]

# A list called accounts is initialized with two Account objects already in it, with the usernames "user1" and "user2" and passwords "password1" and "password2" respectively.

logged_in_account = None
# A variable called logged_in_account is initialized to None. This variable will be used later to keep track of the currently logged-in account.

while True:  # A while loop is started that will run indefinitely until the user logs in successfully and is presented with the available train details.
    print("\n1. Create an account\n2. Login\n")
    choice = input("Enter choice: ")
    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        accounts.append(Account(username, password))
# If the user chooses to create an account (choice == "1"), they are prompted to enter a username and password. The inputted username and password are then used to create a new Account object, which is appended to the accounts list.
        print("Account created successfully!")
# Inside the loop, the user is presented with two options: either to create an account or to login. The user's choice is stored in a variable called choice.
    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for account in accounts:
            if account.username == username and account.check_password(password):
                logged_in_account = account
                break
        if logged_in_account is None:
            print("Invalid username or password.")
# If the user chooses to login (choice == "2"), they are prompted to enter a username and password. The program then iterates through the accounts list and checks if any of the stored accounts match the inputted username and password. If a match is found, the corresponding Account object is assigned to the logged_in_account variable and the loop is broken. Otherwise, an error message is printed.
        else:
            print(
                f"\nLogged in as {logged_in_account.username}\n\n-----Availabe Train details-----\n")

            break
    else:
        print("Invalid choice.")

if logged_in_account is not None:
    trains = [
        Train("12737", "Tadepalligudem", "Secunderabad", 40, ["Sleeper", "AC", "General"]),
        Train("12728", "Tadepalligudem", "Visakhapatnam", 50, ["Sleeper", "AC"]),
        Train("22863", "Vijayawada", "Bangalore", 1, ["General"]),
        
    ]

# --- User Booking Process ---
for train in trains:
    train.display_info()

# User selects a train
while True:
    train_num = input("Enter Train Number: ")
    num_tickets = int(input("Enter Number of Tickets: "))
    if num_tickets <= 0:
        print("Number of tickets must be greater than 0")
        continue

    train = next((t for t in trains if t.train_num == train_num), None)
    if train:
        break
    else:
        print("Invalid Train Number.")

# --- Passenger Details & Berth Selection ---
passengers = []
berth_preferences = []
for i in range(num_tickets):
    print(f"\nEnter details for Passenger {i + 1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    gender = input("Gender: ")
    phone = input("Phone Number: ")

    passenger = Passenger(name, age, gender, phone)
    passengers.append(passenger)

    # Ask for berth preference
    print("Available Berths: Lower, Middle, Upper, Side Lower, Side Upper")
    berth_pref = input("Enter Preferred Berth: ")
    berth_preferences.append(berth_pref)

# --- Book Tickets ---
pnr_data = train.book_tickets(num_tickets, berth_preferences)
if pnr_data is None:
    print("Tickets not available.")
else:
    pnr_list, allocated_berths, allocated_coaches = pnr_data

    print("\n--------------Booking Successful!------------\n")
    for i in range(num_tickets):
        ticket = Ticket(train, train.source, train.destination, 
                        [passengers[i]], pnr_list[i], allocated_berths[i], allocated_coaches[i])
        ticket.display_info()

    print("\n--------Thank You------- \n-------Safe Journey------")
















