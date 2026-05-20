# Plan de Pruebas: Interfaz (UI)

Este documento detalla los casos de prueba visuales y de interacción con la interfaz gráfica construida en CustomTkinter.

| ID | Componente | Acción | Resultado esperado |
| :--- | :--- | :--- | :--- |
| UI-01 | Botón nav Vehiculos | Clic | Se muestra Page Vehiculos, botón en naranja |
| UI-02 | Botón nav Clientes | Clic | Se muestra PageClientes |
| UI-03 | Botón nav Alquilar | Clic | Se muestra PageAlquilar |
| UI-04 | Botón nav Devolver | Clic | Se muestra PageDevolver |
| UI-05 | Tabla de vehículos | Cargar datos | Filas alternadas, encabezados correctos |
| UI-06 | Tabla PageAlquilar | Clic en fila | Se autocompleta campo PATENTE |
| UI-07 | Tabla PageDevolver | Clic en fila | Se autocompleta PATENTE A DEVOLVER |
| UI-08 | Mensaje de éxito | Acción correcta | Texto en verde |
| UI-09 | Mensaje de error | Acción incorrecta | Texto en rojo |
| UI-10 | Campos vacíos | Submit sin datos | Mensaje de error, no se procesa |
| UI-11 | Ventana principal | Redimensionar | Paneles se adaptan correctamente |
| UI-12 | Header | Cualquier página | "AutoRent" visible siempre |
