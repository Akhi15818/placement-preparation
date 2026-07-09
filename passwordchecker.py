password = input("Enter Password : ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:

    if ch.isupper():
        upper += 1

    elif ch.islower():
        lower += 1

    elif ch.isdigit():
        digit += 1

    else:
        special += 1

if len(password) < 8:

    print("Weak Password")

elif upper > 0 and lower > 0 and digit > 0 and special > 0:

    print("Strong Password")

else:

    print("Medium Password")