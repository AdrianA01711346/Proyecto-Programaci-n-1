import time

# variables globales
racha_dormir = 0
racha_ejercicio = 0

#Matriz historial
matriz_historial = []

# Lista de rangos
RANGOS = [(30, "Líder"), (14, "Maestro"), (7, "Contendiente"), (1, "Promesa")]


# Obtener Rango
def obtener_rango(racha):
    for dias, rango in RANGOS:
        if racha >= dias:
            return f"Tu Rango Actual: {rango}"
    return "Tu Rango Actual: Sin Rango"

#......................................................

# Contador de horas dormidas
def contador_horas_dormidas(horas):
    contador_dormir = 0
    while contador_dormir < horas:
        time.sleep(0.2)
        contador_dormir += 1
        print(f"Has dormido: {contador_dormir} horas")
    return contador_dormir

#......................................................

# Contador de ejercicio
def contador_minutos_ejercicio(minutos):
    contador_ejercicio = 0
    while contador_ejercicio < minutos:
        time.sleep(0.02)
        contador_ejercicio += 1
        print(f"Minutos de ejercicio completados: {contador_ejercicio}")
    return contador_ejercicio

#......................................................

# Bucle menu principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Dormir 8 Horas")
    print("2. Ejercicio Semanal")
    print("3. Registro de Hábitos")
    print("4. Ver Racha Actual")
    print("5. Salir")

    opcion = input("Escoge una opción (1-5): ")

    #Proceso dormir 8 horas
    if opcion == "1":
        when = input("¿Quieres empezar tu ciclo de sueño? (si/no): ").lower()
        if when == "si":
            horas_logradas = contador_horas_dormidas(8)

            nueva_fila = [horas_logradas, 0]
            matriz_historial.append(nueva_fila)

            racha_dormir += 1

            print(
                f"\n¡Registro guardado! Racha actual de sueño: {racha_dormir} días."
            )
            print(obtener_rango(racha_dormir))

    #Proceso ejercicio
    elif opcion == "2":
        minutos_meta = int(input("¿Cuántos minutos vas a hacer? (45-120): "))
        if 45 <= minutos_meta <= 120:
            when = input("¿Quieres empezar tu ejercicio? (si/no): ").lower()
            if when == "si":
                mins_logrados = contador_minutos_ejercicio(minutos_meta)

                nueva_fila = [0, mins_logrados]
                matriz_historial.append(nueva_fila)

                racha_ejercicio += 1

                print(
                    f"\n¡Registro guardado! Racha actual de ejercicio: {racha_ejercicio} días."
                )
                print(obtener_rango(racha_ejercicio))
        else:
            print("Por favor ingresa un valor entre 45 y 120 minutos.")

    #Registro de hábitos
    elif opcion == "3":
        print("\n--- Registro DE HÁBITOS ---")

        if not matriz_historial:
            print("Aún no hay registros en la matriz.")
        else:
            print("Sesión\tSueño(hrs)\tEjercicio(min)")
            numero_sesion = 1
            for fila in matriz_historial:
                print(f"#{numero_sesion}\t{fila[0]}\t\t{fila[1]}")
                numero_sesion += 1

    #Ver racha
    elif opcion == "4":
        print("\n--- RACHAS ACTUALES ---")
        print(f"Sueño: {racha_dormir} días | {obtener_rango(racha_dormir)}")
        print(
            f"Ejercicio: {racha_ejercicio} días | {obtener_rango(racha_ejercicio)}"
        )

    #Cerrar programa
    elif opcion == "5":
        print("\n¡La disciplina no es una opción! Nos vemos luego, guerrero.")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")