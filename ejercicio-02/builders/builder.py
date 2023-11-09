from __future__ import annotations
from abc import ABC, abstractmethod


class BuilderPizza(ABC):
    """
    Interfaz para crear las diferentes partes de los objetos Pizza.
    """

    def __init__(self):
        self._pizza = None

    @property  # para que nos cree getters y setters
    @abstractmethod
    def pizza(self) -> None:
        pass

    @abstractmethod
    def tipo_masa(self) -> None:
        pass

    @abstractmethod
    def tipo_salsa_base(self) -> None:
        pass

    @abstractmethod
    def tipo_ingredientes(self) -> None:
        pass

    @abstractmethod
    def tipo_coccion(self) -> None:
        pass

    @abstractmethod
    def tipo_presentacion(self) -> None:
        pass

    @abstractmethod
    def tipo_maridaje(self) -> None:
        pass

    @abstractmethod
    def tipo_extras(self) -> None:
        pass
