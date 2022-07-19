l = ["Bob", "Rolf", "Anne"]
t = ("Bob-t", "Rolf-t", "Anne-t")
s = {"Bob-s", "Rolf-s", "Anne-s"}

print (l[0])
print (l[2])

print (t[1])
print (t[2])

l[0] = "Smith"
print (l)

l.append("Smith")
print (l)

l.remove("Smith")
print (l)

s.add ("Smith")
print (s)

s.remove("Bob-s")
print (s)

my_tuple = ("1")
print (my_tuple)