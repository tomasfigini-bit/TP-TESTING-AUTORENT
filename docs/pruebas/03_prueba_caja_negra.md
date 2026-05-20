# Plan de Pruebas: Caja Negra

Se prueba desde la perspectiva del usuario. Técnicas: Partición de Equivalencia y Análisis de Valores Límite.

## Partición de Equivalencia - Campo 'Días'

| Partición | Rango/Tipo | Ejemplo | Resultado esperado |
| :--- | :--- | :--- | :--- |
| Inválida negativa | dias < 0 | -1 | Rechazo con error |
| Inválida cero | dias = 0 | 0 | Rechazo con error |
| Válida | dias >= 1 | 5 | Aceptado |
| Inválida (no entero) | string | "abc" | Rechazo con error |

## Análisis de Valores Límite - Campo 'Días'

| ID | Valor | Resultado esperado |
| :--- | :--- | :--- |
| CN-01 | dias = -1 | Error |
| CN-02 | dias = 0 | Error |
| CN-03 | dias = 1 | Aceptado (mínimo válido) |
| CN-04 | dias = 2 | Aceptado |
| CN-05 | dias = 365 | Aceptado |
