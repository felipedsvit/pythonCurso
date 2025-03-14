""" 
frutas=["manzana","pera","naranja","banana","kiwi","fresas",""]
for fruta in frutas:
    print("Fruta: ",fruta)


while True: 
    num=int(input("Introduce un número: "))
    if num == 0:
        print("Correcto") 
        break
    else:
        print("Incorrecto")
        continue

while num:=int(input(" Introduce un número: ")) != 0:
    print(f" Has elegido el número {int(num)} \n Inténtalo de nuevo")
print("Has acertado")


#escribe numero de 1 a 10 que se detenga cuando se escriba 0
for i in range(1,11): 
    if i == 5:
        print("En el número 5 se detiene")
        break
    print(i)"
    """
for i in range(1,50): 
    if i == 12:
        print("En el número 12 se detiene")
        break
    print(i)