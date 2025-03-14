#variables
msgPerro="¡Bienvenido a nuestro programa de Python!"

#bienvenido
print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       "+ msgPerro +"\n/_____/   U\n")

edad=int(input("Introduce tu edad: "))

if edad>=18 :
    msgPerro="Ya eres adultos, puedes acceder a nuestro programa avançado."
    print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       "+ msgPerro +"\n/_____/   U\n")
elif edad <13 :
    msgPerro="Ya eres niño, puedes acceder a nuestro programa basico."
    print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       "+ msgPerro +"\n/_____/   U\n")
elif edad>=13 and edad<18 :
    msgPerro="Ya eres adolecente, puedes acceder a nuestro programa intermedio."
    print("  / \\__\n (    @\\___\n /         O\n/   (_____ /       "+ msgPerro +"\n/_____/   U\n")