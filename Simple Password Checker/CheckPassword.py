import re

''' a valid password has >= 8 chars and can contain any letters, 
numbers, and/or $%#@ and ends with a number
'''

print("Check if your password is valid.")
passwordInput = input("Please enter a password: ")

psswdPattern = re.compile(r"(^[a-zA-Z0-9$%#@]{8,}[0-9]$)")

def checkValidity(password, pattern):
    if pattern.search(passwordInput) is not None:
        print("Password is valid!")
    else:
        print("Password is invalid.")

checkValidity(passwordInput, psswdPattern)