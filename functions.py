

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

def print_people(*people): # Usamos un asterisco antes del argumentos para declarar un array (list). Argumentos infinitos
    for person in people:
        print("This person is", person)

def do_math(num1, num2):
    return num1 + num2

my_function()

second_function("Hello", "Christian")
second_function("The same function", "Different arguments")

print_something("Chistian", 34)

print_something2() # Sin variables, imprime por defecto lo que hayamos atribuido... y no molesta diciendo que faltan variables

print_something2("Christian") # Si sólo pasamos un argumento, coge el primero.

print_something2(age = 34) # Para pasar el segundo argumento, usamos "Keywords"

print_something2(age = 34, name = "Christian") # Incluso podemos pasar los argumentos en otro orden...

print_people("Christian", "Joel", "Dámaris", "Lydia")

do_math(5, 10) # Claro que si hacemos esto no hace nada...

math1 = do_math(5, 7)
math2 = do_math(11, 13)

print("First sum is", math1, "and the second sum is", math2) # Si lo asignamos a una variable, podemos imprimir...
