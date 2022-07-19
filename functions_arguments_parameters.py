#--------
print(" ")
print("--- ejemplo 1 ----")

def add(x, y):
    result = x + y
    print(result)

add(5, 3)

#----Genera error porque la function no tiene definido un parametro----
print(" ")
print("--- ejemplo 2 ----")

def say_hello():
    print("Hello")

#say_hello("Bob")

#--------
print(" ")
print("--- ejemplo 3 ----")

def say_hello(name):
    print(f"Hello {name}")

say_hello("Bob")

#----Genera error porque la function tiene un parametro y no se pasa ninguno----
print(" ")
print("--- ejemplo 4 ----")

def say_hello(name):
    print(f"Hello {name}")

#say_hello()

#--------
print(" ")
print("--- ejemplo 5 ----")

def say_hello(name, surname):
    print(f"Hello,  {name} {surname}")

say_hello(surname="Bob", name="Smith")

#--------
print(" ")
print("--- ejemplo 6 ----")

def divide(dividend, divisor):
    if  divisor != 0:
        print (dividend / divisor)
    else:
        print ("you fool!")    

divide(dividend=15, divisor=0)
    
