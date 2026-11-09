# ==============================================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Stwart Santamaria Artavia
# Fecha: 21/10/2026
# Versión: 2.0
# Descripción: Evalúa la factibilidad del viaje de regreso (Caso A) o calcula
#              los días de supervivencia estimada y recursos limitantes si la 
#              tripulación queda varada (Caso B), mostrando un resumen final.
# ==============================================================================

# --- ENTRADA DE DATOS ---
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_ida = int(input("Ingrese la cantidad de días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))

# --- REGLA DE DECISIÓN PRINCIPAL ---
combustible_necesario = dias_ida * 8

if combustible >= combustible_necesario:
    # ==========================================================================
    # CASO A: LA NAVE INICIA EL REGRESO
    # ==========================================================================
    dias_completados = 0
    en_regreso = True
    consumo_oxigeno_dia = tripulantes * 2
    consumo_provisiones_dia = tripulantes * 1
    
    print("\n--------------------------------------------------")
    print(">>> EJECUCIÓN EVALUADA: CASO A (INICIO DE REGRESO) <<<")
    print("--------------------------------------------------")
    
    while en_regreso and dias_completados < dias_ida:
        # Verificar si todos los recursos alcanzan para el día actual
        if (combustible >= 8 and 
            oxigeno >= consumo_oxigeno_dia and 
            energia >= 5 and 
            provisiones >= consumo_provisiones_dia):
            
            # Restar consumos diarios
            combustible = combustible - 8
            oxigeno = oxigeno - consumo_oxigeno_dia
            energia = energia - 5
            provisiones = provisiones - consumo_provisiones_dia
            dias_completados = dias_completados + 1
            
            print("Día", dias_completados, "| Combustible:", combustible, "| Oxígeno:", oxigeno, "| Energía:", energia, "| Provisiones:", provisiones)
        else:
            en_regreso = False

    # --- ENCABEZADO DE RESUMEN FINAL (CASO A) ---
    print("\n==================================================")
    print("           RESUMEN FINAL DE LA EVALUACIÓN        ")
    print("==================================================")
    print("CASO EVALUADO: Caso A - Viaje de regreso iniciado")
    
    if dias_completados == dias_ida:
        print("ESTADO: Regreso exitoso a la Tierra")
        print("--------------------------------------------------")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")
    else:
        dia_interrumpido = dias_completados + 1
        print("ESTADO: Regreso interrumpido en el día", dia_interrumpido)
        print("--------------------------------------------------")
        
        # Evaluar recursos insuficientes en orden: oxígeno, energía, provisiones
        if oxigeno < consumo_oxigeno_dia:
            print("Recurso insuficiente: oxígeno")
        if energia < 5:
            print("Recurso insuficiente: energía")
        if provisiones < consumo_provisiones_dia:
            print("Recurso insuficiente: provisiones")
            
        print("La tripulación no completó el regreso.")
    print("==================================================")

else:
    # ==========================================================================
    # CASO B: LA NAVE NO INICIA EL REGRESO (TRIPULACIÓN VARADA)
    # ==========================================================================
    # Cálculo de días por recurso mediante división entera
    dias_oxigeno = oxigeno // (tripulantes * 2)
    dias_energia = energia // 5
    dias_provisiones = provisiones // tripulantes
    
    # Obtención del menor valor sin utilizar la función min()
    supervivencia_minima = dias_oxigeno
    if dias_energia < supervivencia_minima:
        supervivencia_minima = dias_energia
    if dias_provisiones < supervivencia_minima:
        supervivencia_minima = dias_provisiones
        
    # Identificación de recursos limitantes (manejo de empates)
    recursos_limitantes = ""
    es_primer_recurso = True
    
    if dias_oxigeno == supervivencia_minima:
        recursos_limitantes = "oxígeno"
        es_primer_recurso = False
        
    if dias_energia == supervivencia_minima:
        if es_primer_recurso:
            recursos_limitantes = "energía"
            es_primer_recurso = False
        else:
            recursos_limitantes = recursos_limitantes + ", energía"
            
    if dias_provisiones == supervivencia_minima:
        if es_primer_recurso:
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"

    # --- ENCABEZADO DE RESUMEN FINAL (CASO B) ---
    print("\n==================================================")
    print("           RESUMEN FINAL DE LA EVALUACIÓN        ")
    print("==================================================")
    print("CASO EVALUADO: Caso B - Tripulación varada en el destino")
    print("ESTADO: Sin combustible suficiente para despegue")
    print("--------------------------------------------------")
    print("Días de supervivencia por oxígeno:", dias_oxigeno)
    print("Días de supervivencia por energía:", dias_energia)
    print("Días de supervivencia por provisiones:", dias_provisiones)
    print("--------------------------------------------------")
    print("Supervivencia estimada:", supervivencia_minima, "días")
    print("Recurso(s) limitante(s):", recursos_limitantes)
    print("==================================================")