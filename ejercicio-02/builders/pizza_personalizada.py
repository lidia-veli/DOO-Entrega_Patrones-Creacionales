from builders.builder import BuilderPizza


class ConcreteBuilder_PizzaPersonalizada(BuilderPizza):
    """
    Builder de pizza personalizada
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._pizza = PizzaPersonalizada()

    @property
    def pizza(self) -> PizzaPersonalizada:
        pizza = self._pizza
        self.reset()
        return pizza

    def tipo_masa(self) -> None:
        masa = input("Elige el tipo de masa (fina, normal, gruesa): ")
        self._pizza.add(f"Masa: {masa}")

    def tipo_salsa_base(self) -> None:
        salsa = input("Elige el tipo de salsa base (tomate, barbacoa, pesto): ")
        self._pizza.add(f"Salsa base: {salsa}")

    def tipo_ingredientes(self) -> None:
        while True:
            ingrediente = input("Agrega ingredientes (escribe '0' para terminar): ")
            if ingrediente.lower() == '0':
                break
            self._pizza.add(f"Ingrediente: {ingrediente}")

    def tipo_coccion(self) -> None:
        coccion = input("Elige el tipo de cocción (horno, parrilla, leña): ")
        self._pizza.add(f"Cocción: {coccion}")

    def tipo_presentacion(self) -> None:
        presentacion = input("Elige el tipo de presentación (tradicional, cuadrada, personalizada): ")
        self._pizza.add(f"Presentación: {presentacion}")

    def tipo_maridaje(self) -> None:
        num_bebidas = int(input("¿Cuántas bebidas deseas agregar? (0 para omitir): "))
        if num_bebidas > 0:
            for _ in range(num_bebidas):
                bebida = input("Elige una bebida (refresco, cerveza, agua): ")
                self._pizza.add(f"Maridaje: {bebida}")
        else:
            self._pizza.add("Maridaje: 0")

    def tipo_extras(self) -> None:
        extra = input("Agrega un extra (o escribe '0' para omitir): ")
        if extra.lower() != '0':
            self._pizza.add(f"Extra: {extra}")



class PizzaPersonalizada():

    def __init__(self) -> None:
        self.parts = []

    def get_parts(self) -> list:
        return self.parts
    
    def add(self, part) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"pizza parts: {', '.join(self.parts)}", end="")
