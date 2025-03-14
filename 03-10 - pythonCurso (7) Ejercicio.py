#Autores: Felipe, Camila, Iker
#Fecha: 2021/10/07
#Versión: 1.0
import random


#variables
pi1="  / \\__\n (    @\\___\n /         O\n/   (_____ /       "
pi2="\n/_____/   U\n"
nombres=["messi","cristiano","neymar","mbappe","james","zidane","ronaldinho"]
print(f"{pi1}¡Sea bienvenido el juego de adivinanza de futbol!",pi2," \n Tienes 3 oportunidades para adivinar el nombre del jugador de futbol. \n ¡Buena suerte!\n ")


#random
elegir=random.choice(nombres)

#Juego
match elegir:
    case "messi":
        if elegir==input(f"{pi1}Pista: Jugue en el Barcelona. Dime mi nombre: {pi2}").lower()=="messi":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Argentina. Dime mi nombre: {pi2}").lower()=="messi":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, ha ganado 8 balones de oro. Dime mi nombre: {pi2}").lower()=="messi":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Messi{pi2}")

    case "cristiano":
        if elegir==input(f"{pi1}Pista: Jugue en el Real Madrid. Dime mi nombre: {pi2}").lower()=="cristiano":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Portugal. Dime mi nombre: {pi2}").lower()=="cristiano":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, ha ganado 5 balones de oro. Dime mi nombre: {pi2}").lower()=="cristiano":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Cristiano{pi2}")
    case "neymar":
        if elegir==input(f"{pi1}Pista: Jugue en el Barcelona. Dime mi nombre: {pi2}").lower()=="neymar":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Brasileño. Dime mi nombre: {pi2}").lower()=="neymar":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, ha ganado 0 balones de oro. Dime mi nombre: {pi2}").lower()=="neymar":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Neymar{pi2}")
    case "mbappe"| "kylian":
        if elegir==input(f"{pi1}Pista: Jugue en el PSG. Dime mi nombre: {pi2}").lower()=="mbappe":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Francia. Dime mi nombre: {pi2}").lower()=="mbappe":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, ha ganado 0 balones de oro. Dime mi nombre: {pi2}").lower()=="mbappe":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Mbappe{pi2}")
    case "haaland":
        if elegir==input(f"{pi1}Pista: Jugue en el Dourtmont. Dime mi nombre: {pi2}").lower()=="haaland":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Noruega. Dime mi nombre: {pi2}").lower()=="haaland":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, ha ganado 0 balones de oro. Dime mi nombre: {pi2}").lower()=="haaland":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Haalan{pi2}")
    case "james":
        if elegir==input(f"{pi1}Pista: Jugue en el Everton. Dime mi nombre: {pi2}").lower()=="james":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Colombia. Dime mi nombre: {pi2}").lower()=="james":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, ha ganado 0 balones de oro. \n Dime mi nombre: {pi2}").lower()=="james":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy James Rodriguez{pi2}")


    case "zidane":
        if elegir==input(f"{pi1}Pista: Jugé en el Real Madrid. Dime mi nombre: {pi2}").lower()=="zidane":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Francia. Dime mi nombre: {pi2}").lower()=="zidane":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Ultima oportunidad, He ganado la Copa del Mundo. \n Dime mi nombre: {pi2}").lower()=="zidane":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Zidane{pi2}")

    case "ronaldinho":
        if elegir==input(f"{pi1}Pista: Jugé en el Barcelona. Dime mi nombre: {pi2}").lower()=="zidane":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! Soy de Brasil. Dime mi nombre: {pi2}").lower()=="zidane":
            print(f"{pi1}¡Correcto!{pi2}")
        elif elegir==input(f"{pi1}¡No! He ganado 2 balones de oro., He ganado la Copa del Mundo. \n Dime mi nombre: {pi2}").lower()=="zidane":
            print(f"{pi1}¡Correcto!{pi2}")
        else:
            print(f"{pi1}Perdiste! Yo soy Ronaldinho{pi2}")
