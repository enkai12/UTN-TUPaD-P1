""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” 
por dos nuevos valores. """

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "chevrolet"

autos[2] = "audi"

print(autos)

# otra forma, atraves de indexing

elementos = ["blanco", "verde", "azul", "amarillo"]

nuevos_elementos = ["negro", "marron"]

# reemplazo desde el indice 1 al 2. valores centrales

elementos[1:3] = nuevos_elementos 

print(elementos)