#--------
print(" ")
print("--- ejemplo 1 ----")

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123)"),
    (2, "jose", "longp4ssword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

print (username_mapping)

#----NO genera ERROR pero es notacion mas complicada----
print(" ")
print("--- ejemplo 2 ----")

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123)"),
    (2, "jose", "longp4ssword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

print (username_mapping["Bob"])

#--------
print(" ")
print("--- ejemplo 3 ----")

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123)"),
    (2, "jose", "longp4ssword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input ("Enter your username: ")
password_input = input ("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print ("Your details are correct!")
else:
    print ("Your details are incorrect.")


