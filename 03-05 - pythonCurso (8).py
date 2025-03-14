#variables
edad=int(input("¿Cuál es tu edad? "))
tieneMembresia=bool(input("Tienes membresia VIP? (sí/no)").lower())
tienePermiso= False

if edad >18: 
    tienePermiso=True
    
if edad <=18: 
    tienePermiso=bool(input("Tienes permiso de los padres? (sí/no)").lower())


if (edad >= 18 and tieneMembresia) or ( edad <= 16 and tienePermiso) :
    print("Tienes descuento ")
else:
    print("No cumplumple a los requisitos.")
