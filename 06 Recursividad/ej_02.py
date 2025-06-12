""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique. """

def fibonacci_recursivo(posicion):
    """
    Calcular el valor de la serie Fibonacci en una
    posición dada usando recursividad
    """
    
    # Caso base:
    if posicion <= 1:
        return posicion
    # llamada recursiva
    else:
        return fibonacci_recursivo(posicion - 1) + fibonacci_recursivo(posicion - 2)
    
    
    # para ser mas eficiente muestro la serie con una funcion iterativa
    
    def mostrar_serie_fibo(hasta_posicion):
        """
        mejoro la muestra de forma iterativa para que sea mas eficiente
        """
        
    # valido que el numero no sea negativo
    if hasta_posicion < 0:
        print("Ingresa un numero positivo")
        return
    
    print(f"Serie de fibonacci hasta la posicion {hasta_posicion}:")
    a, b = 0, 1
    for _ in range(hasta_posicion + 1):
        print(a, end = " ")
        a, b = b, a + b             # forma de generar la serie
    print()                         # salto de linea
        
        