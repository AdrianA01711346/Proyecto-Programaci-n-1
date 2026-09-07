#Algoritmo tracker de habitos con rachas
import time

# damos valor a variables globales
racha_dormir=0
racha_ejercicio=0

#.....................................................

#definimos la funcion de menu inicial

def mostrar_menu_inicial():
    print("Bienvenido al tracker de habitos. Tu mejor version te espera!!")
    print("1. Dormir 8 Horas")
    print("2. Ejercicio Semanal")
    return int(input("Escoge tu primer habito: "))

#......................................................

# definimos el contador de horas dormidas

def contador_horas_dormidas(horas):
    contador_dormir=0
    while contador_dormir < horas:
        time.sleep(1)  
        contador_dormir += 1
        print(f"Has dormido: {contador_dormir} horas")
    return contador_dormir

#......................................................

# definimos la funcion de menu horas de ejercicio

def minutos_diarias_ejercicio():
    print("Cuantos minutos de ejercicio planeas hacer al día en un rango de 45-120?")
    minutos_ejercicio = int(input())
    if minutos_ejercicio < 45 or minutos_ejercicio > 120:
        print("Por favor ingresa un valor entre 45 y 120 minutos.")
        return minutos_diarias_ejercicio()  # Llamada recursiva para volver a pedir el valor
    else:
        print(f"Excelente! Ahora deberas hacer {minutos_ejercicio} minutos de ejercicio al día para mantener tu racha.")
        return minutos_ejercicio

#......................................................

#definimos contador de ejercicio

def contador_minutos_ejercicio(minutos):
    contador_ejercicio=0
    while contador_ejercicio < minutos:
        time.sleep(0.1)  
        contador_ejercicio += 1
        print(f"Minutos de ejercicio completados: {contador_ejercicio}")
    return contador_ejercicio

#......................................................

#PROCEDIMIENTO PRINCIPAL DEL PROGRAMA

opcion=mostrar_menu_inicial()

#procedimiento al escoger habito dormir

if opcion==1:
    print("Buena Elección!! Dormir 8 horas definitivamente mejorara tu ritmo de vida. ")
    print("Cumple con tu hábito hoy y desbloquea tu primer día de racha. ")
    when= input("Quieres empezar tu ciclo de sueño? (si/no): ")
    if when=="si":
        contador_horas_dormidas(8)
        racha_dormir+=1
        print(f"Felicidades!! Has completado tu primer día de racha. Tu racha actual es de {racha_dormir} días.") 
        print(f"Disfruta tu día! No querras perder tu racha de {racha_dormir} días, te esperamos de nuevo. ") 

#......................................................

#procedimiento al escoger habito ejercicio

if opcion==2:
    print("Excelente Elección!! Hacer ejercicio te mantendra activo durante el día. ")
    opcion=minutos_diarias_ejercicio()
    print("Cumple con tu hábito hoy y desbloquea tu primer día de racha. ")
    when= input("Quieres empezar tu ciclo de ejercicio? (si/no): ")
    if when=="si":
        contador_minutos_ejercicio(opcion)
        racha_ejercicio+=1
        print(f"Felicidades!! Has completado tu primer día de racha. Tu racha actual es de {racha_ejercicio} días.") 
        print(f"Disfruta tu día! No querras perder tu racha de {racha_ejercicio} días, te esperamos de nuevo. ")
    
       
    

