name = input("how is your name : ")
print (name)

size_input = input("How big is your house (in sqare feet) : ")
square_feet = int (size_input)
square_metres = square_feet / 10.8
print (f"{square_feet} square feet is {square_metres:.3f} square metres.")

print (f"The house of : {name} have {square_metres:.3f} square metres")