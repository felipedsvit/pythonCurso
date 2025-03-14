#

#perro
pi1="  / \\__\n (    @\\___\n /         O\n/   (_____ /       "
pi2="\n/_____/   U\n"
color=input("¿Cuál es tu color favorito? ").strip().lower()

match color:
    case "rojo" | "verde" | "amarillo" | "naranja" | "azul" | "violeta" | "rosa" | "negro" | "blanco" :
        print(f"{pi1}El {color} es un color muy bonito.{pi2}")
    case _:
        print(pi1+"No tengo información sobre ese color o tu color es muy fea."+pi2)