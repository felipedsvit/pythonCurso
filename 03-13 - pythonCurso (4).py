#Lista de telefonica
lista={}
while True:
    i = int(input("\n\nElige:\n 1 - Insetar un contacto. \n 2 - Elimine un contacto. \n 3 - Mire un contacto. \n 4 - Salir.  \n Eliges: "))
    match i:
        case 1:#Pone el nombre
            nombre=input("\n\nIntroduce tu nombre: ").lower()
            numero=input("Introduce tu numero: ")
            lista[nombre]=int(numero)
            print(f"Has introducido el contacto {nombre} del numero {numero} en su lista telefónica\n\n")
            continue
        case 2:#quita el nombre
            eliminarContacto = input("\n\nCual contacto desea de eliminar: ").lower()
            if eliminarContacto in lista:
                del lista[eliminarContacto]
                print(f"Has eliminado el contacto: {eliminarContacto}")
            else:
                print("No hay este contacto en su lista telefónica")        
        case 3:#busque
            verContacto = input("Cual contacto desea ver: ").lower()
            if verContacto in lista:
                print(f"Contacto \nNombre: {verContacto},numero: {numero}  \n")

            else:
                print("Estudiante no encontrado.\n\n")
        case 4:#salir
            print("Saliendo...")
            break
        case _:#error de opción
            print("Opción invalida")