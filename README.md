# Sistema Integral de Gestion de Clientes, Servicios y Reservas
## Software FJ | Curso: Programacion 213023 | UNAD

---

## Descripcion general

Este proyecto implementa un sistema integral orientado a objetos desarrollado en Python para la empresa **Software FJ**. El sistema permite gestionar clientes, servicios y reservas sin el uso de bases de datos, aplicando los principios de abstraccion, herencia, polimorfismo, encapsulacion y manejo avanzado de excepciones.

Toda la informacion se administra mediante objetos y listas en memoria. Los errores y eventos relevantes se registran en un archivo de logs (`sistema_fj.log`).

---

## Estructura del proyecto

```
software-fj/
|-- cliente.py       # Clase base abstracta EntidadSistema y clase Cliente
|-- servicio.py      # Clase abstracta Servicio y servicios especializados
|-- reserva.py       # Clase Reserva con confirmacion, cancelacion y procesamiento
|-- main.py          # Punto de entrada principal. Simula 13 operaciones completas
|-- sistema_fj.log   # Archivo de logs generado automaticamente al ejecutar
|-- README.md        # Documentacion del proyecto
```

---

## Arquitectura orientada a objetos

### Clase abstracta `EntidadSistema` (`cliente.py`)
Base del sistema. Obliga a todas las entidades a implementar los metodos `obtener_info()` y `validar()`.

### Clase `Cliente` (`cliente.py`)
Hereda de `EntidadSistema`. Gestiona los datos personales del cliente con encapsulacion completa mediante propiedades. Valida nombre, email, telefono e ID. Incluye metodos para activar y desactivar clientes.

**Excepciones personalizadas:**
- `NombreInvalidoError`
- `EmailInvalidoError`
- `TelefonoInvalidoError`
- `IDClienteInvalidoError`

### Clase abstracta `Servicio` (`servicio.py`)
Define la estructura base de todos los servicios. Declara como abstractos los metodos `calcular_costo()`, `describir_servicio()` y `validar()`.

**Servicios especializados:**
| Clase | Descripcion | Parametro adicional |
|---|---|---|
| `ReservaSala` | Reserva de salas de reunion | `capacidad` (personas) |
| `AlquilerEquipo` | Alquiler de equipos tecnologicos | `tipo_equipo` |
| `AsesoriaEspecializada` | Asesoria con especialista asignado | `especialista` |

**Excepciones personalizadas:**
- `ServicioInvalidoError`
- `CostoInvalidoError`

### Clase `Reserva` (`reserva.py`)
Integra cliente, servicio y duracion. Gestiona el ciclo de vida completo de una reserva: pendiente, confirmada y cancelada. Calcula el costo total segun el tipo de servicio.

**Excepciones personalizadas:**
- `ReservaError`
- `ReservaCanceladaError`
- `ServicioNoDisponibleError`

---

## Manejo de excepciones

El sistema utiliza las siguientes estructuras de manejo de errores:

- `try / except`: captura errores especificos en cada operacion
- `try / except / else`: ejecuta logica adicional solo cuando no hay errores
- `try / except / finally`: garantiza la ejecucion de acciones de cierre independientemente del resultado
- **Encadenamiento de excepciones**: uso de `raise ... from e` para preservar el contexto del error original
- **Excepciones personalizadas**: clases propias que representan errores del dominio del negocio

Cada error capturado se registra automaticamente en `sistema_fj.log` con fecha, hora y nivel de severidad.

---

## Operaciones simuladas en `main.py`

El archivo `main.py` ejecuta **13 operaciones completas** organizadas en cuatro bloques:

### Bloque 1 - Registro de clientes
| # | Descripcion | Resultado esperado |
|---|---|---|
| 1 | Registro de cliente con datos validos | Exito |
| 2 | Registro de cliente con ID personalizado valido | Exito |
| 3 | Intento con nombre que contiene numeros | `NombreInvalidoError` |
| 4 | Intento con email sin formato correcto | `EmailInvalidoError` |

### Bloque 2 - Creacion de servicios
| # | Descripcion | Resultado esperado |
|---|---|---|
| 5 | Creacion de sala de reunion valida | Exito |
| 6 | Creacion de alquiler de equipo valido | Exito |
| 7 | Creacion de asesoria especializada valida | Exito |
| Extra | Intento con costo negativo | `CostoInvalidoError` |

### Bloque 3 - Gestion de reservas
| # | Descripcion | Resultado esperado |
|---|---|---|
| 8 | Reserva de sala confirmada y procesada | Exito con costo calculado |
| 9 | Reserva de equipo con descuento del 10% | Exito con descuento aplicado |
| 10 | Reserva de asesoria con recargo adicional | Exito con recargo aplicado |
| 11 | Intento con duracion negativa | `ReservaError` |
| 12 | Cancelar reserva e intentar procesarla | `ReservaCanceladaError` |
| 13 | Reservar servicio deshabilitado | `ServicioNoDisponibleError` |

### Bloque 4 - Resumen final
Muestra el listado de clientes registrados, servicios disponibles y total de reservas generadas durante la sesion.

---

## Requisitos del sistema

- Python 3.8 o superior
- No se requieren librerias externas

---

## Instrucciones de ejecucion

1. Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd software-fj
```

2. Ejecutar el sistema principal:
```bash
python main.py
```

3. Revisar el archivo de logs generado:
```bash
cat sistema_fj.log
```

---

## Enlace al repositorio

[Repositorio GitHub del proyecto](https://github.com/camilo1999icrf-lgtm/Sistema-SoftwareFJ)

---

## Autores

Proyecto desarrollado de forma colaborativa por el grupo 20 del curso Programacion 213023 - UNAD.

- Ivan Camilo Restrepo Fontalvo
- Yamid Andres Barros Restrepo
- Tania Marcela Pena Castro

---

## Referencias bibliograficas

- Van Rossum, G., & Drake Jr, F. L. (2024). *El tutorial de Python*. Python Software Foundation. https://docs.python.org/es/3.12/tutorial/errors.html

- Cuevas Alvarez, A. (2016). *Python 3: curso practico*. RA-MA Editorial. https://elibro-net.bibliotecavirtual.unad.edu.co/es/ereader/unad/106404?page=373

- Romano, F., Baka, B., & Phillips, D. (2019). *Getting Started with Python: Understand Key Data Structures and Use Python in Object-oriented Programming*. Packt Publishing. https://research-ebsco-com.bibliotecavirtual.unad.edu.co/linkprocessor/plink?id=b41fd66a-1134-3dcd-8dba-90f36451f08d

- Zambrano, J. P. (2025). *Introduccion al uso de GitHub* [Objeto virtual de Informacion OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75876

- Silva, F. D. (2025). *Basics of using GitHub* [Objeto virtual de Informacion OVI]. Repositorio Institucional UNAD. https://repository.unad.edu.co/handle/10596/75882
