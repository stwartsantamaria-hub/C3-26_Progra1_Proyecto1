# ===============
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Nombre: Stwart Santamaria Artavia.
# Fecha de entrega: 14/10/2026
# Versión: 1.0
# Descripción: Calcula los recursos necesarios (combustible, oxígeno, energía y provisiones)
#              para la preparación de una misión espacial.
# ===============

# --- DECLARACIÓN DE CONSTANTES ---
CONSUMO_COMBUSTIBLE_DIARIO = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO_DIARIO = 2
EMERGENCIA_OXIGENO = 5
CONSUMO_ENERGIA_DIARIO = 5
OPERACIONES_ENERGIA = 10
CONSUMO_PROVISIONES_DIARIO = 1
ADICIONAL_PROVISIONES = 3

# --- ENTRADA DE DATOS ---
nombre_mision = input("Ingrese el nombre de la misión: ")
cantidad_tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese los días estimados para llegar al destino: "))

# --- CÁLCULOS / PROCESAMIENTO ---
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = (dias_viaje * CONSUMO_OXIGENO_DIARIO * 2 * cantidad_tripulantes) + EMERGENCIA_OXIGENO
energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIARIO * 2) + OPERACIONES_ENERGIA
provisiones_requeridas = (dias_viaje * cantidad_tripulantes * CONSUMO_PROVISIONES_DIARIO * 2) + ADICIONAL_PROVISIONES

# --- SALIDA DE RESULTADOS ---
print("\n--- RESUMEN DE LA MISIÓN ---")
print("Misión:", nombre_mision)
print("Tripulantes:", cantidad_tripulantes)
print("Duración estimada hasta el destino:", dias_viaje, "días")
print("Combustible para llegar:", combustible_ida, "unidades")
print("Combustible para regresar:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")