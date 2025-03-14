#importaciones
import requests


#API
url="https://v2.jokeapi.dev/joke/Any?lang=es&blacklistFlags=religious,political,racist,sexist"
response=requests.get(url)

if response.status_code == 200:
    joke = response.json()
    if joke["type"] == "single":
        nombre = input("¿Cuál es tu nombre? ")
        apellido = input("¿Cuál es tu apellido? ")
        nombrecompleto=nombre+" "+apellido
        print(f"Hola {apellido [0]}, {nombre}, aquí tienes tu chiste:")


        print(f"\n {joke["joke"]}. jajaja")

        input(f"Que te pareció el chiste {nombrecompleto}? ")
        print("Gracias por participar.")
    else:
#Estudio
        nombre = input("¿Cuál es tu nombre? ")
        apellido = input("¿Cuál es tu apellido? ")
        nombrecompleto=nombre+" "+apellido
        print(f"Hola {apellido [0]}, {nombre}, aquí tengo un chiste:")

#Chisme
        print(f"\n{joke['setup']} - {joke['delivery']}. jajaja")

#Error
        input(f"Que te pareció el chiste {nombrecompleto}? ")
        print("Gracias por participar.")

else:
    print("Erro ao obter a piada.")
