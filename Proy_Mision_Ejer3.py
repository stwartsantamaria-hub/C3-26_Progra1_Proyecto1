# ===============
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Nombre: Stwart Santamaria Artavia
# Fecha: 14/10/2026
# Versión: 1.0
# Descripción: Verifica si la nave posee soporte suficiente de oxígeno y provisiones
#              para la tripulación mediante una condicional doble.
# ===============

# --- ENTRADA DE DATOS ---
oxigeno_disponible = int(input("Ingrese la cantidad de oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese la cantidad de oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese la cantidad de provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese la cantidad de provisiones requeridas: "))

# --- DECISIÓN (CONDICIONAL DOBLE CON CONDICIÓN COMPUESTA) ---
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    # Salida si ambos recursos son suficientes
    print("La nave posee recursos suficientes para la tripulación.")
else:
    # Salida si falla alguno de los recursos o ambos
    print("La nave no posee recursos suficientes para la tripulación.")