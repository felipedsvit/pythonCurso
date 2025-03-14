#variables
teorico=input("¿Aprobaste el examen teórico? (sí/no): ")
practico=input("¿Aprobaste el examen práctico? (sí/no): ")
mecanico=input("¿Aprobaste el examen mecanico? (sí/no): ")

#
if teorico == "si" or teorico == "sí" or teorico == "S" or teorico == "bai" or teorico == "y" :
    if practico == "si" or practico == "sí" or practico == "S" or practico == "bai" or practico == "y" :
        if mecanico== "si" or mecanico== "sí" or mecanico== "S" or mecanico== "bai" or mecanico== "y" :
            print("Has conseguido tu carnet de viajero espacial.")
        else:
            print("Debe aprobar el examen mecánico para obtener tu liciencia")
    else:
        print("Debe aprobar el examen práctico para obtener tu liciencia")
else:
    print("Debe aprobar el examen teórico para obtener tu liciencia")