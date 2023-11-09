
from builders.builder import BuilderPizza
from builders.pizza_personalizada import PizzaPersonalizada

class Director:
    """ El director ejecuta los pasos de construcción en una secuencia particular."""

    def __init__(self) -> None:
        self._builder = None  # no es privado, es PROTEGIDO, se puede acceder desde las clases hijas

    @property
    def builder(self): # -> BuilderPizza:
        return self._builder

    @builder.setter
    def builder(self, builder: BuilderPizza) -> None:
        self._builder = builder


    def build_pizza(self) -> None:
        self.builder.tipo_masa()
        self.builder.tipo_salsa_base()
        self.builder.tipo_ingredientes()
        self.builder.tipo_coccion()
        self.builder.tipo_presentacion()
        self.builder.tipo_maridaje()
        self.builder.tipo_extras()
