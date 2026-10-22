# ==============================================================================
# Archivo: ejercicio7_actividades_exploracion_cientifica.py
# Curso: SOFT-01 Principios de Programación 1 -  SCV6
# Integrante: Stwart Santamaria Artavia 
# Fecha: 21/10/2026
# Versión: 2.0
# Descripción: Simula la etapa de exploración científica en el destino mediante un
#              menú iterativo. Controla el consumo de energía y provisiones, y 
#              acumula puntos científicos, actividades realizadas y muestras.
# ==============================================================================

# --- ENTRADA DE DATOS INICIALES ---
energia_disponible = int(input("Ingrese la energía disponible al llegar al destino: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles al llegar al destino: "))

# --- INICIALIZACIÓN DE CONTADORES, ACUMULADORES Y VARIABLE DE CONTROL ---
puntos_cientificos = 0
actividades_realizadas = 0
muestras_recolectadas = 0
en_exploracion = True

# --- ESTRUCTURA ITERATIVA (MENÚ DE EXPLORACIÓN) ---
while en_exploracion:
    print("\n--- MENÚ DE ACTIVIDADES DE EXPLORACIÓN ---")
    print("1. Analizar terreno")
    print("2. Recolectar muestra")
    print("3. Realizar observación")
    print("4. Finalizar exploración")
    
    opcion_seleccionada = int(input("Seleccione una actividad: "))
    
    # --- EVALUACIÓN DE OPCIONES (CONDICIONAL MÚLTIPLE Y VERIFICACIÓN DE RECURSOS) ---
    if opcion_seleccionada == 1:
        # Analizar terreno: Consume 8 de energía y 0 de provisiones. Otorga 10 puntos.
        if energia_disponible >= 8 and provisiones_disponibles >= 0:
            energia_disponible = energia_disponible - 8
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + 10
            print("\n Actividad realizada: Analizar terreno. Puntos obtenidos: 10")
            print("Energía restante:", energia_disponible, "unidades | Provisiones restantes:", provisiones_disponibles, "unidades")
            
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            en_exploracion = False

    elif opcion_seleccionada == 2:
        # Recolectar muestra: Consume 12 de energía y 2 de provisiones. Otorga 20 puntos y +1 muestra.
        if energia_disponible >= 12 and provisiones_disponibles >= 2:
            energia_disponible = energia_disponible - 12
            provisiones_disponibles = provisiones_disponibles - 2
            actividades_realizadas = actividades_realizadas + 1
            muestras_recolectadas = muestras_recolectadas + 1
            puntos_cientificos = puntos_cientificos + 20
            print("Actividad realizada: Recolectar muestra. Puntos obtenidos: 20")
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            en_exploracion = False

    elif opcion_seleccionada == 3:
        # Realizar observación: Consume 5 de energía y 0 de provisiones. Otorga 8 puntos.
        if energia_disponible >= 5 and provisiones_disponibles >= 0:
            energia_disponible = energia_disponible - 5
            actividades_realizadas = actividades_realizadas + 1
            puntos_cientificos = puntos_cientificos + 8
            print("Actividad realizada: Realizar observación. Puntos obtenidos: 8")
        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            en_exploracion = False

    elif opcion_seleccionada == 4:
        # Finalización voluntaria por la tripulación
        print("Exploración finalizada por la tripulación.")
        en_exploracion = False

    else:
        # Opción inválida: No modifica el estado ni interrumpe el ciclo
        print("Opción no válida.")

# --- SALIDA DE RESULTADOS (RESUMEN FINAL) ---
print("\nActividades realizadas:", actividades_realizadas)
print("Muestras recolectadas:", muestras_recolectadas)
print("Puntos científicos:", puntos_cientificos)
print("Energía restante:", energia_disponible, "unidades")
print("Provisiones restantes:", provisiones_disponibles, "unidades")
