import mis_funciones as mf # Importamos el módulo donde están las funciones de los ejercicios

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    Cada opción corresponde a un ejercicio diferente.
    """
    print("\n--- Menú de Ejercicios ---")
    print("1. Actividad 1: Hola Mundo")
    print("2. Actividad 2: Saludo Personalizado")
    print("3. Actividad 3: Información Personal")
    print("4. Actividad 4: Área y Perímetro de un Círculo")
    print("5. Actividad 5: Segundos a Horas")
    print("6. Actividad 6: Tabla de Multiplicar")
    print("7. Actividad 7: Operaciones Básicas")
    print("8. Actividad 8: Cálculo de IMC")
    print("9. Actividad 9: Celsius a Fahrenheit")
    print("10. Actividad 10: Promedio de Tres Números")
    print("0. Salir del programa")
    print("---------------------------")

def ejecutar_actividad_1():
    # Consigna: Crear una función llamada imprimir_hola_mundo que imprima 
    # por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde 
    # el programa principal.
    print("\n--- Actividad 1: Hola Mundo ---")
    # Llamamos a la función 'imprimir_hola_mundo' que se encuentra en nuestro módulo 'mf'.
    # Esta función simplemente imprimirá "Hola Mundo!" en la pantalla.
    mf.imprimir_hola_mundo()

def ejecutar_actividad_2():
    # Consigna: Crear una función llamada saludar_usuario(nombre) que reciba
    # como parámetro un nombre y devuelva un saludo personalizado.
    # Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
    # “Hola Marcos!”. Llamar a esta función desde el programa principal
    # solicitando el nombre al usuario.
    print("\n--- Actividad 2: Saludo Personalizado ---")
    # Solicitamos al usuario que ingrese su nombre.
    # La función input() pausa el programa y espera que el usuario escriba algo y presione Enter.
    # Lo que el usuario escribe se guarda como texto (string) en la variable 'nombre_ingresado_usuario'.
    nombre_ingresado_usuario = input("Por favor, ingresa tu nombre: ")
    
    # Llamamos a la función 'crear_saludo_usuario' del módulo 'mf'.
    # Le pasamos el nombre que el usuario ingresó.
    # Esta función devuelve un texto con el saludo personalizado.
    mensaje_saludo_creado = mf.crear_saludo_usuario(nombre_ingresado_usuario)
    
    # Mostramos el saludo personalizado en la pantalla.
    print(mensaje_saludo_creado)

def ejecutar_actividad_3():
    # Consigna: Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) 
    # que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años 
    # y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función 
    # con los valores ingresados.
    # Nota: En mis_funciones.py se modificó para que DEVUELVA la cadena.
    print("\n--- Actividad 3: Información Personal ---")
    # Solicitamos al usuario varios datos personales.
    nombre_ingresado = input("Ingresa tu nombre: ")
    apellido_ingresado = input("Ingresa tu apellido: ")
    edad_ingresada = input("Ingresa tu edad: ") # La edad se pide como texto inicialmente.
    lugar_residencia_ingresado = input("Ingresa tu lugar de residencia: ")
    
    # Llamamos a la función 'crear_informacion_personal' del módulo 'mf'.
    # Le pasamos todos los datos que el usuario ingresó.
    # Esta función devuelve una cadena de texto formateada con la información personal.
    cadena_informacion_creada = mf.crear_informacion_personal(
        nombre_ingresado, 
        apellido_ingresado, 
        edad_ingresada, 
        lugar_residencia_ingresado
    )
    # Mostramos la información personal en la pantalla.
    print(cadena_informacion_creada)

def ejecutar_actividad_4():
    # Consigna: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
    # como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
    # que reciba el radio como parámetro y devuelva el perímetro del círculo. 
    # Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
    print("\n--- Actividad 4: Área y Perímetro de un Círculo ---")
    # Solicitamos al usuario el radio del círculo.
    # Ofrecemos la opción de escribir 's' para omitir esta actividad.
    radio_circulo_texto = input("Ingresa el radio del círculo (o 's' para saltar): ")
    
    # Verificamos si el usuario quiere omitir la actividad.
    if radio_circulo_texto.lower() == 's':
        print("Actividad 4 omitida.")
        return # Termina la ejecución de esta función.
    
    # Convertimos el radio ingresado (que es texto) a un número decimal (float).
    # Si el usuario ingresa un texto que no es un número válido (y no es 's'),
    # el programa se detendrá aquí con un error (ValueError).
    radio_circulo_numero = float(radio_circulo_texto) 
    
    # Calculamos el área llamando a la función 'calcular_area_circulo' del módulo 'mf'.
    area_calculada_circulo = mf.calcular_area_circulo(radio_circulo_numero)
    # Verificamos si la función devolvió un mensaje de error (texto) o un número.
    if isinstance(area_calculada_circulo, str): 
        print(area_calculada_circulo) # Mostramos el mensaje de error.
    else:
        # Si es un número, lo mostramos formateado a dos decimales.
        print(f"El área del círculo es: {area_calculada_circulo:.2f}")

    # Calculamos el perímetro llamando a la función 'calcular_perimetro_circulo' del módulo 'mf'.
    perimetro_calculado_circulo = mf.calcular_perimetro_circulo(radio_circulo_numero)
    # Verificamos si la función devolvió un mensaje de error (texto) o un número.
    if isinstance(perimetro_calculado_circulo, str): 
        print(perimetro_calculado_circulo) # Mostramos el mensaje de error.
    else:
        # Si es un número, lo mostramos formateado a dos decimales.
        print(f"El perímetro del círculo es: {perimetro_calculado_circulo:.2f}")

def ejecutar_actividad_5():
    # Consigna: Crear una función llamada segundos_a_horas(segundos) que reciba una 
    # cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
    # Solicitar al usuario los segundos y mostrar el resultado usando esta función.
    print("\n--- Actividad 5: Segundos a Horas ---")
    # Solicitamos al usuario una cantidad de segundos.
    segundos_ingresados_texto = input("Ingresa la cantidad de segundos (o 's' para saltar): ")
    
    if segundos_ingresados_texto.lower() == 's':
        print("Actividad 5 omitida.")
        return
        
    # Convertimos los segundos ingresados (texto) a un número entero (int).
    # Si el usuario ingresa un texto que no es un número entero válido,
    # el programa se detendrá con un error (ValueError).
    segundos_ingresados_numero = int(segundos_ingresados_texto) 
    
    # Llamamos a la función 'segundos_a_horas' para realizar la conversión.
    horas_calculadas = mf.segundos_a_horas(segundos_ingresados_numero)
    # Verificamos si la función devolvió un error (texto) o el resultado numérico.
    if isinstance(horas_calculadas, str):
        print(horas_calculadas)
    else:
        # Mostramos el resultado de la conversión, formateado a dos decimales.
        print(f"{segundos_ingresados_numero} segundos equivalen a {horas_calculadas:.2f} hora/s.")

def ejecutar_actividad_6():
    # Consigna: Crear una función llamada tabla_multiplicar(numero) que reciba un 
    # número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
    # Pedir al usuario el número y llamar a la función.
    print("\n--- Actividad 6: Tabla de Multiplicar ---")
    # Solicitamos al usuario un número para generar su tabla de multiplicar.
    numero_tabla_texto = input("Ingresa un número para ver su tabla de multiplicar (o 's' para saltar): ")
    
    if numero_tabla_texto.lower() == 's':
        print("Actividad 6 omitida.")
        return

    # Convertimos el número ingresado (texto) a un número entero (int).
    # Si no es un número entero válido, el programa fallará.
    numero_para_tabla = int(numero_tabla_texto) 
    
    # Llamamos a la función 'generar_tabla_multiplicar'.
    # Esta función no devuelve un valor, sino que imprime la tabla directamente.
    mf.generar_tabla_multiplicar(numero_para_tabla)

def ejecutar_actividad_7():
    # Consigna: Crear una función llamada operaciones_basicas(a, b) que reciba dos 
    # números como parámetros y devuelva una tupla con el resultado de sumarlos, 
    # restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
    print("\n--- Actividad 7: Operaciones Básicas ---")

    # Solicitar el primer número al usuario como texto.
    # Se ofrece la opción de ingresar 's' para omitir la actividad.
    primer_numero_texto = input("Ingresa el primer número para las operaciones (o 's' para saltar): ")
    
    # Verificar si el usuario desea omitir la actividad.
    if primer_numero_texto.lower() == 's':
        print("Actividad 7 omitida.")
        return # Termina la ejecución de esta función si se omite.

    # Solicitar el segundo número al usuario como texto.
    segundo_numero_texto = input("Ingresa el segundo número para las operaciones: ")
    
    # Convertir las entradas de texto a números de punto flotante (decimales).
    # Si se ingresa un texto que no puede convertirse a número
    # (por ejemplo, "hola"), el programa se detendrá con un error (ValueError).
    numero_1 = float(primer_numero_texto) 
    numero_2 = float(segundo_numero_texto) 
    
    # Llamar a la función 'calcular_operaciones_basicas' del módulo 'mf' (mis_funciones).
    # Esta función toma los dos números y devuelve una tupla con cuatro resultados:
    # (resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division)
    tupla_resultados_operaciones = mf.calcular_operaciones_basicas(numero_1, numero_2)
    
    # Desempaquetar la tupla: asignar cada elemento de la tupla a una variable individual.
    # El orden es importante y debe coincidir con el orden en que la función devuelve los valores.
    resultado_suma, resultado_resta, resultado_multiplicacion, resultado_division = tupla_resultados_operaciones
    
    # Mostrar los resultados de las operaciones.
    print(f"Suma: {resultado_suma}")
    print(f"Resta: {resultado_resta}")
    print(f"Multiplicación: {resultado_multiplicacion}")

    # Manejo especial para el resultado de la división:
    # La función 'calcular_operaciones_basicas' puede devolver un mensaje de error (texto/string)
    # si se intenta dividir por cero.
    # 'isinstance(variable, tipo)' isinstance(): Esta es una función incorporada de Python que revisa si una variable es de un tipo de dato específico.
    if isinstance(resultado_division, str): 
        # Si resultado_division es un string (texto), significa que es un mensaje de error.
        print(f"División: {resultado_division}")
    else:
        # Si no es un string, es un número (el resultado de la división).
        # Se formatea para mostrarlo con dos decimales usando :.2f
        print(f"División: {resultado_division:.2f}")


def ejecutar_actividad_8():
    # Consigna: Crear una función llamada calcular_imc(peso, altura) que reciba el 
    # peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
    # Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
    print("\n--- Actividad 8: Cálculo de IMC ---")
    # Solicitamos el peso al usuario.
    peso_usuario_texto = input("Ingresa tu peso en kg (ej: 70.5) (o 's' para saltar): ")
    if peso_usuario_texto.lower() == 's':
        print("Actividad 8 omitida.")
        return
    # Solicitamos la altura al usuario.
    altura_usuario_texto = input("Ingresa tu altura en metros (ej: 1.75): ")

    # Convertimos el peso y la altura a números decimales.
    # Si se ingresa texto no numérico, el programa fallará.
    peso_usuario_numero = float(peso_usuario_texto) 
    altura_usuario_numero = float(altura_usuario_texto) 
    
    # Llamamos a la función 'calcular_imc' para obtener el Índice de Masa Corporal.
    imc_final_calculado = mf.calcular_imc(peso_usuario_numero, altura_usuario_numero)
    # Verificamos si el resultado es un mensaje de error (texto) o el valor del IMC.
    if isinstance(imc_final_calculado, str):
        print(imc_final_calculado)
    else:
        # Mostramos el IMC calculado.
        print(f"Tu Índice de Masa Corporal (IMC) es: {imc_final_calculado}")

def ejecutar_actividad_9():
    # Consigna: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba 
    # una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
    # Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
    print("\n--- Actividad 9: Celsius a Fahrenheit ---")
    # Solicitamos la temperatura en grados Celsius.
    grados_celsius_texto = input("Ingresa la temperatura en grados Celsius (o 's' para saltar): ")
    if grados_celsius_texto.lower() == 's':
        print("Actividad 9 omitida.")
        return
        
    # Convertimos la temperatura ingresada a un número decimal.
    # Si no es un número válido, el programa fallará.
    grados_celsius_numero = float(grados_celsius_texto) 
    
    # Llamamos a la función 'celsius_a_fahrenheit' para la conversión.
    grados_fahrenheit_convertidos = mf.celsius_a_fahrenheit(grados_celsius_numero)
    # Mostramos el resultado de la conversión.
    print(f"{grados_celsius_numero}°C equivalen a {grados_fahrenheit_convertidos}°F.")

def ejecutar_actividad_10():
    # Consigna: Crear una función llamada calcular_promedio(a, b, c) que reciba 
    # tres números como parámetros y devuelva el promedio de ellos. 
    # Solicitar los números al usuario y mostrar el resultado usando esta función.
    # Nota: En mis_funciones.py se llama calcular_promedio_tres_numeros.
    print("\n--- Actividad 10: Promedio de Tres Números ---")
    # Solicitamos el primer número para el promedio.
    primer_numero_promedio_texto = input("Ingresa el primer número para el promedio (o 's' para saltar): ")
    if primer_numero_promedio_texto.lower() == 's':
        print("Actividad 10 omitida.")
        return
    # Solicitamos los otros dos números.
    segundo_numero_promedio_texto = input("Ingresa el segundo número para el promedio: ")
    tercer_numero_promedio_texto = input("Ingresa el tercer número para el promedio: ")

    # Convertimos los tres números ingresados a números decimales.
    # Si alguno no es un número válido, el programa fallará.
    primer_numero_promedio = float(primer_numero_promedio_texto) 
    segundo_numero_promedio = float(segundo_numero_promedio_texto) 
    tercer_numero_promedio = float(tercer_numero_promedio_texto) 
    
    # Llamamos a la función 'calcular_promedio_tres_numeros' para obtener el promedio.
    promedio_final_calculado = mf.calcular_promedio_tres_numeros(
        primer_numero_promedio, 
        segundo_numero_promedio, 
        tercer_numero_promedio
    )
    # Mostramos el promedio calculado, formateado a dos decimales.
    print(f"El promedio de {primer_numero_promedio}, {segundo_numero_promedio} y {tercer_numero_promedio} es: {promedio_final_calculado:.2f}")


def programa_principal():
    """
    Función principal que gestiona el menú y la ejecución de actividades.
    Esta función se ejecuta en un bucle hasta que el usuario decide salir.
    """
    print("--- ¡Bienvenido a la Resolución de Ejercicios de Funciones! ---")
    
    # Bucle infinito que mantiene el programa corriendo hasta que el usuario elija salir.
    while True:
        mostrar_menu() # Mostramos las opciones disponibles.
        # Solicitamos al usuario que elija una opción del menú.
        opcion_elegida = input("Selecciona una actividad (número) o '0' para salir: ")

        # Verificamos la opción elegida por el usuario y ejecutamos la actividad correspondiente.
        if opcion_elegida == '1':
            ejecutar_actividad_1()
        elif opcion_elegida == '2':
            ejecutar_actividad_2()
        elif opcion_elegida == '3':
            ejecutar_actividad_3()
        elif opcion_elegida == '4':
            ejecutar_actividad_4()
        elif opcion_elegida == '5':
            ejecutar_actividad_5()
        elif opcion_elegida == '6':
            ejecutar_actividad_6()
        elif opcion_elegida == '7':
            ejecutar_actividad_7()
        elif opcion_elegida == '8':
            ejecutar_actividad_8()
        elif opcion_elegida == '9':
            ejecutar_actividad_9()
        elif opcion_elegida == '10':
            ejecutar_actividad_10()
        elif opcion_elegida == '0':
            # Si el usuario elige '0', mostramos un mensaje de despedida y salimos del bucle (y del programa).
            print("\n--- ¡Gracias por usar el programa! Saliendo... ---")
            break # 'break' rompe el bucle while y termina el programa.
        else:
            # Si la opción no es válida, informamos al usuario.
            print("\nOpción no válida. Por favor, elige un número del menú.")
        
        # Pausa para que el usuario pueda leer el resultado de la actividad antes de volver al menú.
        input("\nPresiona Enter para continuar al menú...")

if __name__ == "__main__":
    programa_principal() # Llamamos a la función principal para iniciar el programa.
