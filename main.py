# Sistema de Gestion - Software FJ
# Archivo: main.py
# Punto de entrada principal del sistema. Simula mas de 10 operaciones completas
# incluyendo registros validos e invalidos de clientes, creacion de servicios
# y reservas exitosas y fallidas, con manejo robusto de excepciones.

import logging
import os
from datetime import datetime

# Importacion de clases del sistema
from cliente import (
    Cliente,
    NombreInvalidoError,
    EmailInvalidoError,
    TelefonoInvalidoError,
    IDClienteInvalidoError
)

from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada,
    ServicioInvalidoError,
    CostoInvalidoError
)

from reserva import (
    Reserva,
    ReservaError,
    ReservaCanceladaError,
    ServicioNoDisponibleError
)


# CONFIGURACION DEL SISTEMA DE LOGS
# Todos los eventos y errores se registran en sistema_fj.log

def configurar_logs():
    """
    Configura el archivo de logs del sistema.
    Registra fecha, nivel de severidad y mensaje de cada evento.
    """
    logging.basicConfig(
        filename="sistema_fj.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    logging.info("=" * 60)
    logging.info("INICIO DE SESION - Sistema Software FJ")
    logging.info("=" * 60)


def registrar_evento(mensaje: str):
    """Registra un evento informativo en el archivo de logs."""
    logging.info(mensaje)


def registrar_error(mensaje: str):
    """Registra un error en el archivo de logs."""
    logging.error(mensaje)


# SEPARADORES VISUALES

def separador(titulo: str = ""):
    """Imprime una linea separadora con titulo opcional."""
    if titulo:
        print(f"\n{'=' * 55}")
        print(f"  {titulo}")
        print(f"{'=' * 55}")
    else:
        print(f"{'=' * 55}")


def imprimir_resultado(exito: bool, mensaje: str):
    """Imprime el resultado de una operacion con icono de estado."""
    icono = "[OK]" if exito else "[ERROR]"
    print(f"  {icono} {mensaje}")


# BLOQUE 1: REGISTRO DE CLIENTES
# Operaciones 1-4: clientes validos e invalidos

def bloque_clientes():
    """
    Simula el registro de clientes en el sistema.
    Incluye casos validos e invalidos para demostrar validaciones.
    """
    separador("BLOQUE 1 - REGISTRO DE CLIENTES")

    clientes_creados = []

    # Operacion 1: registro de cliente valido
    print("\n  Operacion 1: Registro de cliente valido")
    try:
        c1 = Cliente("Carlos Mendoza", "carlos.mendoza@email.com", "3001234567")
        clientes_creados.append(c1)
        imprimir_resultado(True, f"Cliente creado: {c1}")
        registrar_evento(f"Cliente registrado exitosamente: {c1}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error al registrar cliente: {e}")

    # Operacion 2: registro de segundo cliente valido
    print("\n  Operacion 2: Registro de cliente valido con ID personalizado")
    try:
        c2 = Cliente("Laura Sanchez", "laura.sanchez@softwarefj.com", "+573157654321", "CLI-010")
        clientes_creados.append(c2)
        imprimir_resultado(True, f"Cliente creado: {c2}")
        registrar_evento(f"Cliente registrado exitosamente: {c2}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error al registrar cliente con ID personalizado: {e}")

    # Operacion 3: intento con nombre invalido
    print("\n  Operacion 3: Intento de registro con nombre invalido")
    try:
        c3 = Cliente("12345", "test@email.com", "3009876543")
        clientes_creados.append(c3)
    except NombreInvalidoError as e:
        imprimir_resultado(False, f"NombreInvalidoError capturado: {e}")
        registrar_error(f"Intento de registro con nombre invalido: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado en registro de cliente: {e}")
    else:
        imprimir_resultado(True, "Cliente registrado (no se esperaba exito aqui)")
    finally:
        print("  [LOG] Operacion 3 finalizada.")

    # Operacion 4: intento con email invalido
    print("\n  Operacion 4: Intento de registro con email invalido")
    try:
        c4 = Cliente("Pedro Ramirez", "correo_sin_arroba", "3002345678")
        clientes_creados.append(c4)
    except EmailInvalidoError as e:
        imprimir_resultado(False, f"EmailInvalidoError capturado: {e}")
        registrar_error(f"Intento de registro con email invalido: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado en registro de cliente: {e}")
    else:
        imprimir_resultado(True, "Cliente registrado (no se esperaba exito aqui)")
    finally:
        print("  [LOG] Operacion 4 finalizada.")

    return clientes_creados


# BLOQUE 2: CREACION DE SERVICIOS
# Operaciones 5-7: servicios validos e invalidos

def bloque_servicios():
    """
    Simula la creacion de servicios del sistema.
    Incluye los tres tipos disponibles y casos de error.
    """
    separador("BLOQUE 2 - CREACION DE SERVICIOS")

    servicios_creados = []

    # Operacion 5: creacion de sala de reunion valida
    print("\n  Operacion 5: Creacion de sala de reunion valida")
    try:
        sala = ReservaSala("Sala Ejecutiva", 120000, 20)
        servicios_creados.append(sala)
        imprimir_resultado(True, f"Servicio creado: {sala}")
        imprimir_resultado(True, f"Descripcion: {sala.describir_servicio()}")
        registrar_evento(f"Servicio creado: {sala}")
    except ServicioInvalidoError as e:
        imprimir_resultado(False, f"ServicioInvalidoError: {e}")
        registrar_error(f"Error al crear sala: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado al crear sala: {e}")

    # Operacion 6: creacion de alquiler de equipo valido
    print("\n  Operacion 6: Creacion de alquiler de equipo valido")
    try:
        equipo = AlquilerEquipo("Portatil Gamer", 80000, "Laptop")
        servicios_creados.append(equipo)
        imprimir_resultado(True, f"Servicio creado: {equipo}")
        imprimir_resultado(True, f"Descripcion: {equipo.describir_servicio()}")
        registrar_evento(f"Servicio creado: {equipo}")
    except ServicioInvalidoError as e:
        imprimir_resultado(False, f"ServicioInvalidoError: {e}")
        registrar_error(f"Error al crear equipo: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado al crear equipo: {e}")

    # Operacion 7: creacion de asesoria especializada valida
    print("\n  Operacion 7: Creacion de asesoria especializada valida")
    try:
        asesoria = AsesoriaEspecializada("Ciberseguridad Avanzada", 150000, "Ingeniero Senior")
        servicios_creados.append(asesoria)
        imprimir_resultado(True, f"Servicio creado: {asesoria}")
        imprimir_resultado(True, f"Descripcion: {asesoria.describir_servicio()}")
        registrar_evento(f"Servicio creado: {asesoria}")
    except ServicioInvalidoError as e:
        imprimir_resultado(False, f"ServicioInvalidoError: {e}")
        registrar_error(f"Error al crear asesoria: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado al crear asesoria: {e}")

    # Operacion adicional: intento de servicio con costo invalido
    print("\n  Operacion extra: Intento de servicio con costo negativo")
    try:
        sala_invalida = ReservaSala("Sala Invalida", -5000, 10)
    except CostoInvalidoError as e:
        imprimir_resultado(False, f"CostoInvalidoError capturado: {e}")
        registrar_error(f"Intento de crear servicio con costo negativo: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado al validar costo: {e}")
    else:
        imprimir_resultado(True, "Servicio creado (no se esperaba exito aqui)")
    finally:
        print("  [LOG] Operacion de servicio invalido finalizada.")

    return servicios_creados


# BLOQUE 3: GESTION DE RESERVAS
# Operaciones 8-12: reservas exitosas, fallidas y canceladas

def bloque_reservas(clientes: list, servicios: list):
    """
    Simula la creacion, confirmacion, procesamiento y cancelacion de reservas.
    Requiere listas de clientes y servicios previamente creados.

    Args:
        clientes: lista de objetos Cliente validos
        servicios: lista de objetos Servicio validos
    """
    separador("BLOQUE 3 - GESTION DE RESERVAS")

    # Verificacion de datos minimos necesarios
    if len(clientes) < 1 or len(servicios) < 3:
        print("\n  [ADVERTENCIA] No hay suficientes clientes o servicios para simular reservas.")
        registrar_error("Simulacion de reservas omitida por falta de datos validos.")
        return

    cliente = clientes[0]
    sala = servicios[0]
    equipo = servicios[1]
    asesoria = servicios[2]

    # Operacion 8: reserva exitosa de sala con confirmacion y procesamiento
    print("\n  Operacion 8: Reserva exitosa de sala (confirmar y procesar)")
    try:
        r1 = Reserva(cliente, sala, 3)
        r1.confirmar()
        costo = r1.procesar()
        imprimir_resultado(True, f"Reserva creada y procesada. Costo: ${costo:,.2f}")
        print(r1.obtener_info())
        registrar_evento(f"Reserva {r1.id_reserva} procesada. Costo: ${costo:,.2f}")
    except ReservaError as e:
        imprimir_resultado(False, f"ReservaError: {e}")
        registrar_error(f"Error en reserva de sala: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado en reserva de sala: {e}")

    # Operacion 9: reserva de equipo con descuento aplicado
    print("\n  Operacion 9: Reserva de equipo con descuento del 10%")
    try:
        r2 = Reserva(cliente, equipo, 5)
        r2.confirmar()
        costo = equipo.calcular_costo(dias=5, descuento=0.10)
        imprimir_resultado(True, f"Reserva confirmada. Costo con descuento: ${costo:,.2f}")
        registrar_evento(f"Reserva de equipo confirmada con descuento. Costo: ${costo:,.2f}")
    except ReservaError as e:
        imprimir_resultado(False, f"ReservaError: {e}")
        registrar_error(f"Error en reserva de equipo: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado en reserva de equipo: {e}")

    # Operacion 10: reserva de asesoria con recargo
    print("\n  Operacion 10: Reserva de asesoria con recargo adicional")
    try:
        r3 = Reserva(cliente, asesoria, 2)
        r3.confirmar()
        costo = asesoria.calcular_costo(horas=2, recargo=50000)
        imprimir_resultado(True, f"Asesoria confirmada. Costo con recargo: ${costo:,.2f}")
        registrar_evento(f"Reserva de asesoria confirmada con recargo. Costo: ${costo:,.2f}")
    except ReservaError as e:
        imprimir_resultado(False, f"ReservaError: {e}")
        registrar_error(f"Error en reserva de asesoria: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado en reserva de asesoria: {e}")

    # Operacion 11: intento de reserva con duracion invalida
    print("\n  Operacion 11: Intento de reserva con duracion invalida")
    try:
        r4 = Reserva(cliente, sala, -2)
    except ReservaError as e:
        imprimir_resultado(False, f"ReservaError capturado: {e}")
        registrar_error(f"Intento de reserva con duracion invalida: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado con duracion invalida: {e}")
    else:
        imprimir_resultado(True, "Reserva creada (no se esperaba exito aqui)")
    finally:
        print("  [LOG] Operacion 11 finalizada.")

    # Operacion 12: cancelacion de reserva e intento de procesarla
    print("\n  Operacion 12: Cancelar reserva e intentar procesarla")
    try:
        r5 = Reserva(cliente, asesoria, 1)
        r5.cancelar()
        registrar_evento(f"Reserva {r5.id_reserva} cancelada por el usuario.")

        try:
            r5.procesar()
        except ReservaError as e:
            imprimir_resultado(False, f"ReservaError al procesar cancelada: {e}")
            registrar_error(f"Intento de procesar reserva cancelada: {e}")

    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado en cancelacion de reserva: {e}")

    # Operacion 13: intento de reservar un servicio deshabilitado
    print("\n  Operacion 13: Intento de reserva con servicio deshabilitado")
    try:
        sala.deshabilitar()
        registrar_evento(f"Servicio '{sala.nombre}' deshabilitado.")
        r6 = Reserva(cliente, sala, 2)
    except ServicioNoDisponibleError as e:
        imprimir_resultado(False, f"ServicioNoDisponibleError capturado: {e}")
        registrar_error(f"Intento de reserva con servicio no disponible: {e}")
    except ReservaError as e:
        imprimir_resultado(False, f"ReservaError: {e}")
        registrar_error(f"ReservaError con servicio deshabilitado: {e}")
    except Exception as e:
        imprimir_resultado(False, f"Error inesperado: {e}")
        registrar_error(f"Error inesperado con servicio deshabilitado: {e}")
    finally:
        sala.habilitar()
        registrar_evento(f"Servicio '{sala.nombre}' habilitado nuevamente.")
        print("  [LOG] Servicio restaurado al estado disponible.")


# BLOQUE 4: RESUMEN FINAL DEL SISTEMA

def mostrar_resumen(clientes: list, servicios: list):
    """
    Muestra un resumen general de los objetos activos en el sistema.

    Args:
        clientes: lista de clientes registrados exitosamente
        servicios: lista de servicios creados exitosamente
    """
    separador("RESUMEN FINAL DEL SISTEMA")

    print(f"\n  Clientes registrados: {len(clientes)}")
    for c in clientes:
        print(f"    - {c}")

    print(f"\n  Servicios disponibles: {len(servicios)}")
    for s in servicios:
        estado = "Disponible" if s.disponible else "No disponible"
        print(f"    - {s} | Estado: {estado}")

    print(f"\n  Reservas generadas: {Reserva._contador}")
    print(f"  Archivo de logs: sistema_fj.log")

    registrar_evento("Resumen final mostrado. Sistema finalizado correctamente.")
    separador()


# FUNCION PRINCIPAL

def main():
    """
    Funcion principal del sistema Software FJ.
    Ejecuta de forma secuencial todos los bloques de operaciones
    y garantiza el registro de eventos y errores en el archivo de logs.
    """
    # Configuracion inicial del sistema de logs
    configurar_logs()

    # Encabezado del sistema
    separador()
    print("  SISTEMA INTEGRAL DE GESTION - SOFTWARE FJ")
    print(f"  Fecha de ejecucion: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    separador()

    # Ejecucion de bloques del sistema con manejo de excepciones globales
    try:
        clientes = bloque_clientes()
    except Exception as e:
        print(f"\n  [CRITICO] Error en bloque de clientes: {e}")
        registrar_error(f"Error critico en bloque de clientes: {e}")
        clientes = []

    try:
        servicios = bloque_servicios()
    except Exception as e:
        print(f"\n  [CRITICO] Error en bloque de servicios: {e}")
        registrar_error(f"Error critico en bloque de servicios: {e}")
        servicios = []

    try:
        bloque_reservas(clientes, servicios)
    except Exception as e:
        print(f"\n  [CRITICO] Error en bloque de reservas: {e}")
        registrar_error(f"Error critico en bloque de reservas: {e}")

    # Resumen final
    mostrar_resumen(clientes, servicios)

    print("\n  Sistema finalizado correctamente.")
    print("  Revise el archivo sistema_fj.log para ver el registro completo.\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
