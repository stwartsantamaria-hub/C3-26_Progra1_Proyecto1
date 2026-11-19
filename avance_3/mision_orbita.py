# ==============================================================================
# Archivo: mision_orbita.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Stwart Santamaria Artavia
# Fecha: 18/11/2026
# Versión: 1.0
# Descripción: Sistema integrado Misión Órbita (Componente A: Preparación y 
#              autorización, y Componente B: Viaje de ida).
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
# CONTROL DE MISIÓN Y PROGRAMA PRINCIPAL
# ==============================================================================

def ejecutar_mision(numero):
    """Controla las fases de planificación, autorización y viaje de una misión."""
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
            resultado_mision = RESULTADOS[0]
            puntos_totales = 0
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