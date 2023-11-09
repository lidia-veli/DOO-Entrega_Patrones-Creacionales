import csv
from random import randint
from builders.pizza_personalizada import ConcreteBuilder_PizzaPersonalizada, PizzaPersonalizada
from builders.director import Director
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Pedido:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.numero_pedido = None
        self.pizzas = [] # lista de objetos PizzaPersonalizada

    def asignar_numero_pedido(self):
        '''asignar numero de pedido con el formato 3 letras y 3 numeros'''
        num_pedido = letras[randint(0,25)] + letras[randint(0,25)] + letras[randint(0,25)] + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
        self.numero_pedido = num_pedido

    def agregar_pizza(self, pizza: PizzaPersonalizada):
        self.pizzas.append(pizza)



def generar_pedido():
    '''Funcion que genera un pedido para un cliente, le asigna un numero de pedido, 
    le pregunta cuantas pizzas quiere y las manda hacer'''
    nombre_cliente = input("Introduce tu nombre: ")
    pedido = Pedido(nombre_cliente)
    pedido.asignar_numero_pedido()
    num_pedido = pedido.numero_pedido

    print("Hola, " + nombre_cliente + ".")
    print("Tu número de pedido es: " + num_pedido)

    
    director = Director()
    builder = ConcreteBuilder_PizzaPersonalizada() #tipo de pizza
    director.builder = builder #Le decimos al chef que tipo de pizza queremos
    
    num_pizzas = int(input("¿Cuántas pizzas quieres? "))
    for i in range(num_pizzas):
        print(f'PIZZA {i+1}')
        hacer_pizza(pedido, director, builder)
        print()
    
    print()
    print("Tu pedido es: ")
    pizzas_solicitadas = leer_pizzas_por_numero_de_pedido(num_pedido)
    for p in pizzas_solicitadas:
        print(p)

    

def hacer_pizza(pedido, director, builder):
    '''Funcion que crea una pizza personalizada, la agrega al pedido y la guarda en un diccionario de pedidos'''
    
    director.build_pizza()
    pizza_personalizada = builder.pizza  # es un objeto PizzaPersonalizada
    lista_ingredientes = pizza_personalizada.get_parts()
    pedido.agregar_pizza(lista_ingredientes) # agregamos la pizza al pedido (en forma de lista de ingredientes)
    #pizza_personalizada.list_parts()  # imprime la lista de ingredientes
    
    # GUARDAR DATOS PIZZA
    guardar_datos_csv(pedido)

    builder.reset() #reseteamos  builder para que no se acumulen los datos



def guardar_datos_csv(pedido):
    with open('ejercicio-02/data/pedidos.csv', mode='a', newline='') as file:
        fieldnames = ['Número de Pedido', 'Masa', 'Salsa Base', 'Ingredientes', 'Cocción', 'Presentación', 'Maridaje', 'Extra']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        for pizza in pedido.pizzas:
                writer.writerow({
                    'Número de Pedido': pedido.numero_pedido,
                    'Masa': pizza[0],
                    'Salsa Base': pizza[1],
                    'Ingredientes': pizza[2],
                    'Cocción': pizza[3],
                    'Presentación': pizza[4],
                    'Maridaje': pizza[5],
                    'Extra': pizza[6]
                })

def leer_pizzas_por_numero_de_pedido(numero_pedido, nombre_archivo='ejercicio-02/data/pedidos.csv'):
    try:
        pizzas_solicitadas = []

        with open(nombre_archivo, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Número de Pedido'] == numero_pedido:
                    pizza = {
                        'Masa': row['Masa'],
                        'Salsa Base': row['Salsa Base'],
                        'Ingredientes': row['Ingredientes'],
                        'Cocción': row['Cocción'],
                        'Presentación': row['Presentación'],
                        'Maridaje': row['Maridaje'],
                        'Extra': row['Extra']
                    }
                    pizzas_solicitadas.append(pizza)

        return pizzas_solicitadas

    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return []

