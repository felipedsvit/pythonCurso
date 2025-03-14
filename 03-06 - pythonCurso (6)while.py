contador = 0

while contador < 10:
    contador += 1
    if contador %2 == 0:
        print(f"El numero {contador} es par.")        
        continue
    print(f"El numero {contador} es impar.")