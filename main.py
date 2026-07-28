import re

print("Please enter a password")
password = input()

if (len(password) >= 8
    and re.search("[a-z]", password)
    and re.search("[A-Z]", password)
    and re.search("[0-9]", password)
    and re.search("[_@$]", password)
    and not re.search("\s", password)):
    print("Good Password")
else:
    print("Please make password stronger")