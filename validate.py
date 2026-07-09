def validate_name(name):

    for ch in name:

        if not (ch.isalpha() or ch == " "):
            return False

    return True


def validate_age(age):

    if age >= 17 and age <= 30:
        return True

    return False


def validate_phone(phone):

    if len(phone) != 10:
        return False

    for digit in phone:

        if not digit.isdigit():
            return False

    return True


def validate_email(email):

    if "@" in email and "." in email:
        return True

    return False


print("===== Student Information =====")

name = input("Enter Name : ")

age = int(input("Enter Age : "))

phone = input("Enter Phone Number : ")

email = input("Enter Email : ")

if not validate_name(name):
    print("Invalid Name")

elif not validate_age(age):
    print("Invalid Age")

elif not validate_phone(phone):
    print("Invalid Phone Number")

elif not validate_email(email):
    print("Invalid Email")

else:

    print("\nStudent Details")
    print("Name :", name)
    print("Age :", age)
    print("Phone :", phone)
    print("Email :", email)