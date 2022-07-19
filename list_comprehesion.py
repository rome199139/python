#--------
numbers = [1, 3, 5]
double = [num * 2 for num in numbers]

print(double)

#--------
friends = ["Rolf","Sam","Samantha","Saurabh","Jen"]
starst_s = []

for friend in friends:
    if friend.startswith("S"):
        starst_s.append(friend)

print(starst_s)        

#--------
friends = ["Rolf","Sam","Samantha","Saurabh","Jen"]
starst_s = [friend for friend in friends if friend.startswith ("S")]

print(starst_s)        

#--------
friends = ["Sam1","Samantha1","Saurabh1"]
starst_s = [friend for friend in friends if friend.startswith ("S")]

print(friends)
print(starst_s)
print(friends is starst_s)
print("friends: ", id(friends), "starts_s: ", id(starst_s))

#--------
friends = ["Sam1","Samantha1","Saurabh1"]
starst_s = friends

print(friends)
print(starst_s)
print(friends is starst_s)
print("friends: ", id(friends), "starts_s: ", id(starst_s))

