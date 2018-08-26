# Basics of Python programing

# Numbers

a = 5 + 5
b = "5" + "6"
c = int("5") + int("6")

print(a)
print(b)
print(c)

# Strings

a = 'This is a String'
b = "Don't forget to use doble quaotes whrn using apostrofes"
c = 'And single quotes when "quoting"'
d = 'It can get worse... "Don\'t freak out"' # You will need to use scape ( \ ) some times...

print(a)
print(b)
print(c)
print(d)

# Basic String manipulation

a = "Hello " + "Christian"
b = "H" + "e" + "l" + "l" + "o"
c = "This costs " + str(6 + 3) + " bucks" # Numbers always have to be converted in strings to be concatenated (Casting?)
d = "Hello:Christian"

d.split(":")

print(a)
print(b)
print(c)
print(d)
print(d.split(":")) # El metodo split se usa para dividir texto. El parametro indica el lugar de la division
print("My name is " + d.split(":")[1]) # El indice se pone entre [], empezando de 0

# Booleans

a = True # Siempre la primera mayúscula...
b = "True" is True # Para que validara, habria que havcer "True" is str(True)
c = 5 is not 3
d = 5 == 5

print(a)
print(type(a))
print(b)
print("5 is not 3 : " + str(c))
print("5 == 5 : " + str(d))