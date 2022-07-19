#--------
print(" ")
print("--- ejemplo 1 ----")

def add(x, y=8):
    print(x + y)

add(5)

#----Genera error porque la function tiene definido un parametro default si y otro NO----
print(" ")
print("--- ejemplo 2 ----")

#def add(x=5, y):
#    print(x + y)

add(15)

#--------
print(" ")
print("--- ejemplo 3 ----")

def add(x=5, y=3):
    print(x + y)

add(x=15, y=12)

#----Genera error porque la function tiene definido un parametro default si y otro NO----
print(" ")
print("--- ejemplo 4 ----")

#def add(x=5, y):
#    print(x + y)

#add(x=15, 12)

#--------
print(" ")
print("--- ejemplo 5 ----")

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print (sum)

add (2)

#-------NO por tener una nueva variable default y asignarla se cambia el resultado-
print(" ")
print("--- ejemplo 6 ----")

default_y = 3

def add(x, y=default_y):
    sum = x + y
    print (sum)

add (2)

default_y = 4
add (2)    
