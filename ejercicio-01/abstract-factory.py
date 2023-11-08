from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def pasar_a_horas_minutos(h_seg):
    h_hora = h_seg // 3600
    h_min = (h_seg % 3600) // 60
    return f'{h_hora} horas y {h_min} minutos'



class AbstractFactory(ABC):

    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_media(self) -> AbstractMedia:
        pass

    @abstractmethod
    def calcular_mediana(self) -> AbstractMediana:
        pass
    
    @abstractmethod
    def graficar_histograma(self) -> AbstractHistograma:
        pass

    @abstractmethod
    def calcular_moda(self) -> AbstractModa:
        pass


class ConcreteFactory_HSolicitud(AbstractFactory):
    def calcular_media(self) -> AbstractMedia:
        return ConcreteMedia_HSol(self.datos)

    def calcular_mediana(self) -> AbstractMediana:
        return ConcreteMediana_HSol(self.datos)
    
    def calcular_moda(self) -> AbstractModa:
        return ConcreteModa_HSol(self.datos)

    def graficar_histograma(self) -> AbstractHistograma:
        return ConcreteHistograma_HSol(self.datos)
    



class ConcreteFactory_HIntervencion(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def calcular_media(self) -> AbstractMedia:
        return ConcreteMedia_HInterv(self.datos)

    def calcular_mediana(self) -> AbstractMediana:
        return ConcreteMediana_HInterv(self.datos)

    def calcular_moda(self) -> AbstractModa:
        return ConcreteModa_HInterv(self.datos)

    def graficar_histograma(self) -> AbstractHistograma:
        return ConcreteHistograma_HInterv(self.datos)
    




# PRODUCTOS Media -----------------------------------------
class AbstractMedia(ABC):
    """
    Interfaz base para calcular la media
    """

    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_media(self):
        pass


class ConcreteMedia_HSol(AbstractMedia):
    def calcular_media(self):
        '''Calcular la media de la columna H Solicitud (seg)'''
        return pasar_a_horas_minutos(self.datos['H Solicitud (seg)'].mean())

class ConcreteMedia_HInterv(AbstractMedia):
    def calcular_media(self):
        '''Calcular la media de la columna H Intervencion (seg)'''
        return pasar_a_horas_minutos(self.datos['H Intervencion (seg)'].mean())


# PRODUCTOS Mediana ----------------------------------------
class AbstractMediana(ABC):
    """
    Interfaz base para calcular la mediana
    """
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_mediana(self) -> None:
        pass


class ConcreteMediana_HSol(AbstractMediana):
    def calcular_mediana(self) -> str:
        '''Calcular la mediana de la columna H Solicitud (seg)'''
        return pasar_a_horas_minutos(self.datos['H Solicitud (seg)'].median())

class ConcreteMediana_HInterv(AbstractMediana):
    def calcular_mediana(self) -> str:
        '''Calcular la mediana de la columna H Intervencion (seg)'''
        return pasar_a_horas_minutos(self.datos['H Intervencion (seg)'].median())
        


# PRODUCTOS Moda -------------------------------------------------------------
class AbstractModa(ABC):
    '''Interfaz para calcular la moda'''
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def calcular_moda(self) -> str:
        pass

class ConcreteModa_HSol(AbstractModa):
    def calcular_moda(self) -> str:
        '''Calcular moda de columna H Solicitud (seg)'''
        return pasar_a_horas_minutos(self.datos['H Solicitud (seg)'].mode()[0])

class ConcreteModa_HInterv(AbstractModa):
    def calcular_moda(self) -> str:
        '''Calcular moda de columna H Intervencion (seg)'''
        return pasar_a_horas_minutos(self.datos['H Intervencion (seg)'].mode()[0])
        


# PRODUCTOS Histograma -------------------------------------------------------------
class AbstractHistograma(ABC):
    '''Interfaz base para graficar histogramas'''
    def __init__(self, datos):
        self.datos = datos

    @abstractmethod
    def graficar_histograma(self) -> str:
        pass


class ConcreteHistograma_HSol(AbstractHistograma):
    def graficar_histograma(self) -> str:
        '''Graficar histograma de la columna H Solicitud (seg)'''
        plt.hist(self.datos['H Solicitud (seg)'], bins=50)
        plt.show()

    
class ConcreteHistograma_HInterv(AbstractHistograma):
    def graficar_histograma(self) -> str:
        '''Graficar histograma de la columna H Intervencion (seg)'''
        plt.hist(self.datos['H Intervencion (seg)'], bins=50)
        plt.show()
  


# CLIENTE -----------------------------------------------------------------
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





if __name__ == "__main__":

    # ----------------------------------------------------------------------------------------------
    # TRATAMIENTO DATOS ----------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------

    URL = 'https://datos.madrid.es/egob/catalogo/300178-10-samur-activaciones.csv'
    data = pd.read_csv(URL, sep=';')

    # eliminar nulos
    data_1 = data.dropna()

    # eliminar duplicados
    data_1.duplicated().sum()
    data_2 = data_1.drop_duplicates()
    df = data_2.copy()
    # transformar var 'Meses' a numérico
    dict_meses = {'ENERO':1, 'FEBRERO':2, 'MARZO':3, 'ABRIL':4, 'MAYO':5, 'JUNIO':6, 'JULIO':7, 'AGOSTO':8, 'SEPTIEMBRE':9, 'OCTUBRE':10, 'NOVIEMBRE':11, 'DICIEMBRE':12}
    df['Mes'] = df['Mes'].map(dict_meses)

    # transformas var 'H Solicitud (seg)' y 'H Intervencion (seg)' a formato numérico (segundos) 
        # que luego transformaremos prar el output
    df['H Solicitud (seg)'] = pd.to_datetime(df['Hora Solicitud'], format='%H:%M:%S')
    df['H Solicitud (seg)'] = df['H Solicitud (seg)'].dt.hour * 3600 + df['H Solicitud (seg)'].dt.minute * 60 + df['H Solicitud (seg)'].dt.second

    df['H Intervencion (seg)'] = pd.to_datetime(df['Hora Intervención'], format='%H:%M:%S')
    df['H Intervencion (seg)'] = df['H Intervencion (seg)'].dt.hour * 3600 + df['H Intervencion (seg)'].dt.minute * 60 + df['H Intervencion (seg)'].dt.second

    # ----------------------------------------------------------------------------------------------

    factory_h_sol = ConcreteFactory_HSolicitud(df)
    factory_h_interv = ConcreteFactory_HIntervencion(df)

    print()
    print('----------------------------------------')
    print('ESTADÍSTICAS HORA SOLICITUD')
    print('----------------------------------------')
    client_code_media(factory_h_sol)
    print()
    client_code_mediana(factory_h_sol)
    print()
    client_code_moda(factory_h_sol)
    print()
    client_code_histograma(factory_h_sol)

    print()
    print()
    print('----------------------------------------')
    print('ESTADÍSTICAS HORA INTERVENCIÓN')
    print('----------------------------------------')
    client_code_media(factory_h_interv)
    print()
    client_code_mediana(factory_h_interv)
    print()
    client_code_moda(factory_h_interv)
    print()
    client_code_histograma(factory_h_interv)


