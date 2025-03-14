

while True:
    elige=int(input("Menu: \n 1. - Iniciar pedido \n 2. - Detener \n 3. - Salir \n Eliges tu opicion: "))
    match elige:
        case 1:
            print("Iniciando pedido")
            break
        case 2:
            print("Deteniendo pedido")
            break
        case 3:
            print("Saliendo de la hamburgueria")
            continue
        case _:
            print("Opcion no valida")
            continue
   