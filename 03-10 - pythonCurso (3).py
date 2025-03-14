"""
edad=int(input("Introduce tu edad: "))
if (edad) < 12:
    print("Eres un niño")
elif (edad >=13 and edad <=16):
    print("Eres un adolescente")
elif (int(edad) >= 18 and int(edad) <= 67):
    print("Eres un adulto")
elif int(edad) >= 68:
    print("Eres jubilado")
"""
edad=int(input("Introduce tu edad: "))
match edad:
    case _ if edad < 12: print("Eres un niño")
    case  _ if 13 <= edad <= 16: print("Eres un adolescente")
    case  _ if 18 <= edad <= 67: print("Eres un adulto")
    case  _ if edad >= 68: print("Eres jubilado")

