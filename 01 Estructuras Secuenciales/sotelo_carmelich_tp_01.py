# Actividad III - Estructuras Secuenciales

"""  Funciónes	Descripción
print()	        Muestra un mensaje en pantalla.
input()	        Solicita una entrada del usuario.
int()	        Convierte un valor a número entero.
float()	        Convierte un valor a número decimal.
math.pi	        Representa el valor de π.
**	            Operador de potencia (exponente).
range(1, 11)	Genera una secuencia de números del 1 al 10.

for	Estructura de repetición para recorrer valores. """

# 1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".
print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima un saludo con el nombre ingresado.
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida nombre, apellido, edad y lugar de residencia e imprima una oración con los datos ingresados.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4) Crear un programa que pida el radio de un círculo e imprima su área y su perímetro.
# f-string (f"texto {valor:.2f}")
# :2f convierte el valor flotante a dos decimales en python.
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

# 5) Crear un programa que pida una cantidad de segundos e imprima a cuántas horas equivale.
segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas:.2f} horas.")

# 6) Crear un programa que pida un número e imprima su tabla de multiplicar.
numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Crear un programa que pida dos números enteros distintos de 0 y muestre la suma, división, multiplicación y resta.
n1 = int(input("Ingrese el primer número (distinto de 0): "))
n2 = int(input("Ingrese el segundo número (distinto de 0): "))
print(f"Suma: {n1 + n2}, Resta: {n1 - n2}, Multiplicación: {n1 * n2}, División: {n1 / n2:.2f}")

# 8) Crear un programa que pida la altura y el peso e imprima el índice de masa corporal (IMC).
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es {imc:.2f}")

# 9) Crear un programa que convierta una temperatura en grados Celsius a Fahrenheit.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"Equivalente en Fahrenheit: {fahrenheit:.2f}")

# 10) Crear un programa que pida 3 números e imprima su promedio.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio es {promedio:.2f}")