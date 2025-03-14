#Tirar el promedio de notas de 3 estudiantes
estudiantes = {}

while True:
    i = int(input("Elige:\n 1 - Inserir estudiantes. \n 2 - Busque el alumno. \n 3 - Salir. \n Eliges: "))

    match i:
        case 1:
            for _ in range(1, 4):
                nombre = input("Dame el nombre del estudiante: ").lower()
                nota1 = int(input("Introduce la nota bimensual 1/4: "))
                nota2 = int(input("Introduce la nota bimensual 2/4: "))
                nota3 = int(input("Introduce la nota bimensual 3/4: "))
                nota4 = int(input("Introduce la nota bimensual 4/4: "))
                print("\n")
                promedio = sum([nota1, nota2, nota3, nota4]) / 4 
                estudiantes[nombre] = {
                    "nota1": nota1,
                    "nota2": nota2,
                    "nota3": nota3,
                    "nota4": nota4,
                    "promedio": promedio
                }
        case 2:
            estudianteBuscado = input("Ingresa el nombre del estudiante que deseas consultar: ").lower()
            if estudianteBuscado in estudiantes:
                print(f"Nombre: {estudianteBuscado} \nPromedio: {estudiantes[estudianteBuscado]['promedio']}\n")
            else:
                print("Estudiante no encontrado.")
        case 3:
            print("Saliendo del programa.")
            break  

        case _:
            print("Opción inválida. Intenta nuevamente.")
