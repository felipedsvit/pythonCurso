suEdad = int(input("Dame tu edad, baby: "))
esMayor = suEdad >= 18

if esMayor:
    print("¿Es mayor de edad? Sí, soy mayor de edad.")
elif suEdad > 13:
    print("¿Es mayor de edad? No, soy menor de edad")
else:
    print("¿Es mayor de edad? Pregunta a mi amigo Pol Licía.")
