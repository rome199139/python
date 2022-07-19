friends = {"Bob", "Rolf", "Anne"}
print ("Anne" in friends)

movies_watched = {"The Matrix", "Green Book", "Her"}
user_movie = input("Enter something you've watched recently: ")

print (user_movie in movies_watched)


user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")