estudiante={}

for _ in range(3):  #agregamos 3 estudiantes
    nombre=input("Introduce el nombre del estudiante: ")
    edad=int(input("Ingresa la edad: "))
    carrera=input("Cuentame que estudios tienes: ")
    estudiante[nombre]={"edad":edad,"carrera":carrera}
print(f"\ndiccionario de estudiantes \n{estudiante}")   