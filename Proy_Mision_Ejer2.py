# ===============
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Nombre: Stwart Santamaria Artavia
# Fecha: 14/10/2026
# Versión: 1.0
# Descripción: Verifica la disponibilidad de combustible e informa si el margen
#              de reserva adicional es bajo mediante condicional simple.
# ===============

# --- DECLARACIÓN DE CONSTANTES ---
RESERVA_COMBUSTIBLE = 10

# --- ENTRADA DE DATOS ---
combustible_disponible = int(input("Ingrese la cantidad de combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible requerido para el viaje de ida: "))
combustible_regreso = int(input("Ingrese el combustible requerido para el viaje de regreso: "))

# --- CÁLCULOS / PROCESAMIENTO ---
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total_requerido

# --- SALIDA DE RESULTADOS OBLIGATORIOS ---
print("\n--- RESUMEN DE COMBUSTIBLE ---")
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible requerido para llegar:", combustible_ida, "unidades")
print("Combustible requerido para regresar:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total_requerido, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")

# --- DECISIÓN (CONDICIONAL SIMPLE) ---
if combustible_adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")