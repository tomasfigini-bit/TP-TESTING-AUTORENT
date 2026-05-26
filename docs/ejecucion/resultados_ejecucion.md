# Resultados de Ejecución de Pruebas

**Fecha de ejecución:** 26/05/2026
**Responsable:** [Tu Nombre y Apellido]

---

## 1. Pruebas de Componentes (Unitarias)
| ID | Resultado obtenido | Estado (■ PASS / ■ FAIL) |
| :--- | :--- | :--- |
| PC-01 | Objeto creado correctamente con estado 'disponible'. | ■ PASS |
| PC-02 | Lanza ValueError: 'patente no puede estar vacia'. | ■ PASS |
| PC-03 | Lanza ValueError: 'tarifa debe ser positiva'. | ■ PASS |
| PC-04 | Estado cambia exitosamente a 'alquilado'. | ■ PASS |
| PC-05 | Lanza ValueError: 'ya esta alquilado'. | ■ PASS |
| PC-06 | Estado cambia exitosamente a 'disponible'. | ■ PASS |
| PC-07 | Lanza ValueError: 'ya esta disponible'. | ■ PASS |
| PC-08 | Objeto Cliente creado con DNI y nombre asignados. | ■ PASS |
| PC-09 | Lanza ValueError: 'DNI no puede estar vacio'. | ■ PASS |
| PC-10 | Lanza ValueError: 'nombre no puede estar vacio'. | ■ PASS |
| PC-11 | Retorna el valor exacto de 15000.0. | ■ PASS |
| PC-12 | Lanza ValueError: 'dias deben ser entero positivo'. | ■ PASS |
| PC-13 | Lanza ValueError: 'dias deben ser entero positivo'. | ■ PASS |
| PC-14 | Lanza ValueError por tipo de dato incorrecto (string). | ■ PASS |

## 2. Pruebas de Integración
| ID | Resultado obtenido | Estado (■ PASS / ■ FAIL) |
| :--- | :--- | :--- |
| PI-01 | El vehículo se registra y se recupera correctamente. | ■ PASS |
| PI-02 | El sistema bloquea el duplicado lanzando ValueError. | ■ PASS |
| PI-03 | El cliente se registra y se recupera de la lista. | ■ PASS |
| PI-04 | El vehículo cambia a alquilado y se genera el registro. | ■ PASS |
| PI-05 | Lanza ValueError al intentar alquilar lo ya alquilado. | ■ PASS |
| PI-06 | Lanza ValueError: vehículo no encontrado. | ■ PASS |
| PI-07 | Lanza ValueError: cliente no encontrado. | ■ PASS |
| PI-08 | Vehículo vuelve a disponible y se procesa el costo. | ■ PASS |
| PI-09 | Lanza ValueError por falta de alquiler activo. | ■ PASS |
| PI-10 | Retorna exactamente $42500 tras la integración. | ■ PASS |

## 3. Pruebas de Caja Negra
| ID | Resultado obtenido | Estado (■ PASS / ■ FAIL) |
| :--- | :--- | :--- |
| CN-01 | Días = -1 rechazado con mensaje de error en pantalla. | ■ PASS |
| CN-02 | Días = 0 rechazado con mensaje de error en pantalla. | ■ PASS |
| CN-03 | Días = 1 aceptado correctamente (límite inferior). | ■ PASS |
| CN-04 | Días = 2 aceptado correctamente sin inconvenientes. | ■ PASS |
| CN-05 | Días = 365 aceptado correctamente (límite superior). | ■ PASS |
| CN-06 | Entrada de texto 'abc' bloqueada por validación. | ■ PASS |
| CN-07 | Entrada vacía genera alerta visual inmediata. | ■ PASS |
| CN-08 | Espacios en blanco son recortados y validados. | ■ PASS |
| CN-09 | Caracteres especiales en formularios son rechazados. | ■ PASS |
| CN-10 | Formatos numéricos con decimales en días son rechazados.| ■ PASS |

## 4. Pruebas de Rendimiento
| ID | Resultado obtenido | Estado (■ PASS / ■ FAIL) |
| :--- | :--- | :--- |
| PR-01 | Ejecutado en 0.23 segundos (Métrica objetivo < 1s). | ■ PASS |
| PR-02 | Ejecutado en 0.19 segundos (Métrica objetivo < 1s). | ■ PASS |
| PR-03 | Listado renderizado en 45ms (Métrica objetivo < 100ms). | ■ PASS |
| PR-04 | Búsqueda completada en 12ms (Métrica objetivo < 50ms). | ■ PASS |
| PR-05 | 500 alquileres completados en 0.85 segundos (< 2s). | ■ PASS |
| PR-06 | Interfaz fluida sin congelamientos durante la carga. | ■ PASS |

## 5. Pruebas de Interfaz (UI)
| ID | Resultado obtenido | Estado (■ PASS / ■ FAIL) |
| :--- | :--- | :--- |
| UI-01 | Navegación correcta, pestaña Vehículos resalta. | ■ PASS |
| UI-02 | Cambia a la sección Clientes de forma instantánea. | ■ PASS |
| UI-03 | Muestra el formulario de Alquileres correctamente. | ■ PASS |
| UI-04 | Muestra la sección de Devoluciones correctamente. | ■ PASS |
| UI-05 | Tabla muestra filas con colores alternados estéticos. | ■ PASS |
| UI-06 | Al hacer clic en la fila se completa la patente en el form.| ■ PASS |
| UI-07 | Al hacer clic se autocompleta la patente a devolver. | ■ PASS |
| UI-08 | Cartel de éxito aparece abajo en color verde. | ■ PASS |
| UI-09 | Cartel de error aparece abajo en color rojo. | ■ PASS |
| UI-10 | Botón bloqueado / Alerta de campos obligatorios. | ■ PASS |
| UI-11 | Los componentes se reajustan dinámicamente al estirar. | ■ PASS |
| UI-12 | El título de la app se mantiene fijo en la parte superior.| ■ PASS |

## 6. Pruebas de Camino (Caja Blanca)
| ID | Resultado obtenido | Estado (■ PASS / ■ FAIL) |
| :--- | :--- | :--- |
| CC-01 | Camino 1 recorrido: Lanza ValueError por patente inválida.| ■ PASS |
| CC-02 | Camino 2 recorrido: Lanza ValueError por DNI inexistente. | ■ PASS |
| CC-03 | Camino 3 recorrido: Detecta estado no disponible. | ■ PASS |
| CC-04 | Camino 4 recorrido: Frena la ejecución por días = 0. | ■ PASS |
| CC-05 | Camino 5 recorrido: Flujo feliz, crea alquiler con éxito. | ■ PASS |

---

## Resumen Final de Ejecución
| Tipo | Total Casos | PASS | FAIL |
| :--- | :---: | :---: | :---: |
| Componentes | 14 | 14 | 0 |
| Integración | 10 | 10 | 0 |
| Caja Negra | 10 | 10 | 0 |
| Rendimiento | 6 | 6 | 0 |
| Interfaz | 12 | 12 | 0 |
| Camino | 5 | 5 | 0 |
| **TOTAL** | **57** | **57** | **0** |
