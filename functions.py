

def my_function(): # Las funciones se definen en "snake_case", "CamelCase" es para clases. No necesitamos {, sólo:
    print("This is my Function")
    print("A second string")

def second_function(str1, str2):
    print(str1)
    print(str2)

def print_something (name, age):
    print("My name is " + name + " and my age is " + str(age)) # No podemos concatenar un numero directo, hay que hacer casting...
    print("My name is", name, "and my age is", age) # Una alternativa es usar comas en vez de concatenar

def print_something2 (name = "Someone", age = "Unknown"): # Asignando las variables, las atribuimos por defecto...
    print("My name is " + name + " and my age is " + str(age))
    print("My name is", name, "and my age is", age)

my_function()

second_function("Hello", "Christian")
second_function("The same function", "Different arguments")

print_something("Chistian", 34)

print_something2() # Sin variables, imprime por defecto lo que hayamos atribuido... y no molesta diciendo que faltan variables

print_something2("Christian") # Si sólo pasamos un argumento, coge el primero...