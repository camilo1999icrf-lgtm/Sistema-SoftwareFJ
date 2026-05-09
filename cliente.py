# Sistema de Gestión - Software FJ
# Archivo: cliente.py
# Aquí definimos la clase base del sistema y todo lo relacionado con clientes

import re  # Lo usamos para validar formatos como emails y teléfonos


# Excepciones personalizadas para el manejo de errores del cliente
# Cada una representa un tipo de error específico que puede ocurrir

class NombreInvalidoError(Exception):
    """Se lanza cuando el nombre del cliente no es válido."""
    pass


class EmailInvalidoError(Exception):
    """Se lanza cuando el correo electrónico no tiene buen formato."""
    pass


class TelefonoInvalidoError(Exception):
    """Se lanza cuando el número de teléfono no es correcto."""
    pass


class IDClienteInvalidoError(Exception):
    """Se lanza cuando el ID del cliente no cumple el formato esperado."""
    pass


# Clase abstracta base: EntidadSistema
# Toda clase del sistema debe heredar de esta para mantener consistencia

from abc import ABC, abstractmethod


class EntidadSistema(ABC):
    """
    Clase abstracta que representa cualquier entidad dentro del sistema.
    Obliga a las clases hijas a implementar obtener_info() y validar().
    """

    @abstractmethod
    def obtener_info(self):
        """Cada entidad debe poder mostrar su propia información."""
        pass

    @abstractmethod
    def validar(self):
        """Cada entidad debe poder verificar si sus datos son correctos."""
        pass


# Clase Cliente
# Hereda de EntidadSistema y aplica encapsulación con getters y setters

class Cliente(EntidadSistema):
    """
    Representa a un cliente de Software FJ.

    Todos los atributos son privados y se acceden mediante propiedades,
    lo que nos permite validar los datos cada vez que se asignan.

    Atributos:
        __id_cliente: identificador único, ej: CLI-001
        __nombre: nombre completo del cliente
        __email: correo electrónico
        __telefono: número de contacto
        __activo: indica si el cliente está activo en el sistema
    """

    # Este contador nos ayuda a generar IDs automáticos para cada cliente
    _contador = 0

    def __init__(self, nombre: str, email: str, telefono: str, id_cliente: str = None):
        """
        Crea un nuevo cliente validando todos sus datos desde el inicio.
        Si no se proporciona un ID, se genera uno automáticamente.
        """
        Cliente._contador += 1

        # Usamos los setters directamente para que las validaciones se ejecuten
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

        # Si no nos pasan un ID, lo generamos nosotros (ej: CLI-001, CLI-002...)
        if id_cliente is None:
            self.__id_cliente = f"CLI-{Cliente._contador:03d}"
        else:
            self.id_cliente = id_cliente

        # Por defecto todo cliente nuevo entra como activo
        self.__activo = True

    # Getters y setters — aquí es donde ocurre la encapsulación

    @property
    def id_cliente(self):
        """Retorna el ID del cliente."""
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor: str):
        """
        Valida que el ID tenga el formato correcto antes de asignarlo.
        El formato esperado es CLI-XXX, por ejemplo CLI-001.
        """
        try:
            if not valor or not valor.strip():
                raise IDClienteInvalidoError("El ID no puede estar vacío.")

            patron = r'^CLI-\d{3,}$'
            if not re.match(patron, valor.strip()):
                raise IDClienteInvalidoError(
                    f"El ID '{valor}' no es válido. El formato correcto es CLI-XXX (ej: CLI-001)."
                )

            self.__id_cliente = valor.strip().upper()

        except IDClienteInvalidoError:
            raise
        except Exception as e:
            raise IDClienteInvalidoError(f"Ocurrió un error al validar el ID: {e}") from e

    @property
    def nombre(self):
        """Retorna el nombre del cliente."""
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str):
        """
        Verifica que el nombre no esté vacío, sea suficientemente largo
        y solo contenga letras y espacios.
        """
        try:
            if not valor or not valor.strip():
                raise NombreInvalidoError("El nombre no puede estar vacío.")

            if len(valor.strip()) < 3:
                raise NombreInvalidoError(
                    f"'{valor}' es muy corto. El nombre debe tener al menos 3 caracteres."
                )

            patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$'
            if not re.match(patron, valor.strip()):
                raise NombreInvalidoError(
                    f"'{valor}' contiene caracteres no permitidos. Solo se aceptan letras y espacios."
                )

            # Guardamos el nombre con mayúscula inicial en cada palabra
            self.__nombre = valor.strip().title()

        except NombreInvalidoError:
            raise
        except Exception as e:
            raise NombreInvalidoError(f"Ocurrió un error al validar el nombre: {e}") from e

    @property
    def email(self):
        """Retorna el email del cliente."""
        return self.__email

    @email.setter
    def email(self, valor: str):
        """
        Verifica que el email tenga un formato válido antes de guardarlo.
        Por ejemplo: usuario@dominio.com
        """
        try:
            if not valor or not valor.strip():
                raise EmailInvalidoError("El email no puede estar vacío.")

            patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
            if not re.match(patron, valor.strip()):
                raise EmailInvalidoError(
                    f"'{valor}' no parece un email válido. Ejemplo correcto: usuario@dominio.com"
                )

            # Guardamos el email en minúsculas para evitar duplicados por capitalización
            self.__email = valor.strip().lower()

        except EmailInvalidoError:
            raise
        except Exception as e:
            raise EmailInvalidoError(f"Ocurrió un error al validar el email: {e}") from e

    @property
    def telefono(self):
        """Retorna el teléfono del cliente."""
        return self.__telefono

    @telefono.setter
    def telefono(self, valor: str):
        """
        Acepta números con o sin código de país y con o sin guiones.
        Al guardarlo lo dejamos solo con dígitos para uniformidad.
        """
        try:
            if not valor or not valor.strip():
                raise TelefonoInvalidoError("El teléfono no puede estar vacío.")

            # Quitamos espacios, guiones y paréntesis antes de validar
            telefono_limpio = re.sub(r'[\s\-\(\)]', '', valor.strip())

            patron = r'^(\+?\d{10,13})$'
            if not re.match(patron, telefono_limpio):
                raise TelefonoInvalidoError(
                    f"'{valor}' no es un teléfono válido. Debe tener entre 10 y 13 dígitos."
                )

            self.__telefono = telefono_limpio

        except TelefonoInvalidoError:
            raise
        except Exception as e:
            raise TelefonoInvalidoError(f"Ocurrió un error al validar el teléfono: {e}") from e

    @property
    def activo(self):
        """Retorna si el cliente está activo en el sistema."""
        return self.__activo

    # Métodos obligatorios heredados de EntidadSistema

    def obtener_info(self) -> str:
        """Muestra toda la información del cliente de forma organizada."""
        estado = "Activo" if self.__activo else "Inactivo"
        return (
            f"{'='*45}\n"
            f"  INFORMACIÓN DEL CLIENTE\n"
            f"{'='*45}\n"
            f"  ID       : {self.__id_cliente}\n"
            f"  Nombre   : {self.__nombre}\n"
            f"  Email    : {self.__email}\n"
            f"  Teléfono : {self.__telefono}\n"
            f"  Estado   : {estado}\n"
            f"{'='*45}"
        )

    def validar(self) -> bool:
        """
        Verifica que el cliente tenga todos sus datos completos y esté activo.
        Retorna True si todo está bien, False si no.
        """
        return (
            bool(self.__nombre) and
            bool(self.__email) and
            bool(self.__telefono) and
            bool(self.__id_cliente) and
            self.__activo
        )

    # Métodos para gestionar el estado del cliente

    def desactivar(self):
        """Desactiva al cliente sin eliminarlo del sistema."""
        self.__activo = False
        print(f"  ⚠ Cliente '{self.__nombre}' desactivado.")

    def activar(self):
        """Vuelve a activar a un cliente que estaba desactivado."""
        self.__activo = True
        print(f"  ✔ Cliente '{self.__nombre}' activado nuevamente.")

    def __str__(self):
        """Forma corta de mostrar el cliente, útil para imprimir listas."""
        return f"Cliente({self.__id_cliente} - {self.__nombre} - {self.__email})"

    def __repr__(self):
        """Representación técnica del objeto, útil para depuración."""
        return (f"Cliente(id='{self.__id_cliente}', nombre='{self.__nombre}', "
                f"email='{self.__email}', telefono='{self.__telefono}')")


# Pruebas — esto solo corre cuando ejecutamos este archivo directamente

if __name__ == "__main__":

    print("\n" + "="*55)
    print("  PRUEBAS DE LA CLASE CLIENTE - SOFTWARE FJ")
    print("="*55)

    # Prueba 1: crear clientes con datos correctos
    print("\n[PRUEBA 1] Clientes con datos válidos:")
    try:
        c1 = Cliente("Juan Pérez", "juan.perez@email.com", "3001234567")
        print(f"  ✔ {c1}")
        print(c1.obtener_info())
    except Exception as e:
        print(f"  ✘ Error inesperado: {e}")

    try:
        c2 = Cliente("María López", "maria@softwarefj.com", "+573157654321", "CLI-010")
        print(f"  ✔ {c2}")
    except Exception as e:
        print(f"  ✘ Error inesperado: {e}")

    # Prueba 2: intentar crear un cliente sin nombre
    print("\n[PRUEBA 2] Nombre vacío:")
    try:
        c3 = Cliente("", "test@email.com", "3009876543")
    except NombreInvalidoError as e:
        print(f"  ✔ Error capturado: {e}")

    # Prueba 3: nombre con números
    print("\n[PRUEBA 3] Nombre con números:")
    try:
        c4 = Cliente("Carlos123", "carlos@email.com", "3009876543")
    except NombreInvalidoError as e:
        print(f"  ✔ Error capturado: {e}")

    # Prueba 4: email con formato incorrecto
    print("\n[PRUEBA 4] Email inválido:")
    try:
        c5 = Cliente("Ana Torres", "correo_invalido", "3001111111")
    except EmailInvalidoError as e:
        print(f"  ✔ Error capturado: {e}")

    # Prueba 5: teléfono demasiado corto
    print("\n[PRUEBA 5] Teléfono muy corto:")
    try:
        c6 = Cliente("Luis Gómez", "luis@email.com", "123")
    except TelefonoInvalidoError as e:
        print(f"  ✔ Error capturado: {e}")

    # Prueba 6: ID con formato incorrecto
    print("\n[PRUEBA 6] ID inválido:")
    try:
        c7 = Cliente("Rosa Martínez", "rosa@email.com", "3002222222", "CLIENTE-1")
    except IDClienteInvalidoError as e:
        print(f"  ✔ Error capturado: {e}")

    # Prueba 7: desactivar y reactivar un cliente
    print("\n[PRUEBA 7] Desactivar y reactivar cliente:")
    try:
        c1.desactivar()
        es_valido = c1.validar()
    except Exception as e:
        print(f"  ✘ Error: {e}")
    else:
        print(f"  ✔ ¿Cliente válido tras desactivar?: {es_valido}")
    finally:
        c1.activar()
        print(f"  ✔ ¿Cliente válido tras reactivar?: {c1.validar()}")

    print("\n" + "="*55)
    print("  FIN DE PRUEBAS")
    print("="*55 + "\n")
