# 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]

numeros.remove(max(numeros))

print(numeros)

# la funcion max() lo que hace es retornar el elemento más grande.
# Por lo tanto, fucionada con el méotod remove() lo que va a hacer es eliminar el elemento
# más grande de la lista.

# Resultado
# numeros = [8, 15, 3, 7]
