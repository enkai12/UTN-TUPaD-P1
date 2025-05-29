# Archivo: mis_funciones.py
# Este módulo contiene las funciones para cada actividad del tp n°5
import math

def imprimir_hola_mundo():
    """Actividad 1: Imprime 'Hola Mundo!'."""
    print("Hola Mundo!")

def crear_saludo_usuario(nombre):
    """Actividad 2: Devuelve un saludo personalizado."""
    # Verifica si el nombre está vacío o solo contiene espacios.
    if not nombre or nombre.strip() == "":
        return "Por favor, ingresa un nombre válido."
    return f"¡Hola {nombre}!"

def crear_informacion_personal(nombre, apellido, edad, residencia):
    """Actividad 3: Devuelve una cadena con información personal."""
    # Verifica que todos los campos tengan algún valor.
    # La función all() devuelve True si todos los elementos en la lista son verdaderos (no vacíos, no None, etc.).
    if not all([nombre, apellido, edad, residencia]): 
        return "Por favor, completa todos los campos de información personal."
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

def calcular_area_circulo(radio):
    """Actividad 4: Calcula el área de un círculo. Devuelve el área o un mensaje de error."""
    # El radio no puede ser un número negativo.
    if radio < 0:
        return "El radio no puede ser negativo."
    # Fórmula del área del círculo: pi * radio^2
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    """Actividad 4: Calcula el perímetro de un círculo. Devuelve el perímetro o un mensaje de error."""
    # El radio no puede ser un número negativo.
    if radio < 0:
        return "El radio no puede ser negativo."
    # Fórmula del perímetro del círculo: 2 * pi * radio
    return 2 * math.pi * radio

def segundos_a_horas(segundos):
    """Actividad 5: Convierte segundos a horas. Devuelve las horas o un mensaje de error."""
    # La cantidad de segundos no puede ser negativa.
    if segundos < 0:
        return "La cantidad de segundos no puede ser negativa."
    # Hay 3600 segundos en una hora.
    return segundos / 3600

def generar_tabla_multiplicar(numero):
    """Actividad 6: Imprime la tabla de multiplicar de un número del 1 al 10."""
    # Aunque la conversión a número se hace en main.py, esta es una verificación adicional.
    # isinstance verifica si 'numero' es de tipo entero (int) o decimal (float).
    if not isinstance(numero, (int, float)):
        print("Por favor, ingresa un número válido para la tabla.")
        return # Termina la función si el número no es válido.
    
    print(f"--- Tabla de Multiplicar del {numero} ---")
    # Un bucle 'for' que va desde 1 hasta 10 (inclusive).
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("------------------------------------")

def calcular_operaciones_basicas(a, b):
    """
    Actividad 7: Realiza suma, resta, multiplicación y división.
    Devuelve una tupla con los resultados: (suma, resta, multiplicacion, division_o_error).
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Manejo especial para la división: no se puede dividir por cero.
    if b == 0:
        division_o_error = "Error: División por cero no permitida."
    else:
        division_o_error = a / b
    return suma, resta, multiplicacion, division_o_error

def calcular_imc(peso_kg, altura_metros):
    """
    Actividad 8: Calcula el Índice de Masa Corporal (IMC).
    Devuelve el IMC redondeado a dos decimales o un mensaje de error.
    """
    # El peso y la altura deben ser valores positivos.
    if peso_kg <= 0 or altura_metros <= 0:
        return "El peso y la altura deben ser valores positivos."
    # Fórmula del IMC: peso / (altura^2)
    imc = peso_kg / (altura_metros ** 2)
    return round(imc, 2) # Redondea el resultado a dos decimales.

def celsius_a_fahrenheit(grados_celsius):
    """Actividad 9: Convierte grados Celsius a Fahrenheit."""
    # Fórmula de conversión: (Celsius * 9/5) + 32
    grados_fahrenheit = (grados_celsius * 9/5) + 32
    return round(grados_fahrenheit, 2) # Redondea el resultado a dos decimales.

def calcular_promedio_tres_numeros(num1, num2, num3):
    """Actividad 10: Calcula el promedio de tres números."""
    # Fórmula del promedio: (suma de los números) / (cantidad de números)
    return (num1 + num2 + num3) / 3

