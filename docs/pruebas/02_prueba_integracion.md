# Plan de Pruebas: Integración

Este documento verifica la interacción correcta entre las distintas clases del sistema (Agencia, Vehiculo, Cliente, Alquiler).

| ID | Flujo | Resultado esperado |
| :--- | :--- | :--- |
| PI-01 | Registro y búsqueda de vehículo | Retorna el objeto Vehiculo correcto |
| PI-02 | Registro duplicado de vehículo | ValueError en el segundo intento |
| PI-03 | Registro y búsqueda de cliente | Retorna el objeto Cliente correcto |
| PI-04 | Flujo completo de alquiler | Vehículo alquilado, Alquiler en lista |
| PI-05 | Alquilar vehículo no disponible | ValueError: no esta disponible |
| PI-06 | Alquilar con vehículo inexistente | ValueError: no encontrado |
| PI-07 | Alquilar con cliente inexistente | ValueError: no encontrado |
| PI-08 | Flujo completo de devolución | Vehículo disponible, alquiler removido |
| PI-09 | Devolver vehículo sin alquiler activo | ValueError: no tiene alquiler activo |
| PI-10 | Costo calculado en integración | 5 dias x $8500 = $42500 |
