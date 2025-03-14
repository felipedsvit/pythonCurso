respuesta = input("¿Desea continuar? (sí/no): ").strip().lower()

opcionSi = ["si", "sí", "s", "bai", "y"]
opcionNo = ["no", "n", "ez", "nope", "nop"]

if respuesta in opcionSi:
    print("has elegido continuar.")
elif respuesta in opcionNo:
    print("has elegido salir de la fiesta o no. ;-)")
else:
    print("Entrada   no válida")