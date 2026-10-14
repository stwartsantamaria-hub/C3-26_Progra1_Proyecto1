# ===============
# Archivo: ejercicio4_autorizacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Nombre: Stwart Santamaria Artavia
# Fecha: 14/10/2026
# Versión: 1.0
# Descripción: Realiza la verificación general de los cuatro recursos principales
#              y autoriza el lanzamiento mediante condicional doble sin anidadas.
# ===============

# --- DECLARACIÓN DE CONSTANTES ---
RESERVA_COMBUSTIBLE = 10

# --- ENTRADA DE DATOS ---
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible para ida: "))
combustible_regreso = int(input("Ingrese el combustible para regreso: "))

oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))

energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))

provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))

# --- CÁLCULOS / PROCESAMIENTO ---
combustible_total_requerido = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

# --- DECISIÓN (CONDICIONAL DOBLE CON EVALUACIÓN DE LOS 4 RECURSOS) ---
if (combustible_disponible >= combustible_total_requerido and
    oxigeno_disponible >= oxigeno_requerido and
    energia_disponible >= energia_requerida and
    provisiones_disponibles >= provisiones_requeridas):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")