# Autor: Felipe da Silva
# Versión: 0.2
# Fecha: 05/03/2025~06/03/2025
# Descripción: Este programa solicita al usuario que ingrese su nombre, edad, sueldo y aval, y luego imprime un perro ASCII.

#asistente
pi1="  / \\__\n (    @\\___\n /         O\n/   (_____ /       "
pi2="\n/_____/   U\n"

#mensaje de bienvenida
print(pi1+"BANCO PERRITO GASTEIZ¡Bienvenido!"+pi2)

#nombre
name=input("Ingrese su nombre: ")
print(pi1+"Bienvenido a nuestro banco Mr. "+ name +pi2)

#preguntas
edad=int(input("Ingrese su edad: "))
sueldo=float(input("Ingrese su sueldo: $"))
antCrim=input("Tienes antecedentes criminales: ").lower() == "sí"
eval=0

#Si se necesita aval
if sueldo < 2000: aval=float(input("Ingrese el aval: $"))
else: aval=0

#Se es mayor de Edad
if edad > 21: mayorEdad=True
else: mayorEdad=False

#Se tienes condiciones financera
if sueldo > 2000 or aval > 3000 : financiero=True
else: financiero=False

#Respuesta de la solicitud
if mayorEdad and financiero and (not antCrim): print(pi1+"Mr. "+ name +", su prestamo fue APROVADO."+pi2)
else: print(pi1+"Mr. "+ name +", su prestamo fue DENEGADO."+pi2)
#fin