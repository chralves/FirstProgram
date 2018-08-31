'''
    Progama: La Calculadora Mágica
    Autor: Christian Alves - Copiado de Nick G
    Copyright: 2018

'''

import re

# Definir funciones

print("Nuestra calculadora mágica")
print("Escribe 'quit' para salir\n")

previous = 0
run = True

def perform_math():
    global run
    global previous
    equation = ""

    # Si existe algun cáculo anterior, usalo...
    if previous == 0:
        equation = input("Enter equation: ")
    else:
        equation = input(str(previous))

    # Si el usuario sale del programa ->
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