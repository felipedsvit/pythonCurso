edad=int(input("Ingrese su edad ")) #variable
if edad >= 18 and edad < 24: #condicional
    print("Eres mayor de edad.")

elif edad >= 25 and edad < 30:#condicial 2
    print("Tienes que ir a la universidad.")

elif edad >= 13 and edad < 18:#condicial 2
    print("Soy menor de edad.")

elif edad >= 30 and edad < 40:#condicial 3
    print("Tienes que irte a la trabajar.")    
elif edad >40:#condicial 4
    print("INSS te espera.")
else:#condicional restante
    print("Soy niño, se me hablas tonterias te vás a la cárcer.")
