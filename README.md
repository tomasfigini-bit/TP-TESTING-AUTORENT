# AutoRent — Sistema de Alquiler de Vehículos

## Objetivo del Software
[cite_start]AutoRent es una aplicación de escritorio diseñada para gestionar de manera eficiente el alquiler de vehículos, permitiendo el control de la flota, el registro de clientes y la automatización de los cálculos de costos de alquiler[cite: 177].

## Requerimientos Funcionales
| ID | Requerimiento | Tipo |
|:---:|---|:---:|
| RF01 | Registrar vehículos con patente, modelo y tarifa diaria | Funcional |
| RF02 | Registrar clientes con DNI y nombre | Funcional |
| RF03 | Alquilar vehículo disponible a un cliente por N días | Funcional |
| RF04 | Procesar devolución y calcular costo total | Funcional |
| RF05 | Listar vehículos (todos / disponibles / alquilados) | Funcional |
| RF06 | Listar clientes registrados | Funcional |
| RF07 | Listar alquileres activos | Funcional |
[cite_start][cite: 184]

## Requerimientos No Funcionales
| ID | Requerimiento | Tipo |
|:---:|---|:---:|
| RNF01 | Interfaz gráfica de escritorio (CustomTkinter) | No Funcional |
| RNF02 | Validación de datos en todos los formularios | No Funcional |
| RNF03 | Feedback visual inmediato ante errores o éxitos | No Funcional |
| RNF04 | El sistema debe ejecutarse en Python 3.10+ | No Funcional |
| RNF05 | Navegación por secciones sin recargar la aplicación | No Funcional |
[cite_start][cite: 184, 185]

## Tecnologías utilizadas
* Python 3.10+
* [cite_start]CustomTkinter para la interfaz gráfica[cite: 184, 185].

## Diagramas UML
### Diagrama de Clases
```mermaid
classDiagram
    class Vehiculo {
        +str patente
        +str modelo
        +float tarifa_diaria
        +str estado
        +marcar_alquilado()
        +marcar_disponible()
    }
    class Cliente {
        +str dni
        +str nombre
    }
    class Alquiler {
        +Vehiculo vehiculo
        +Cliente cliente
        +int dias
        +float costo_total
        +calcular_costo()
    }
    class Agencia {
        +list vehiculos
        +list clientes
        +list alquileres
        +registrar_vehiculo()
        +registrar_cliente()
        +alquilar_vehiculo()
        +devolver_vehiculo()
    }
    Agencia "1" -- "*" Vehiculo
    Agencia "1" -- "*" Cliente
    Agencia "1" -- "*" Alquiler
    Alquiler "*" -- "1" Vehiculo
    Alquiler "*" -- "1" Cliente

graph TD
    Empleado((Empleado de Agencia))
    UC1(Registrar vehículo)
    UC2(Registrar cliente)
    UC3(Alquilar vehículo)
    UC4(Devolver vehículo)
    UC5(Listar vehículos)
    UC6(Listar clientes)
    UC7(Listar alquileres)

    Empleado --> UC1
    Empleado --> UC2
    Empleado --> UC3
    Empleado --> UC4
    Empleado --> UC5
    Empleado --> UC6
    Empleado --> UC7

sequenceDiagram
    participant E as Empleado
    participant UI as UI (Interfaz)
    participant A as Agencia
    participant V as Vehiculo
    participant AL as Alquiler

    E->>UI: Ingresa datos (Patente, DNI, Días)
    UI->>A: alquilar_vehiculo(patente, dni, dias)
    A->>V: verificar disponibilidad
    V-->>A: disponible
    A->>V: marcar_alquilado()
    A->>AL: crear nuevo Alquiler()
    AL-->>A: objeto alquiler
    A-->>UI: Confirmación de éxito
    UI-->>E: Muestra costo y éxito

**Mensaje de commit:** `docs: actualizar README con diagramas UML`[cite: 186].

¡Listo! Con esto el Sprint 1 queda impecable. ¿Querés que hagamos el último paso de este Sprint, que es el archivo de instrucciones de ejecución? [cite: 209-213]
