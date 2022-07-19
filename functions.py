#--------
print(" ")
print("--- ejemplo 1 ----")

def Hello():
    print("hello too!")

Hello()

#--------
print(" ")
print("--- ejemplo 2 ----")

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}.")

user_age_in_seconds()

#--------
print(" ")
print("--- ejemplo 3 ----")

print("Welcome to the age in minutes program!")
def user_age_in_minutes():
    user_age = int(input("Enter your age: "))
    age_minutes = user_age * 365 * 24 * 60
    print(f"Your age in minutes is {age_minutes}.")
user_age_in_minutes()
print("Goodbye!")

#--------
print(" ")
print("--- ejemplo 4 ----")

friends = ["Bob","Rolf"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    #friends = friends + [friend_name]
    f = friends + [friend_name]
    print(f)

add_friend()
print(friends)

#--------
print(" ")
print("--- ejemplo 5 ----")

friends = []

def add_friend():
    friends.append("Rolf")
    
add_friend()
add_friend()
add_friend()

print(friends)  # Rolf



    
