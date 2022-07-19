#--------
print(" ")
print("--- ejemplo 1 ----")

def multiply(*args):
    print(args)

multiply(1, 3, 5)


#-------
print(" ")
print("--- ejemplo 2 ----")

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total    

print(multiply(1, 3, 5))


#--------
print(" ")
print("--- ejemplo 3 ----")

def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total    

print(multiply(-1))

#--------
print(" ")
print("--- ejemplo 4 ----")

def add(x, y):
    return x + y

nums = [3, 5]   
print (add(*nums))

#--------
print(" ")
print("--- ejemplo 5 ----")

def add(x, y):
    return x + y

nums = [3, 5]   
print (add(x=3, y=5))

#--------
print(" ")
print("--- ejemplo 6 ----")

def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}
print (add(x=nums["x"], y=nums["y"]))

#--------simplificando-----
print(" ")
print("--- ejemplo 7 ----")

def add(x, y):
    return x + y

nums = {"x": 15, "y": 25}
print (add(**nums))

#--------
print(" ")
print("--- ejemplo 8 ----")

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)    
    else:
        return "No valid operator provided  to apply()"    

print (apply(1, 3, 6, 7,  operator="+"))        

#--------Devuelve es una tupla y no la * ----
print(" ")
print("--- ejemplo 9 ----")

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)    
    else:
        return "No valid operator provided  to apply()"    

print (apply(1, 3, 6, 7,  operator="*"))       

#--------se envian *args en multiply ----
print(" ")
print("--- ejemplo 10 ----")

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)    
    else:
        return "No valid operator provided  to apply()"    

print (apply(1, 3, 6, 7,  operator="*"))       


