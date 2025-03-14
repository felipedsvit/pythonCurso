import random

# Variables
jugadores = {
    1: "messi",
    2: "cristiano",
    3: "neymar",
    4: "mbappe",
    5: "haaland",
    6: "james"
}

# Función para jugar
def adivinar_jugador(jugador):
    pistas = {
        "messi": [
            ("Jugé en el Barcelona.", "messi"),
            ("Soy de Argentina.", "messi"),
            ("He ganado 8 balones de oro.", "messi"),
        ],
        "cristiano": [
            ("Jugé en el Real Madrid.", "cristiano"),
            ("Soy de Portugal.", "cristiano"),
            ("He ganado 5 balones de oro.", "cristiano"),
        ],
        "neymar": [
            ("Jugé en el Barcelona.", "neymar"),
            ("Soy de Brasil.", "neymar"),
            ("He ganado 0 balones de oro.", "neymar"),
        ],
        "mbappe": [
            ("Jugé en el PSG.", "mbappe"),
            ("Soy de Francia.", "mbappe"),
            ("He ganado 0 balones de oro.", "mbappe"),
        ],
        "haaland": [
            ("Jugé en el Dortmund.", "haaland"),
            ("Soy de Noruega.", "haaland"),
            ("He ganado 0 balones de oro.", "haaland"),
        ],
        "james": [
            ("Jugé en el Everton.", "james"),
            ("Soy de Colombia.", "james"),
            ("He ganado 0 balones de oro.", "james"),
        ]
    }
    
    for pista, respuesta in pistas[jugador]:
        if input(f"Pista: {pista} \n\nDime mi nombre: ").lower() == respuesta:
            print("¡Correcto!")
            return True
        print("¡No! Intentémoslo de nuevo.")
    
    print(f"Perdiste! Yo soy {jugador.capitalize()}")
    return False

# Juego principal
print("¡Sea bienvenido al juego de adivinanza de fútbol!")
print("Tienes 3 oportunidades para adivinar el nombre del jugador de fútbol.")
print("¡Buena suerte!\n")
print("Estos son los jugadores disponibles:")
print("1. Messi")
print("2. Cristiano Ronaldo")
print("3. Neymar")
print("4. Mbappé")
print("5. Haaland")
print("6. James Rodríguez")

# Selecciona un jugador aleatorio
jugador_numero = random.choice(list(jugadores.keys()))
jugador_seleccionado = jugadores[jugador_numero]

# Llama a la función para empezar el juego
adivinar_jugador(jugador_seleccionado)
