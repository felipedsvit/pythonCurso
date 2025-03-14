frase="Aprender Python es increible"
palavras=frase.split()
print(palavras)
print(len(palavras))
print(len(frase))

#len es una función que devuelve la longitud de un objeto iterable, como una lista, una tupla, un conjunto, una cadena, etc.
#.split() es un método que divide una cadena en una lista. Por defecto, divide la cadena por espacios en blanco.

frase2=" ".join(palavras)
print(frase2)