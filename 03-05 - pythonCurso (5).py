#variables
nombre=input("Ingresa tu nombre ")
edad=int(input("Ingresa tu edad "))
tiene_carnet=input("¿Tienes carnet de conducir? (sí/no) ").lower() == "sí"

#código
print(f"Nombre: {nombre} (Tipo: {type(edad)})")
print(f"Edad: {edad} (Tipo: {type(edad)})")
print(f"Tiene carnet: {tiene_carnet} (Tipo: {type(tiene_carnet)})")
