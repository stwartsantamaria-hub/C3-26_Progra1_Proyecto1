# C3-26_Progra1_Proyecto1
# Misión Órbita - Simulador de Exploración Espacial (Avance 1 y 2)

**Universidad CENFOTEC**  
**Escuela de Ingeniería del Software**  
**Curso:** Principios de Programación 1 (SOFT-01) - Sección SCV6  
**Periodo:** C3-2026  
**Docente Facilitador:** Verónica Mora Lezcano  

---

## 📋 Descripción del Proyecto
Este repositorio contiene el desarrollo del **Primer Avance del Proyecto Integrador: Misión Órbita**. Consiste en un conjunto de cuatro programas independientes desarrollados en Python que modelan las fases iniciales de planificación, cálculo de insumos, verificación de combustible y autorización de lanzamiento para una misión de exploración espacial.

* **Avance 1:** Algoritmos independientes para la preparación inicial de la misión y cálculo de recursos necesarios.
* **Avance 2:** Ejecución de la misión mediante algoritmos iterativos y condicionales.

---

### Descripción de los Ejercicios

* **Ejercicio 1: Cálculo de recursos necesarios para una misión**  
  Solicita el nombre de la misión, la cantidad de tripulantes y los días estimados de viaje para calcular de forma secuencial el combustible necesario de ida, regreso y reserva, así como el oxígeno, energía y provisiones requeridas.

* **Ejercicio 2: Verificación de combustible**  
  Solicita el combustible disponible, el requerido para la ida y para el regreso. Calcula el total requerido con reserva de emergencia y el margen adicional, mostrando una advertencia si el margen es menor a 10 unidades mediante una condicional simple.

* **Ejercicio 3: Verificación del soporte para la tripulación**  
  Solicita el oxígeno y las provisiones tanto disponibles como requeridas. Evalúa mediante una condicional doble si la nave cuenta con recursos suficientes para mantener a la tripulación durante el viaje sin especificar cuál recurso presenta déficit.

* **Ejercicio 4: Autorización inicial de lanzamiento**  
  Solicita la disponibilidad y los requerimientos de combustible, oxígeno, energía y provisiones. Realiza una verificación general mediante una condicional doble compuesta para autorizar o rechazar el lanzamiento, garantizando que exista combustible suficiente para el viaje de regreso.

 * **Ejercicio 7: Simula la fase de exploración científica en el destino a través de un menú interactivo repetitivo. Administra la energía y provisiones disponibles, permitiendo realizar actividades como analizar terreno, recolectar muestras u observar, acumulando puntos científicos y contadores sin permitir interrumpir el ciclo mediante cláusulas no autorizadas.
  * **Ejercicio 8: Evalúa las condiciones para el retorno de la nave a la Tierra. Si el combustible es suficiente, simula el viaje de regreso día a día (Caso A). Si el combustible es insuficiente, simula la situación de tripulación varada, calcula los días de supervivencia estimada mediante división entera sin utilizar funciones integradas de ordenamiento/búsqueda y detecta los recursos limitantes gestionando empates (Caso B).

  

---

## 👥 Integrate: Stwart Santamaria Artavia

---

## 📁 Estructura del Repositorio C3-26_Progra1_Proyecto1
mision-orbita/
│
├── README.md
│
├── avance1/
│   ├── documentacion
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
│
├── avance2/
│   ├── ejercicio7_exploracion.py
│   └── ejercicio8_regreso.py
└── documentacion/
    ├── ejercicio7_exploracion.pdf
    └── ejercicio8_regreso.pdf
