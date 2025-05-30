""" 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa 
función para calcular y mostrar en pantalla el factorial de todos los números enteros 
entre 1 y el número que indique el usuario """

def factorial_recursivo(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Args:
      n: El número para el cual se calculará el factorial.

    Returns:
      El factorial de n.
      Retorna 1 si n es 0 o 1.
      Retorna un mensaje de error si n es negativo.
    """
    if n < 0:
        return "No se permite calcular el factorial de números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        # Paso recursivo: n * (n-1)!
        return n * factorial_recursivo(n - 1)

# El siguiente bloque de código se ejecuta solo cuando el script se corre directamente.
if __name__ == "__main__":
    # Hago un bloque try-except para manejar posibles errores si el usuario
    # no ingresa un número entero.
    try:
        numero_limite = int(input("Ingrese un numero entero para calcular los factoriales: "))
        
        if numero_limite < 1:
            print("Error, por favor ingresa un numero entero mayor o igual a 1.")
        else:
            print(f"\nCálculo de factoriales desde 1 hasta {numero_limite}:\n")
            # Itero desde 1 hasta el número límite ingresado por el usuario (inclusive).
            for i in range(1, numero_limite + 1):
                resultado = factorial_recursivo(i)
                print(f"El factorial de {i} es: {resultado}")
    except ValueError: #  except tipo_de_error_especifico
        # Este mensaje se muestra si el usuario ingresa algo que no es un número entero (ej: letras).
        print("Entrada inválida. Ingresa un número entero.")
        # El programa no sé rompe y maneja el error de forma controlada - muestra un mensaje.


""" Caso Base (n == 0 or n == 1): Es la condición de salida. Sin un caso base, 
la función se llamaría a sí misma infinitamente (o hasta que se agote la memoria de 
la computadora, se conoce como "desbordamiento de pila" o "stack overflow").

Paso Recursivo (else: return n * factorial_recursivo(n - 1)): 
Es donde la función se llama a sí misma con una versión más pequeña del problema 
(n-1). Se acerca progresivamente al caso base. """

    



