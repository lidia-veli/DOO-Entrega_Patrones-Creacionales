from abstract_factory import AbstractFactory


def client_code_media(factory: AbstractFactory) -> None:
    media = factory.calcular_media()
    print(f"Media: {media.calcular_media()}", end="")
    
def client_code_mediana(factory: AbstractFactory) -> None:
    mediana = factory.calcular_mediana()
    print(f"Mediana: {mediana.calcular_mediana()}", end="")

def client_code_moda(factory: AbstractFactory) -> None:
    moda = factory.calcular_moda()
    print(f"Moda: {moda.calcular_moda()}", end="")

def client_code_histograma(factory: AbstractFactory) -> None:
    histograma = factory.graficar_histograma()
    print(f"Histograma: {histograma.graficar_histograma()}", end="")
