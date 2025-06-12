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
        muestro la serie completa hasta la posicion especificada
        """
        
        print(f"Serie de Fibonacci hasta la posicion {hasta_posicion}:")
        
        for i in range(hasta_posicion + 1):
            print(fibonacci_recursivo(i)), end=" ")
        print()