#importaciones
import datetime
import requests 


#perro
pi1="  / \\__\n (    @\\___\n /         O\n/   (_____ /       "
pi2="\n/_____/   U\n"


# Hora
hora= datetime.datetime.now().strftime("%H:%M")


#API tiempo
API_KEY = '067514e1a297419ab0f131218250603'
CITY = 'Vitoria-Gasteiz'
url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&lang=es'
response = requests.get(url)

if response.status_code == 200:
    datos = response.json()
else:
        print('Error en la petición')
        exit()

temperatura = datos['current']['temp_c']
descripcion = datos['current']['condition']['text']


# Menu
while True:
    elige=int(input("Menu: \n 1. - ¿Quieres sabe que horas son? \n 2. - ¿Quieres saber el clima? \n 3. - Salir \n Eliges tu opicion: "))
    match elige:
        case 1:
            print(pi1+"Ahorita es exatamente: "+hora+pi2)
            break
        case 2:
            print(f"{pi1}El tiempo en {CITY} es {temperatura} ºC ({descripcion}) {pi2}")
            break
        case 3:
            print(pi1+"Saliendo"+pi2)
            break
        case _:
            print(pi1+"¡Opción no es válida!"+pi2)
            continue
#fin
# Las horas lo saque de Copilate(me pedió para importar datetime, que tiene la funccion datetime.now())
#
#https://www.weatherapi.com/my/ (felipedsvit@gmail.com)
# Para la API de tiempo, me pedio importar requests(tubo que instalarlo con pip install requests)
# importando el requests pudo hacer la peticion a la API de tiempo
# crié una variable API_KEY con la clave de la API de tiempo
# crié una variable CITY con la ciudad
# crié una variable url con la url de la API de tiempo
# crié una variable response con la peticion de la url
# si la respuesta es 200, crié una variable datos con la respuesta en formato json
# si no, imprimi un mensaje de error
# crié una variable temperatura con la temperatura actual
# crié una variable descripcion con la descripcion del tiempo actual
#
# Entonces impecé el menu con un bucle while    
#
#
