# Plan de Pruebas: Rendimiento

Este documento detalla los escenarios de prueba para verificar los tiempos de respuesta y el comportamiento del sistema bajo carga usando el módulo `time` de Python.

| ID | Escenario | Métrica objetivo | Resultado esperado |
| :--- | :--- | :--- | :--- |
| PR-01 | Registrar 1000 vehículos | < 1 segundo total | Sin errores |
| PR-02 | Registrar 1000 clientes | < 1 segundo total | Sin errores |
| PR-03 | Listar 1000 vehículos | < 100ms | Lista completa |
| PR-04 | Buscar vehículo en lista de 1000 (peor caso) | 50ms | Encuentra correcto |
| PR-05 | 500 alquileres secuenciales | < 2 segundos | Todos registrados |
| PR-06 | Tabla UI con 100 filas. | Respuesta visual < 1s | Sin freeze de UI |
