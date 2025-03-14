respuesta = input("¿Desea continuar? (sí/no): ").strip().lower()
match respuesta:
    case "si" | "sí" | "s" | "bai" | "y":
        print("has elegido continuar.")
    case "no" | "n" | "ez" | "nope" | "nop":
        print("has elegido salir de la fiesta o no. ;-)")
    case _:
        print("Entrada no válida. Escriba 'sí' o 'no'.")