# AutoRent — Sistema de Alquiler de Vehículos

## Objetivo del Software
AutoRent es una aplicación de escritorio diseñada para gestionar de manera eficiente el alquiler de vehículos, permitiendo el control de la flota, el registro de clientes y la automatización de los cálculos de costos de alquiler.

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

## Requerimientos No Funcionales
| ID | Requerimiento | Tipo |
|:---:|---|:---:|
| RNF01 | Interfaz gráfica de escritorio (CustomTkinter) | No Funcional |
| RNF02 | Validación de datos en todos los formularios | No Funcional |
| RNF03 | Feedback visual inmediato ante errores o éxitos | No Funcional |
| RNF04 | El sistema debe ejecutarse en Python 3.10+ | No Funcional |
| RNF05 | Navegación por secciones sin recargar la aplicación | No Funcional |

## Tecnologías utilizadas
* Python 3.10+
* CustomTkinter para la interfaz gráfica.

## Estructura del proyecto
El código fuente se divide en cuatro módulos principales: `modelo.py`, `componentes.py`, `ui.py` y `main.py`.

## Cómo ejecutar
Las instrucciones detalladas se encuentran en el archivo `docs/como_ejecutar.md`.
