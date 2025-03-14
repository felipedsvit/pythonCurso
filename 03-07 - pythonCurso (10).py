muyLista =[]
a=input("ingrese un nombre: ")
b=input("ingrese un nombre: ")
c=input("ingrese un nombre: ")
d=input("ingrese un nombre: ")
e=input("ingrese un nombre: ")
muyLista.append(a)
muyLista.append(b)
muyLista.append(c)
muyLista.append(d)
muyLista.append(e)

for i in muyLista:
    if i == c:
        muyLista.remove(c)
    print(i)
