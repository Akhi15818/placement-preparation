balance = 5000

while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Choose: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Deposit Amount: "))
        balance += amount
        print("Updated Balance =", balance)

    elif choice == 3:
        amount = float(input("Withdraw Amount: "))
        if amount <= balance:
            balance -= amount
            print("Updated Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == 4:
        break

    else:
        print("Invalid Choice")