import re

def validate_name(name):
    return name.replace(" ", "").isalpha()

def validate_age(age):
    return age.isdigit() and 10 <= int(age) <= 50

def validate_mobile(mobile):
    return mobile.isdigit() and len(mobile) == 10

def validate_email(email):
    pattern =r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def validate_username(username):
    return len(username) >= 5

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[@%^$*()_+=-]", password):
        return False
    return True

print("----- Student Registration Form -----")

name = input("Enter Name: ")
if not validate_name(name):
    print("Error: Name should contain only alphabets.")
    exit()

age = input("Enter Age: ")
if not validate_age(age):
    print("Error: Age must be between 10 and 50.")
    exit()

mobile = input("Enter Mobile Number: ")
if not validate_mobile(mobile):
    print("Error: Mobile number must be 10 digits.")
    exit()

email = input("Enter Email: ")
if not validate_email(email):
    print("Error: Invalid email format.")
    exit()

username = input("Enter Username: ")
if not validate_username(username):
    print("Error: Username must be at least 5 characters long.")
    exit()

password = input("Enter Password: ")
if not validate_password(password):
    print("Error: Password must be strong.")
    exit()

print("\nRegistration Completed Successfully!")
