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
