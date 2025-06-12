""" 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición 
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario 
especifique. """

def fibonacci_recursivo(posicion):
    """
    Calcular el valor de la serie Fibonacci en una
    posición dada usando recursividad.
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
    Muestra la serie de Fibonacci completa, de forma iterativa.
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
        
# Programa principal
if __name__ == "__main__": # este bloque solo se ejecuta cuando el archvio es el programa principal
    try:
        # pide al usuario que ingrese un numero
        posicion_usuario = int(input("Ingresa un numero y te mostrare la serie de Fibonacci que quieras ver: "))
        
        # 1: Calculo en la funcion recursiva
        valor_en_posicion = fibonacci_recursivo(posicion_usuario)
        print(f"\nEl valor en posicion {posicion_usuario} es: {valor_en_posicion}")
        
        # 2: Muestro la serie con la funcion iterativa
        mostrar_serie_fibo(posicion_usuario)
        
        # se captura el error en este bloque try-except
    except ValueError:
        print("Ingresa un numero entero!!")