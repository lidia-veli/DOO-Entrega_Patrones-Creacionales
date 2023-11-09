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
        plt.title("Histograma de H Solicitud (seg)")
        plt.show()

    
class ConcreteHistograma_HInterv(AbstractHistograma):
    def graficar_histograma(self) -> str:
        '''Graficar histograma de la columna H Intervencion (seg)'''
        plt.hist(self.datos['H Intervencion (seg)'], bins=50)
        plt.title("Histograma de H Intervencion (seg)")
        plt.show()
