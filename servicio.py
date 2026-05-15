# sistema de gestión - software fj
# archivo: servicio.py
# aquí definimos la clase abstracta servicio y sus diferentes tipos

from abc import ABC, abstractmethod


# excepciones personalizadas para los servicios

class ServicioInvalidoError(Exception):
    pass


class CostoInvalidoError(Exception):
    pass

class DuracionInvalidaError(Exception):
    pass


# clase abstracta servicio

class Servicio(ABC):

    # contador para generar ids automáticos
    _contador = 0

    def __init__(self, nombre: str, costo_base: float):

        # aumento automático del contador
        Servicio._contador += 1

        # generación automática del id
        self.__id_servicio = f"SER-{Servicio._contador:03d}"

        # asignación usando setters
        self.nombre = nombre
        self.costo_base = costo_base

        # estado inicial del servicio
        self.__disponible = True

    # getter del id del servicio
    @property
    def id_servicio(self):
        return self.__id_servicio

    # getter del nombre
    @property
    def nombre(self):
        return self.__nombre

    # setter del nombre
    @nombre.setter
    def nombre(self, valor: str):

        try:

            # validación de campo vacío
            if not valor or not valor.strip():
                raise ServicioInvalidoError(
                    "el nombre del servicio no puede estar vacío."
                )

            # validación de longitud mínima
            if len(valor.strip()) < 3:
                raise ServicioInvalidoError(
                    "el nombre del servicio es demasiado corto."
                )

            # guardado del nombre formateado
            self.__nombre = valor.strip().title()

        except ServicioInvalidoError:
            raise

        except Exception as e:
            raise ServicioInvalidoError(
                f"error al validar el nombre: {e}"
            ) from e

    # getter del costo base
    @property
    def costo_base(self):
        return self.__costo_base

    # setter del costo base
    @costo_base.setter
    def costo_base(self, valor: float):

        try:

            # conversión del valor
            valor = float(valor)

            # validación del costo
            if valor <= 0:
                raise CostoInvalidoError(
                    "el costo debe ser mayor que cero."
                )

            # guardado del costo
            self.__costo_base = valor

        except ValueError as e:
            raise CostoInvalidoError(
                "el costo debe ser numérico."
            ) from e

        except CostoInvalidoError:
            raise

        except Exception as e:
            raise CostoInvalidoError(
                f"error al validar el costo: {e}"
            ) from e

    # getter del estado disponible
    @property
    def disponible(self):
        return self.__disponible

    # método para deshabilitar el servicio
    def deshabilitar(self):
        self.__disponible = False
        print(f"servicio '{self.__nombre}' deshabilitado.")

    # método para habilitar nuevamente el servicio
    def habilitar(self):
        self.__disponible = True
        print(f"servicio '{self.__nombre}' habilitado.")

    # método abstracto para calcular costos
    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    # método abstracto para describir servicios
    @abstractmethod
    def describir_servicio(self):
        pass

    # método abstracto de validación
    @abstractmethod
    def validar(self):
        pass


# clase hija para reserva de salas

class ReservaSala(Servicio):

    def __init__(self, nombre, costo_base, capacidad):

        # llamado al constructor padre
        super().__init__(nombre, costo_base)

        # asignación de capacidad
        self.capacidad = capacidad

    # getter de capacidad
    @property
    def capacidad(self):
        return self.__capacidad

    # setter de capacidad
    @capacidad.setter
    def capacidad(self, valor):

        try:

            # conversión del valor
            valor = int(valor)

            # validación de capacidad
            if valor <= 0:
                raise ServicioInvalidoError(
                    "la capacidad debe ser mayor que cero."
                )

            # guardado de capacidad
            self.__capacidad = valor

        except ValueError as e:
            raise ServicioInvalidoError(
                "la capacidad debe ser numérica."
            ) from e

    # cálculo del costo del servicio
    def calcular_costo(self, horas=1, impuesto=0):

        subtotal = self.costo_base * horas
        total = subtotal + (subtotal * impuesto)

        return total

    # descripción del servicio
    def describir_servicio(self):

        return (
            f"sala con capacidad para "
            f"{self.__capacidad} personas."
        )

    # validación general del servicio
    def validar(self):

        return (
            self.__capacidad > 0 and
            self.disponible
        )

    # representación corta del objeto
    def __str__(self):

        return (
            f"ReservaSala("
            f"{self.id_servicio} - "
            f"{self.nombre})"
        )


# clase hija para alquiler de equipos

class AlquilerEquipo(Servicio):

    def __init__(self, nombre, costo_base, tipo_equipo):

        # llamado al constructor padre
        super().__init__(nombre, costo_base)

        # asignación del tipo de equipo
        self.tipo_equipo = tipo_equipo

    # getter del tipo de equipo
    @property
    def tipo_equipo(self):
        return self.__tipo_equipo

    # setter del tipo de equipo
    @tipo_equipo.setter
    def tipo_equipo(self, valor):

        try:

            # validación del campo
            if not valor or not valor.strip():
                raise ServicioInvalidoError(
                    "el tipo de equipo no puede estar vacío."
                )

            # guardado del tipo de equipo
            self.__tipo_equipo = valor.strip().title()

        except ServicioInvalidoError:
            raise

    # cálculo del costo del alquiler
    def calcular_costo(self, dias=1, descuento=0):

        subtotal = self.costo_base * dias
        total = subtotal - (subtotal * descuento)

        return total

    # descripción del servicio
    def describir_servicio(self):

        return (
            f"alquiler de equipos tipo "
            f"{self.__tipo_equipo}."
        )

    # validación general
    def validar(self):

        return (
            bool(self.__tipo_equipo) and
            self.disponible
        )

    # representación corta del objeto
    def __str__(self):

        return (
            f"AlquilerEquipo("
            f"{self.id_servicio} - "
            f"{self.nombre})"
        )


# clase hija para asesorías especializadas

class AsesoriaEspecializada(Servicio):

    def __init__(self, nombre, costo_base, especialista):

        # llamado al constructor padre
        super().__init__(nombre, costo_base)

        # asignación del especialista
        self.especialista = especialista

    # getter del especialista
    @property
    def especialista(self):
        return self.__especialista

    # setter del especialista
    @especialista.setter
    def especialista(self, valor):

        try:

            # validación del especialista
            if not valor or not valor.strip():
                raise ServicioInvalidoError(
                    "el especialista no puede estar vacío."
                )

            # guardado del especialista
            self.__especialista = valor.strip().title()

        except ServicioInvalidoError:
            raise

    # cálculo del costo de asesoría
    def calcular_costo(self, horas=1, recargo=0):

        subtotal = self.costo_base * horas
        total = subtotal + recargo

        return total

    # descripción del servicio
    def describir_servicio(self):

        return (
            f"asesoría especializada realizada por "
            f"{self.__especialista}."
        )

    # validación general
    def validar(self):

        return (
            bool(self.__especialista) and
            self.disponible
        )

    # representación corta del objeto
    def __str__(self):

        return (
            f"AsesoriaEspecializada("
            f"{self.id_servicio} - "
            f"{self.nombre})"
        )


# pruebas del sistema

if __name__ == "__main__":

    print("\n" + "=" * 50)
    print("pruebas del módulo de servicios")
    print("=" * 50)

    try:

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

        # impresión de servicios
        print(sala)
        print(equipo)
        print(asesoria)

        # pruebas de costos
        print("\ncostos calculados:")

        print(
            sala.calcular_costo(
                horas=2,
                impuesto=0.19
            )
        )

        print(
            equipo.calcular_costo(
                dias=3,
                descuento=0.10
            )
        )

        print(
            asesoria.calcular_costo(
                horas=2,
                recargo=50000
            )
        )

    except Exception as e:
        print(f"error: {e}")

    print("=" * 50)
