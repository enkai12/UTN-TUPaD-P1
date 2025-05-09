# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

# Usamos range(start, stop, step) comenzando en 4, hasta 101 (porque 101 no se incluye), de 4 en 4

multiplos_de_4 = list(range(4, 101, 4))

# Mostramos la lista completa
print(f"Lista de múltiplos de 4 del 1 al 100: {multiplos_de_4}")
