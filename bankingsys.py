balance = 0


def deposit():

    global balance

    amount = float(input("Enter amount to deposit: "))

    if amount > 0:
        balance += amount
        print("Amount Deposited Successfully.")
    else:
        print("Invalid Amount")


def withdraw():

    global balance

    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid Amount")

    elif amount > balance:
        print("Insufficient Balance")

    else:
        balance -= amount
        print("Please collect your cash.")


def check_balance():

    print("Available Balance :", balance)


def menu():

    while True:

        print("\n========== PYTHON BANK ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":
            deposit()

        elif choice == "2":
            withdraw()

        elif choice == "3":
            check_balance()

        elif choice == "4":
            print("Thank You for Banking.")
            break

        else:
            print("Invalid Choice")


menu()