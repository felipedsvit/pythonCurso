numeros=[10,20,30,40]
total=sum(numeros)
print(total)

numeros2=[1,2,3]
total2=sum (numeros2,10)
print(total2)

total3=sum(range(1,6))
print(total3)

cuadrado=sum([x**2 for x in range(1,6)])
print(cuadrado)

palabras=["Hola","Mundo","!"]
#print(sum(palabras))
print(" ".join(palabras))

ventas={"enero":1000, "febrero":1200, "marzo":1100}
total_ventas=sum(ventas.values())
print(total_ventas,ventas.values())

calificaciones=[80,90,78,92,88]
promedio=sum(calificaciones)/len(calificaciones)
print(f"El promedio de calificaciones es {promedio:.2f}")