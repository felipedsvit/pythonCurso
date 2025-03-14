muyLista =[]
a=input("ingrese un valor: ")
b=input("ingrese un valor: ")
c=input("ingrese un valor: ")
d=input("ingrese un valor: ")
e=input("ingrese un valor: ")
muyLista.append(a)
muyLista.append(b)
muyLista.append(c)
muyLista.append(d)
muyLista.append(e)
print(muyLista)
muyLista.pop(muyLista.index(c)) #muestra el indice de la variable c
print(muyLista)
muyLista.remove(e) #remueve la variable e
print(muyLista)