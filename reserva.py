# sistema de gestión - software fj
# archivo: reserva.py
# aquí definimos todo lo relacionado con las reservas

from datetime import datetime

# importación de excepciones necesarias
from servicio import (
    DuracionInvalidaError
)


# excepciones personalizadas para reservas

class ReservaError(Exception):
    pass


class ReservaCanceladaError(Exception):
    pass


class ServicioNoDisponibleError(Exception):
    pass


# clase reserva

class Reserva:

    # contador para generar ids automáticos
    _contador = 0

    def __init__(self, cliente, servicio, duracion):

        try:

            # aumento automático del contador
            Reserva._contador += 1

            # generación automática del id
            self.__id_reserva = f"RES-{Reserva._contador:03d}"

            # asignación usando setters
            self.cliente = cliente
            self.servicio = servicio
            self.duracion = duracion

            # estado inicial de la reserva
            self.__estado = "pendiente"

            # fecha automática de creación
            self.__fecha = datetime.now()

        except Exception as e:
            raise ReservaError(
                f"no fue posible crear la reserva: {e}"
            ) from e

    # getter del id
    @property
    def id_reserva(self):
        return self.__id_reserva

    # getter del cliente
    @property
    def cliente(self):
        return self.__cliente

    # setter del cliente
    @cliente.setter
    def cliente(self, valor):

        try:

            # validación del cliente
            if valor is None:
                raise ReservaError(
                    "la reserva debe tener un cliente válido."
                )

            # guardado del cliente
            self.__cliente = valor

        except ReservaError:
            raise

    # getter del servicio
    @property
    def servicio(self):
        return self.__servicio

    # setter del servicio
    @servicio.setter
    def servicio(self, valor):

        try:

            # validación del servicio
            if valor is None:
                raise ReservaError(
                    "la reserva debe tener un servicio válido."
                )

            # validación de disponibilidad
            if not valor.disponible:
                raise ServicioNoDisponibleError(
                    "el servicio no está disponible."
                )

            # guardado del servicio
            self.__servicio = valor

        except ServicioNoDisponibleError:
            raise

    # getter de duración
    @property
    def duracion(self):
        return self.__duracion

    # setter de duración
    @duracion.setter
    def duracion(self, valor):

        try:

            # conversión del valor
            valor = int(valor)

            # validación de duración
            if valor <= 0:
                raise DuracionInvalidaError(
                    "la duración debe ser mayor que cero."
                )

            # guardado de duración
            self.__duracion = valor

        except ValueError as e:
            raise DuracionInvalidaError(
                "la duración debe ser numérica."
            ) from e

    # getter del estado
    @property
    def estado(self):
        return self.__estado

    # método para confirmar reservas
    def confirmar(self):

        try:

            # validación del estado
            if self.__estado == "cancelada":
                raise ReservaCanceladaError(
                    "no puede confirmarse una reserva cancelada."
                )

            # cambio de estado
            self.__estado = "confirmada"

            print(
                f"reserva {self.__id_reserva} confirmada."
            )

        except ReservaCanceladaError:
            raise

    # método para cancelar reservas
    def cancelar(self):

        # cambio de estado
        self.__estado = "cancelada"

        print(
            f"reserva {self.__id_reserva} cancelada."
        )

    # método para procesar reservas
    def procesar(self):

        try:

            # validación de cancelación
            if self.__estado == "cancelada":
                raise ReservaCanceladaError(
                    "no puede procesarse una reserva cancelada."
                )

            # cálculo del costo
            costo = self.__servicio.calcular_costo(
                self.__duracion
            )

            print("reserva procesada correctamente.")
            print(f"costo total: ${costo:,.2f}")

            return costo

        except Exception as e:
            raise ReservaError(
                f"error al procesar la reserva: {e}"
            ) from e

    # método para mostrar información
    def obtener_info(self):

        return (
            f"{'=' * 45}\n"
            f"información de la reserva\n"
            f"{'=' * 45}\n"
            f"id reserva : {self.__id_reserva}\n"
            f"cliente    : {self.__cliente.nombre}\n"
            f"servicio   : {self.__servicio.nombre}\n"
            f"duración   : {self.__duracion}\n"
            f"estado     : {self.__estado}\n"
            f"fecha      : "
            f"{self.__fecha.strftime('%d/%m/%Y %H:%M')}\n"
            f"{'=' * 45}"
        )

    # representación corta del objeto
    def __str__(self):

        return (
            f"Reserva("
            f"{self.__id_reserva} - "
            f"{self.__cliente.nombre} - "
            f"{self.__servicio.nombre})"
        )


# pruebas del sistema

if __name__ == "__main__":

    # importación de clases necesarias
    from cliente import Cliente

    from servicio import (
        ReservaSala,
        AlquilerEquipo,
        AsesoriaEspecializada
    )

    print("\n" + "=" * 50)
    print("pruebas del módulo de reservas")
    print("=" * 50)

    try:

        # creación del cliente
        cliente1 = Cliente(
            "iván restrepo",
            "ivan@email.com",
            "3001234567"
        )

        # creación de servicios
        sala = ReservaSala(
            "sala premium",
            120000,
            20
        )

        equipo = AlquilerEquipo(
            "portátil gamer",
            80000,
            "laptop"
        )

        asesoria = AsesoriaEspecializada(
            "ciberseguridad",
            150000,
            "ingeniero senior"
        )

        # creación de reservas
        r1 = Reserva(
            cliente1,
            sala,
            2
        )

        r2 = Reserva(
            cliente1,
            equipo,
            3
        )

        # confirmación de reservas
        r1.confirmar()
        r2.confirmar()

        # procesamiento de reservas
        r1.procesar()
        r2.procesar()

        # impresión de información
        print("\n")
        print(r1.obtener_info())

        # cancelación de reserva
        reserva_cancelada = Reserva(
            cliente1,
            asesoria,
            1
        )

        reserva_cancelada.cancelar()

        try:

            # intento de procesar reserva cancelada
            reserva_cancelada.procesar()

        except ReservaError as e:
            print(f"error controlado: {e}")

    except Exception as e:
        print(f"error inesperado: {e}")

    print("=" * 50)
