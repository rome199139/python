number = 7

while True:
    user_input = input("Would you like to play (Y/n) ")

    if user_input == 'n':
        break
    
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    #elif number - user_number in (1, -1):    
    elif abs(number - user_number) == 1:
        print("You were off by one")   
    else:
        print("Sorry, it's wrong!")   


friends = ["Bob", "Rolf", "Jen", "Anne"]

print(f"{friends[0]} is my friend.")
print(f"{friends[1]} is my friend.")
print(f"{friends[2]} is my friend.")
print(f"{friends[3]} is my friend.")

#for friend in friends:
for friend in range (4):    
    print (f"{friend} is my friend too!.")

grades = [35, 67, 98, 100, 100]   
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print (total / amount)   

grades = [135, 167, 198, 1100, 1100]   
total = sum(grades)
amount = len(grades)

print (total / amount)   

