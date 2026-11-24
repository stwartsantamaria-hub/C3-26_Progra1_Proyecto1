# ==============================================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Stwart Santamaria Artavia
# Fecha: 23/11/2026
# Versión: 2.0
# Descripción: Sistema integrado Misión Órbita (Componentes A, B, C y D:
#              Preparación, Viaje de ida, Exploración científica y Regreso).
# ==============================================================================

# --- DECLARACIÓN DE CONSTANTES ---
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))

# Cada actividad: (nombre, combustible, energía, provisiones, puntos)
ACTIVIDADES = (
    ("Analizar terreno", 0, 8, 0, 10),
    ("Recolectar muestra", 0, 12, 2, 20),
    ("Realizar observación", 0, 5, 0, 8),
    ("Sobrevolar la zona", 15, 3, 0, 25)
)

RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = (
    "Regreso exitoso",
    "Regreso interrumpido",
    "Tripulación varada",
    "No autorizada",
    "No planificada"
)

# Columnas de DESTINOS: (nombre, dias)
DES_NOMBRE = 0
DES_DIAS = 1

# Columnas de ACTIVIDADES: (nombre, combustible, energía, provisiones, puntos)
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Posición de cada recurso en las listas recursos, requeridos y consumo
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Columnas de la matriz bitacora: [numero, actividad, puntos]
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Columnas de la matriz historial: [numero, nombre, destino, resultado, puntos]
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# Constantes numéricas de fórmulas
CANTIDAD_TRAYECTOS = 2
CONSUMO_COMBUSTIBLE_DIARIO = 8
CONSUMO_OXIGENO_DIARIO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIARIA = 5
CONSUMO_PROVISIONES_DIARIAS_TRIPULANTE = 1

RESERVA_COMBUSTIBLE = 10
OXIGENO_EMERGENCIA = 5
ENERGIA_EXPLORACION = 10
PROVISIONES_ADICIONALES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10


# ==============================================================================
# COMPONENTE A: PREPARACIÓN Y AUTORIZACIÓN
# ==============================================================================

def mostrar_destinos():
    """Muestra la lista numerada de destinos disponibles y sus días de ida."""
    print("Destinos disponibles:")
    for indice in range(len(DESTINOS)):
        nombre_destino = DESTINOS[indice][DES_NOMBRE]
        dias_destino = DESTINOS[indice][DES_DIAS]
        print(str(indice + 1) + ". " + nombre_destino + " (" + str(dias_destino) + " días)")


def leer_recursos():
    """Solicita las cantidades disponibles de cada recurso y devuelve una lista."""
    disponibles = []
    for nombre_recurso in RECURSOS:
        cantidad_recurso = int(input("Cantidad disponible de " + nombre_recurso + ": "))
        disponibles.append(cantidad_recurso)
    return disponibles


def calcular_requeridos(dias_viaje, tripulantes):
    """Calcula los recursos mínimos requeridos para ida, exploración y regreso."""
    combustible_requerido = (dias_viaje * CONSUMO_COMBUSTIBLE_DIARIO * CANTIDAD_TRAYECTOS) + RESERVA_COMBUSTIBLE
    oxigeno_requerido = (dias_viaje * CANTIDAD_TRAYECTOS * CONSUMO_OXIGENO_DIARIO_TRIPULANTE * tripulantes) + OXIGENO_EMERGENCIA
    energia_requerida = (dias_viaje * CONSUMO_ENERGIA_DIARIA * CANTIDAD_TRAYECTOS) + ENERGIA_EXPLORACION
    provisiones_requeridas = (dias_viaje * tripulantes * CANTIDAD_TRAYECTOS) + PROVISIONES_ADICIONALES
    
    requeridos = [
        combustible_requerido,
        oxigeno_requerido,
        energia_requerida,
        provisiones_requeridas
    ]
    return requeridos


def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes, disponibles, requeridos):
    """Muestra el resumen comparativo de recursos y evalúa el margen de combustible."""
    print("Misión:", nombre_mision)
    print("Destino:", nombre_destino)
    print("Duración del viaje de ida:", dias_viaje, "días")
    print("Tripulantes:", tripulantes)
    
    for indice in range(len(RECURSOS)):
        nombre_recurso = RECURSOS[indice].capitalize()
        print(nombre_recurso + ": disponible " + str(disponibles[indice]) + " | requerido " + str(requeridos[indice]))
        
    margen_combustible = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]
    print("Margen adicional de combustible:", margen_combustible, "unidades")
    
    if margen_combustible < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


def autorizar_lanzamiento(disponibles, requeridos):
    """Verifica que todos los recursos disponibles cubran los requeridos."""
    autorizado = True
    for indice in range(len(RECURSOS)):
        if disponibles[indice] < requeridos[indice]:
            autorizado = False
    return autorizado


# ==============================================================================
# COMPONENTE B: VIAJE DE IDA
# ==============================================================================

def calcular_consumo_diario(tripulantes):
    """Calcula el consumo diario de cada recurso según los tripulantes."""
    consumo = [
        CONSUMO_COMBUSTIBLE_DIARIO,
        CONSUMO_OXIGENO_DIARIO_TRIPULANTE * tripulantes,
        CONSUMO_ENERGIA_DIARIA,
        CONSUMO_PROVISIONES_DIARIAS_TRIPULANTE * tripulantes
    ]
    return consumo


def viajar_al_destino(recursos, dias_viaje, tripulantes):
    """Descuenta directamente los recursos consumidos durante el viaje de ida."""
    consumo = calcular_consumo_diario(tripulantes)
    for indice in range(len(RECURSOS)):
        recursos[indice] = recursos[indice] - (consumo[indice] * dias_viaje)
    return recursos


def recursos_alcanzan(recursos, consumo):
    """Verifica si los recursos actuales cubren el consumo de un día."""
    alcanzan = True
    for indice in range(len(RECURSOS)):
        if recursos[indice] < consumo[indice]:
            alcanzan = False
    return alcanzan


def simular_trayecto(recursos, dias, tripulantes):
    """Simula día a día un trayecto mientras alcancen los recursos."""
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True
    
    while dias_completados < dias and puede_continuar:
        if recursos_alcanzan(recursos, consumo):
            for indice in range(len(RECURSOS)):
                recursos[indice] = recursos[indice] - consumo[indice]
            dias_completados = dias_completados + 1
            print(
                "Día", dias_completados,
                "| Combustible:", recursos[COMBUSTIBLE],
                "| Oxígeno:", recursos[OXIGENO],
                "| Energía:", recursos[ENERGIA],
                "| Provisiones:", recursos[PROVISIONES]
            )
        else:
            puede_continuar = False
            
    return dias_completados


def mostrar_recursos(recursos):
    """Muestra las unidades restantes de cada recurso."""
    print("Recursos restantes:")
    for indice in range(len(RECURSOS)):
        nombre_recurso = RECURSOS[indice].capitalize()
        print("- " + nombre_recurso + ": " + str(recursos[indice]) + " unidades")


# ==============================================================================
# COMPONENTE C: EXPLORACIÓN CIENTÍFICA Y BITÁCORA
# ==============================================================================

def mostrar_actividades():
    """Muestra las actividades científicas disponibles y la opción de finalizar."""
    print("Actividades científicas disponibles:")
    for indice in range(len(ACTIVIDADES)):
        nombre_actividad = ACTIVIDADES[indice][ACT_NOMBRE]
        costo_combustible = ACTIVIDADES[indice][ACT_COMBUSTIBLE]
        costo_energia = ACTIVIDADES[indice][ACT_ENERGIA]
        costo_provisiones = ACTIVIDADES[indice][ACT_PROVISIONES]
        puntos_actividad = ACTIVIDADES[indice][ACT_PUNTOS]
        print(
            str(indice + 1) + ". " + nombre_actividad +
            " (Combustible: " + str(costo_combustible) +
            ", Energía: " + str(costo_energia) +
            ", Provisiones: " + str(costo_provisiones) +
            ", Puntos: " + str(puntos_actividad) + ")"
        )
    print(str(len(ACTIVIDADES) + 1) + ". Finalizar exploración")


def actividad_viable(recursos, indice_actividad):
    """Verifica si los recursos actuales cubren el costo de la actividad."""
    costo_combustible = ACTIVIDADES[indice_actividad][ACT_COMBUSTIBLE]
    costo_energia = ACTIVIDADES[indice_actividad][ACT_ENERGIA]
    costo_provisiones = ACTIVIDADES[indice_actividad][ACT_PROVISIONES]
    
    viable = True
    if recursos[COMBUSTIBLE] < costo_combustible:
        viable = False
    if recursos[ENERGIA] < costo_energia:
        viable = False
    if recursos[PROVISIONES] < costo_provisiones:
        viable = False
    return viable


def ejecutar_actividad(recursos, indice_actividad):
    """Descuenta de recursos los costos de la actividad ejecutada."""
    recursos[COMBUSTIBLE] = recursos[COMBUSTIBLE] - ACTIVIDADES[indice_actividad][ACT_COMBUSTIBLE]
    recursos[ENERGIA] = recursos[ENERGIA] - ACTIVIDADES[indice_actividad][ACT_ENERGIA]
    recursos[PROVISIONES] = recursos[PROVISIONES] - ACTIVIDADES[indice_actividad][ACT_PROVISIONES]


def registrar_actividad(bitacora, numero_actividad, nombre_actividad, puntos):
    """Agrega una nueva fila a la matriz bitacora con los datos de la actividad."""
    registro = [numero_actividad, nombre_actividad, puntos]
    bitacora.append(registro)


def mostrar_bitacora(bitacora):
    """Despliega todas las actividades registradas en la bitácora."""
    print("=== BITÁCORA DE EXPLORACIÓN ===")
    if len(bitacora) == 0:
        print("No se registraron actividades científicas.")
    else:
        for indice in range(len(bitacora)):
            numero_registro = bitacora[indice][BIT_NUMERO]
            nombre_actividad = bitacora[indice][BIT_ACTIVIDAD]
            puntos_registro = bitacora[indice][BIT_PUNTOS]
            print(str(numero_registro) + ". " + nombre_actividad + " - " + str(puntos_registro) + " puntos")


def calcular_puntos(bitacora):
    """Suma y retorna los puntos científicos acumulados en la bitácora."""
    puntos_totales = 0
    for indice in range(len(bitacora)):
        puntos_totales = puntos_totales + bitacora[indice][BIT_PUNTOS]
    return puntos_totales


def explorar(recursos):
    """Gestiona el ciclo interactivo de exploración científica en superficie."""
    bitacora = []
    numero_actividad = 1
    opcion_finalizar = len(ACTIVIDADES) + 1
    explorando = True
    
    while explorando:
        mostrar_actividades()
        opcion_actividad = int(input("Seleccione una actividad: "))
        
        if opcion_actividad == opcion_finalizar:
            explorando = False
        elif opcion_actividad < 1 or opcion_actividad > len(ACTIVIDADES):
            print("Opción de actividad no válida.")
        else:
            indice_actividad = opcion_actividad - 1
            if actividad_viable(recursos, indice_actividad):
                ejecutar_actividad(recursos, indice_actividad)
                nombre_actividad = ACTIVIDADES[indice_actividad][ACT_NOMBRE]
                puntos_actividad = ACTIVIDADES[indice_actividad][ACT_PUNTOS]
                registrar_actividad(bitacora, numero_actividad, nombre_actividad, puntos_actividad)
                numero_actividad = numero_actividad + 1
                print("Actividad ejecutada:", nombre_actividad)
                mostrar_recursos(recursos)
            else:
                print("Recursos insuficientes para realizar esta actividad.")
                
    return bitacora


# ==============================================================================
# COMPONENTE D: VIAJE DE REGRESO Y SUPERVIVENCIA
# ==============================================================================

def calcular_dias_supervivencia(recursos, tripulantes):
    """Calcula cuántos días completos puede sobrevivir la tripulación con recursos vitales."""
    consumo_diario = calcular_consumo_diario(tripulantes)
    dias_oxigeno = recursos[OXIGENO] // consumo_diario[OXIGENO]
    dias_energia = recursos[ENERGIA] // consumo_diario[ENERGIA]
    dias_provisiones = recursos[PROVISIONES] // consumo_diario[PROVISIONES]
    
    dias_minimos = dias_oxigeno
    if dias_energia < dias_minimos:
        dias_minimos = dias_energia
    if dias_provisiones < dias_minimos:
        dias_minimos = dias_provisiones
        
    return dias_minimos


def identificar_recurso_critico(recursos, tripulantes):
    """Identifica cuál recurso vital se agota primero (menor autonomía en días)."""
    consumo_diario = calcular_consumo_diario(tripulantes)
    dias_oxigeno = recursos[OXIGENO] // consumo_diario[OXIGENO]
    dias_energia = recursos[ENERGIA] // consumo_diario[ENERGIA]
    dias_provisiones = recursos[PROVISIONES] // consumo_diario[PROVISIONES]
    
    dias_minimos = dias_oxigeno
    recurso_critico = RECURSOS_VITALES[0]
    
    if dias_energia < dias_minimos:
        dias_minimos = dias_energia
        recurso_critico = RECURSOS_VITALES[1]
        
    if dias_provisiones < dias_minimos:
        dias_minimos = dias_provisiones
        recurso_critico = RECURSOS_VITALES[2]
        
    return recurso_critico


def evaluar_varados(recursos, tripulantes):
    """Muestra la autonomía de supervivencia y el recurso vital crítico si quedan varados."""
    dias_supervivencia = calcular_dias_supervivencia(recursos, tripulantes)
    recurso_critico = identificar_recurso_critico(recursos, tripulantes)
    print("Días estimados de supervivencia:", dias_supervivencia)
    print("Recurso vital crítico:", recurso_critico)


def clasificar_resultado(dias_completados, dias_viaje):
    """Determina el estado final de la misión según los días recorridos de regreso."""
    if dias_completados == dias_viaje:
        resultado_mision = RESULTADOS[0]
    elif dias_completados > 0:
        resultado_mision = RESULTADOS[1]
    else:
        resultado_mision = RESULTADOS[2]
    return resultado_mision


def viajar_de_regreso(recursos, dias_viaje, tripulantes):
    """Simula el viaje de regreso día a día y evalúa supervivencia si no se completa."""
    print("=== VIAJE DE REGRESO ===")
    dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)
    resultado_mision = clasificar_resultado(dias_completados, dias_viaje)
    print("Resultado del regreso:", resultado_mision)
    
    if dias_completados < dias_viaje:
        evaluar_varados(recursos, tripulantes)
        
    return resultado_mision


# ==============================================================================
# CONTROL DE MISIÓN Y PROGRAMA PRINCIPAL
# ==============================================================================

def ejecutar_mision(numero):
    """Controla las fases de planificación, autorización, viaje, exploración y regreso."""
    print("=== PLANIFICACIÓN ===")
    nombre_mision = input("Nombre de la misión: ")
    tripulantes = int(input("Cantidad de tripulantes: "))
    mostrar_destinos()
    opcion_destino = int(input("Seleccione un destino: "))
    
    if opcion_destino < 1 or opcion_destino > len(DESTINOS):
        print("Opción de destino no válida. La misión no puede planificarse.")
        nombre_destino = "Ninguno"
        resultado_mision = RESULTADOS[4]
        puntos_totales = 0
    else:
        nombre_destino = DESTINOS[opcion_destino - 1][DES_NOMBRE]
        dias_viaje = DESTINOS[opcion_destino - 1][DES_DIAS]
        recursos = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, tripulantes)
        mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes, recursos, requeridos)
        
        if autorizar_lanzamiento(recursos, requeridos):
            print("Lanzamiento autorizado.")
            print("=== VIAJE DE IDA ===")
            recursos = viajar_al_destino(recursos, dias_viaje, tripulantes)
            print("La nave llegó a", nombre_destino, "en", dias_viaje, "días.")
            mostrar_recursos(recursos)
            
            print("=== EXPLORACIÓN CIENTÍFICA ===")
            bitacora = explorar(recursos)
            mostrar_bitacora(bitacora)
            puntos_totales = calcular_puntos(bitacora)
            print("Puntos científicos obtenidos:", puntos_totales)
            
            resultado_mision = viajar_de_regreso(recursos, dias_viaje, tripulantes)
        else:
            print("Lanzamiento no autorizado. La misión debe ser revisada.")
            resultado_mision = RESULTADOS[3]
            puntos_totales = 0

    mision = [numero, nombre_mision, nombre_destino, resultado_mision, puntos_totales]
    return mision


def main():
    """Punto de entrada principal del sistema Misión Órbita."""
    ejecutar_mision(1)


main()