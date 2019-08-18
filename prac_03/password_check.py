"""
Sean
"""
MIN_LENGTH = 5
password = input("Enter new password: ")
while len(password) < MIN_LENGTH:
    password = input("Enter new password: ")
print(len(password) * "*")