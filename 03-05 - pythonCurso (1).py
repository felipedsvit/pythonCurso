#Declarar variables
nombreCompleto=input("¿Cuál es tu nombre completo?  ")
nickName=input("¿Escribe su Apodo?  ")
motto=input("¿Qué le gusta hacer?  ")
numeroTelefono=int(input("¿Cuál es tú telefono?  "))
coche=bool(input("¿Tienes coche?  "))

#Imprime cada tipo de variable
print(f"\n Hola, {nombreCompleto}, el tipo de variable es {type(nombreCompleto)}.\n su apodo es {nickName}, el tipo de variable es {type(nickName)}.\n que le gusta hacer {motto}, el tipo de variable es {type(motto)}. \n su telefono es {numeroTelefono}, el tipo de variable es {type(numeroTelefono)}.\n Tú tienes coche {coche}, el tipo de variable es {type(coche)}.")
