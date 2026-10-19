import time

# variables globales
racha_dormir = 0
racha_ejercicio = 0

# Listas para almacenar el historial de registros de cada hábito
historial_dormir = []
historial_ejercicio = []

# Lista de tuplas 
RANGOS = [
    (30, "Líder"),
    (14, "Maestro"),
    (7, "Contendiente"),
    (1, "Promesa")
]

# Lista menú inicial
OPCIONES_MENU = [
    "1. Dormir 8 Horas",
    "2. Ejercicio Semanal",
    "3. Ver Historial de Hábitos",
    "4. Cerrar Mi Tracker"
]

# .....................................................

# Obtener Rango
def obtener_rango(racha):
    for dias, rango in RANGOS:
        if racha >= dias:
            return f"Tu Rango Actual: {rango}"
    return "Tu Rango Actual: Sin Rango"

# .....................................................

# Menu Inicial
def mostrar_menu_inicial():
    print("\n" + "="*40)
    print("Bienvenido al tracker de hábitos. ¡¡Tu mejor versión te espera!!")
    for opcion in OPCIONES_MENU:
        print(opcion)
    print("="*40)
    try:
        return int(input("Escoge tu opción: "))
    except ValueError:
        return 0

# .....................................................

# Contador de horas dormidas
def contador_horas_dormidas(horas):
    contador_dormir = 0
    while contador_dormir < horas:
        time.sleep(0.5)  # Ajustado para pruebas
        contador_dormir += 1
        print(f"Has dormido: {contador_dormir} horas")
    return contador_dormir

# .....................................................

# Menu Ejercicio
def minutos_diarias_ejercicio():
    while True:
        try:
            minutos_ejercicio = int(input("¿Cuántos minutos de ejercicio planeas hacer al día (rango 45-120)?: "))
            if 45 <= minutos_ejercicio <= 120:
                print(f"¡Excelente! Ahora deberás hacer {minutos_ejercicio} minutos al día.")
                return minutos_ejercicio
            else:
                print("Por favor ingresa un valor entre 45 y 120 minutos.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# .....................................................

# Contador de ejercicio
def contador_minutos_ejercicio(minutos):
    contador_ejercicio = 0
    while contador_ejercicio < minutos:
        time.sleep(0.05)  
        contador_ejercicio += 1
        print(f"Minutos de ejercicio completados: {contador_ejercicio}")
    return contador_ejercicio

# .....................................................

# Mostrar Historial
def mostrar_historial():
    print("\n--- HISTORIAL DE REGISTROS ---")
    
    print("\nRegistros de Sueño:")
    if not historial_dormir:
        print("  Aún no hay registros de sueño.")
    else:
        for i, horas in enumerate(historial_dormir, start=1):
            print(f"  Día {i}: {horas} horas completadas.")

    print("\nRegistros de Ejercicio:")
    if not historial_ejercicio:
        print("  Aún no hay registros de ejercicio.")
    else:
        for i, mins in enumerate(historial_ejercicio, start=1):
            print(f"  Sesión {i}: {mins} minutos completados.")

# .....................................................

# PROCEDIMIENTO PRINCIPAL DEL PROGRAMA

while True:
    opcion = mostrar_menu_inicial()
    
    # Proceso dormir 8 horas
    if opcion == 1:
        print("\n¡Buena Elección! Dormir 8 horas mejorará tu ritmo de vida.")
        when = input("¿Quieres empezar tu ciclo de sueño? (si/no): ").lower()
        if when == "si":
            horas_logradas = contador_horas_dormidas(8)
            racha_dormir += 1
            historial_dormir.append(horas_logradas)  # Guardar registro en lista
            
            print(f"\n¡Felicidades! Has completado el día. Racha actual: {racha_dormir} días.")
            print(obtener_rango(racha_dormir))

    # Proceso ejercicio
    elif opcion == 2:
        print("\n¡Excelente Elección! El ejercicio te mantendrá activo.")
        minutos_meta = minutos_diarias_ejercicio()
        when = input("¿Quieres empezar tu ciclo de ejercicio? (si/no): ").lower()
        if when == "si":
            mins_logrados = contador_minutos_ejercicio(minutos_meta)
            racha_ejercicio += 1
            historial_ejercicio.append(mins_logrados)  # Guardar registro en lista
            
            print(f"\n¡Felicidades! Has completado el día. Racha actual: {racha_ejercicio} días.")
            print(obtener_rango(racha_ejercicio))

    # Consultar historial
    elif opcion == 3:
        mostrar_historial()

    # Cerrar programa
    elif opcion == 4:
        print("\n¡La disciplina no es una opción! Nos vemos luego, guerrero.")
        break 
        
    else:
        print("Opción inválida. Por favor, selecciona una opción válida del menú.")