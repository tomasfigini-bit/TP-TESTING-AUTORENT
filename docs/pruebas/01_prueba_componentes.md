# Plan de Pruebas: Componentes (Unitarias)

Este documento detalla los casos de prueba unitarios para las clases principales del sistema AutoRent, verificando su comportamiento aislado.

## 1. Clase Vehiculo
| ID Prueba | Método | Descripción | Entrada (Datos) | Salida Esperada |
| :--- | :--- | :--- | :--- | :--- |
| CP-01 | `__init__` | Crear un vehículo con datos válidos | Patente: "AA123BB", Modelo: "Ford Focus", Tarifa: 5000 | Objeto Vehiculo creado con estado "disponible" |
| CP-02 | `marcar_alquilado` | Cambiar estado a alquilado | Vehículo disponible | Estado cambia a "alquilado" |
| CP-03 | `marcar_disponible` | Cambiar estado a disponible | Vehículo alquilado | Estado cambia a "disponible" |

## 2. Clase Cliente
| ID Prueba | Método | Descripción | Entrada (Datos) | Salida Esperada |
| :--- | :--- | :--- | :--- | :--- |
| CP-04 | `__init__` | Crear cliente con datos válidos | DNI: "12345678", Nombre: "Juan Perez" | Objeto Cliente creado con sus atributos |

## 3. Clase Alquiler
| ID Prueba | Método | Descripción | Entrada (Datos) | Salida Esperada |
| :--- | :--- | :--- | :--- | :--- |
| CP-05 | `calcular_costo` | Cálculo correcto de tarifa | Vehiculo(tarifa=5000), 3 días | Costo total = 15000 |
