import pandas as pd
from abstract_factory import ConcreteFactory_HSolicitud, ConcreteFactory_HIntervencion
from cliente import client_code_histograma, client_code_media, client_code_mediana, client_code_moda

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
