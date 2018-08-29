import re

# Una calculadora que hace algunas cosas interesantes

# Definir funciones

print("Nuestra calculadora mágica")
print("Escribe 'quit' para salir\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))
    if equation == "quit":
        print("Goodbye Human")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation) # Eliminamos lo que no nos interesa, para que nadie ejecute codigo en la fucion

        if previous == 0:
            previous = eval(equation) # Eval evalua la operacion antes de presentarla
        else:
            previous = eval(str(previous) + equation)
        # print("You typed", previous)

while run:
    perform_math()