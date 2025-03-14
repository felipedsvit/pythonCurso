#bienvenido
print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       BANCO PERRITO GASTEIZ ¡Bienvenido a nuestro banco digital!\n/_____/   U\n")
#variables
nombre=input("¿Cual es tu nombre? ")

#bienvenido
print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       ¡Hola! Mr."+ (nombre) +"\n/_____/   U\n")

#variables
edad = int(input("Ingresa tu edad: "))
sueldo=int(input("Ingresa tu sueldo: $"))
aval=0
antCrim=input("¿Estas sin antecedentes? ").lower() == "sí"

#condicionales
if sueldo <= 2000:
    aval=int(input("¿Cuanto ganas tu avalista?: $"))

if edad > 21:
    mayorEdad=True
else:
    mayorEdad=False

if sueldo > 2000 or aval > 3000:
    fin=True
else:
    fin=False
#teste
print(antCrim)
print(type(antCrim))
#resultado
if mayorEdad and antCrim and fin:

    print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       Enhorabuena, su prestamo fue CONCEDIDO Mr."+ (nombre) +"\n/_____/   U\n")

else:
  print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       Lamentamos, su prestamo fue  DENEGADO Mr."+ (nombre) +"\n/_____/   U\n")
