while True:
    pregunta = input("Digame algo bonito: ").lower()

    if ("hola" in pregunta) or ("kaixo" in pregunta):
        print("Hola, puedo ayudarte en lo que necesites")
    elif "python"  in pregunta:
        print("Python es un lenguaje increible")
    elif ("adios" in pregunta) or ("adiós" in pregunta) or ("agur" in pregunta):
        print("Adios, espero haberte ayudado")
        break
    else:
        print("No entiendo tu respuesta jovenzuelo")