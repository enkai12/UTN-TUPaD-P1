""" 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:

a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla 
"""

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a)
compras[2].append("jugo")
print(compras)

# b)
compras[1][1] = "tallarines"
print(compras)

# c)
compras[0].remove("pan")
print(compras)

# d)
print(f"\nLista final de compras: \n{compras}")
