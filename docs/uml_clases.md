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
