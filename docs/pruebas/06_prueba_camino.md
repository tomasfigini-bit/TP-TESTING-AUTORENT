# Plan de Pruebas: Camino (Caja Blanca)

Método analizado: `Agencia.alquilar_vehiculo(patente, dni, dias)`

## Caminos identificados
| Camino | Descripción |
| :--- | :--- |
| 1 | buscar_vehiculo -> None -> ValueError (vehículo no encontrado) |
| 2 | buscar_vehiculo OK -> buscar_cliente -> None -> ValueError (cliente no encontrado) |
| 3 | buscar_vehiculo OK -> buscar_cliente OK -> not disponible -> ValueError |
| 4 | Ambos OK -> disponible -> días inválidos -> ValueError |
| 5 | Todo OK -> Alquiler creado (camino feliz) |

## Casos de prueba por camino
| ID | Camino | Condición | Resultado esperado |
| :--- | :--- | :--- | :--- |
| CC-01 | 1 | Patente no existe | ValueError: Vehiculo no encontrado |
| CC-02 | 2 | Patente OK, DNI no existe | ValueError: Cliente no encontrado |
| CC-03 | 3 | Ambos existen, vehículo alquilado | ValueError: no esta disponible |
| CC-04 | 4 | Todo OK pero dias=0 | ValueError: dias deben ser entero positivo |
| CC-05 | 5 | Todo OK | Alquiler creado, vehículo alquilado |

**Complejidad ciclomática:** 5 caminos independientes.
