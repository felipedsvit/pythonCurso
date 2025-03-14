import random

nombres = ["Maria", "Luis", "Lauren", "Jhon", "Aritz", "Helena", "Abdel", "Alfonso", "Markel", "Osama", "Iker", "Felipe","Kamila","Haizea", "Ilia"]
apellidos = ["Garcia", "Lopez", "Gonzalez", "Rodriguez", "Fernandez", "Sanchez", "Perez", "Martin", "Torres", "Gomez", "Vazquez", "Jimenez", "Ruiz", "Hernandez", "da Silva"]
nombres_completos = random.choice(nombres) + " " + random.choice(apellidos)
print(nombres_completos)