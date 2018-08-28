
check = "Hamburguer"

if check == False: # La igualdad se comprueba con dos =
    print("It is False")
elif check == "Hamburguer": # elif eqivale a else ... if, un nivel mas de comprobación
    print("I love Hamburguers")
elif check == "Yo":
    print("Hello!")
else: # Es el valor por defecto si no se cumple ninguna de las condiciones anteriores
    print("It is True")

numbers = ["Nick", "Christian", "Joel"]

for item in numbers: # El segundo parametro es la lista, y el primero como llamamos al elemento que iteramos
    print("This person name is", item)

run = True
current = 1

while run: # Un while funciona hasta que la condcion deja de cumplirse
    if current == 100:
        run = False # Tiene que haber una forma de cambiar la condicion dentreo del While, claro...
    else:
        print(current)
        current += 1