#--------
print(" ")
print("--- ejemplo 1 ----")

add = lambda x, y: x + y
    
print (add(5, 7))

#----NO genera ERROR pero es notacion mas complicada----
print(" ")
print("--- ejemplo 2 ----")

print ((lambda x, y: x + y)(8, 9))

#--------
print(" ")
print("--- ejemplo 3 ----")

def double (x):
    return x * 2

sequence = [1, 3, 5, 9]
doubled = [double (x) for x in sequence]
#doubled = map(double, sequence)
print (doubled)

#----Otra forma de hacerlo----
print(" ")
print("--- ejemplo 4 ----")

sequence = [1, 3, 5, 9]
#doubled1 = [(lambda x: x * 2) (x) for x in sequence]
doubled1 = map(lambda x: x * 2, sequence)
print (doubled1)

#--------
print(" ")
print("--- ejemplo 5 ----")

sequence = [1, 3, 5, 9]
#doubled1 = [(lambda x: x * 2) (x) for x in sequence]
doubled1 = list(map(lambda x: x * 2, sequence))
print (doubled1)

#-------NO combinar return diferentes tipos (int, sprint) porque puede devolver cosas ilogicas-----
print(" ")
print("--- ejemplo 6 ----")

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!."

result = divide (15, 0) * 5
print (result)
