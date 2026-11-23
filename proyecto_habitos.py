import time
import os  

# variables globales
racha_dormir = 0
racha_ejercicio = 0

#Matriz historial
matriz_historial = []

# Lista de rangos
RANGOS = [(30, "Líder"), (14, "Maestro"), (7, "Contendiente"), (1, "Promesa")]

# Lista de notas de hábitos
notas_historial = []


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

# Guardado de sesion
def registro(nombre_registro, nombre, codigo, r_dormir, r_ejercicio, matriz, notas):
    
    with open(nombre_registro, "w", encoding="utf-8") as historial:
        historial.write(f"Usuario|{nombre}|{codigo}\n")  
        historial.write(f"Tus Rachas|{r_dormir}|{r_ejercicio}\n")  
        for fila in matriz:
            historial.write(f"Tiempo de Habito|{fila[0]}|{fila[1]}\n")  
        for nota in notas:
            nota_limpia = nota.replace("\n", " ").replace("|", "-")
            historial.write(f"Notas de Habitos|{nota_limpia}\n") 

#...................................................... 

# Recuperador de sesion
def cargar_registro(nombre_registro):
    if not os.path.exists(nombre_registro):
        return 0, 0, [], [], False

    r_dormir = 0
    r_ejercicio = 0
    matriz = []
    notas = []

    with open(nombre_registro, "r", encoding="utf-8") as historial:
        for linea in historial:
            lineas = linea.strip().split("|")
            if lineas[0] == "Tus Rachas":
                r_dormir = int(lineas[1])
                r_ejercicio = int(lineas[2])
            elif lineas[0] == "Tiempo de Habito":
                matriz.append([int(lineas[1]), int(lineas[2])])
            elif lineas[0] == "Notas de Habitos":
                notas.append(lineas[1])

    return r_dormir, r_ejercicio, matriz, notas, True

#......................................................

# Creador de Perfil y Cargar Sesión
nombre_inicial = input("Ingresa tu nombre de guerrero: ")
nombre_usuario = nombre_inicial.strip().title()
if not nombre_usuario:
    nombre_usuario = "Guerrero Anónimo"

codigo_unico = f"{nombre_usuario[:3].upper()}-{len(nombre_usuario):02d}"
print(f"\n{' ERES BIENVENIDO '.center(40, '=')}")
print(f"Usuario: {nombre_usuario} | Código: {codigo_unico}")

registro_sesion = f"sesion_{codigo_unico}.txt"
racha_dormir, racha_ejercicio, matriz_historial, notas_historial, sesion_cargada = cargar_registro(registro_sesion)

if sesion_cargada:
    print(f"¡Estas de vuelta! ({len(matriz_historial)} registros anteriores)")
else:
    registro(registro_sesion, nombre_usuario, codigo_unico, racha_dormir, racha_ejercicio, matriz_historial, notas_historial)
    print(f"Registro Creado: {registro_sesion}")

#.....................................................

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

            # Nota de sueño
            nota_sueño = input("Cómo dormiste?: ").strip()
            if len(nota_sueño) == 0:
                nota_sueño = "Sin comentario"
            else:
                nota_sueño = nota_sueño.capitalize().replace("mal", "en mejora")
            total_palabras = len(nota_sueño.split())
            notas_historial.append(f"[Sueño] {nota_sueño} ({total_palabras} palabras)")

            registro(registro_sesion, nombre_usuario, codigo_unico, racha_dormir, racha_ejercicio, matriz_historial, notas_historial)

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

                # Nota de ejercicio
                enfoque = input("¿Cuál fue tu enfoque? (ej. correr, pesas): ").strip().lower()
                if "correr" in enfoque or "cardio" in enfoque:
                    categoria = "CARDIO"
                elif "pesas" in enfoque or "fuerza" in enfoque:
                    categoria = "FUERZA"
                else:
                    categoria = enfoque.upper() if enfoque else "GENERAL"
                notas_historial.append(f"[Ejercicio - {categoria}] {enfoque.capitalize()}")

                registro(registro_sesion, nombre_usuario, codigo_unico, racha_dormir, racha_ejercicio, matriz_historial, notas_historial)
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

        # Notas de hábitos
        if notas_historial:
            print("\n--- NOTAS DE HÁBITOS ---")
            for nota in notas_historial:
                print(f"• {nota}")

    #Ver racha
    elif opcion == "4":
        print("\n--- RACHAS ACTUALES ---")
        print(f"Sueño: {racha_dormir} días | {obtener_rango(racha_dormir)}")
        print(
            f"Ejercicio: {racha_ejercicio} días | {obtener_rango(racha_ejercicio)}"
        )

        # Buscar en notas de hábitos
        if notas_historial:
            palabra_buscar = input("\nBusca una palabra en tus notas (Enter para saltar): ").strip().lower()
            if palabra_buscar:
                apariciones = 0
                for nota in notas_historial:
                    if palabra_buscar in nota.lower():
                        print(f"  -> {nota}")
                        apariciones += nota.lower().count(palabra_buscar)
                print(f"Menciones de '{palabra_buscar}': {apariciones}")

    #Cerrar programa
    elif opcion == "5":
        registro(registro_sesion, nombre_usuario, codigo_unico, racha_dormir, racha_ejercicio, matriz_historial, notas_historial)
        print(f"\nRegistro guardado en '{registro_sesion}'.") 
        print("¡La disciplina no es una opción! Nos vemos luego, guerrero.")
        print(f"Buen Camino: {nombre_usuario.upper()} [{codigo_unico}]")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")