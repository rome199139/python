#--------
print(" ")
print("--- ejemplo 1 ----")

def add(x, y):
    print(x + y)

add(5, 8)
result = add(5, 8)
print (result)

#----NO genera ERROR pero no genera nada----
print(" ")
print("--- ejemplo 2 ----")

def add(x, y):
    return x + y

add(5, 8)

#--------
print(" ")
print("--- ejemplo 3 ----")

def add(x, y):
    return x + y

add(5, 8)
result = add(5, 8)
print (result)

#----Otra forma de hacerlo----
print(" ")
print("--- ejemplo 4 ----")

def add(x, y):
    print (x + y) 

print (add(5, 8))

#--------
print(" ")
print("--- ejemplo 5 ----")

def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!."

result = divide (15, 3)
print (result)

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
