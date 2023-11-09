# DOO-Entrega_Patrones-Creacionales
link repositorio: https://github.com/lidia-veli/DOO-Entrega_Patrones-Creacionales

## Ejercicio 1: Análisis Modular de las Activaciones del SAMUR-Protección Civil en Madrid con Abstract Factory
### Problema
El SAMUR-Protección Civil es el servicio de atención a urgencias y emergencias sanitarias extrahospitalarias en el municipio de Madrid. Su labor es esencial para garantizar la seguridad y el bienestar de los ciudadanos en situaciones de emergencia. A lo largo del año, el SAMUR lleva a cabo múltiples "activaciones" en respuesta a diversas situaciones, desde accidentes de tráfico hasta emergencias médicas.  
La ciudad de Madrid, en su compromiso con la transparencia y la apertura de datos, publica un registro detallado de estas activaciones en formato CSV. Este registro incluye información como la fecha, hora, tipo de emergencia, y otros detalles relevantes de cada activación.  
  
Tu tarea es desarrollar un programa en Python que haga uso del patrón de diseño "Abstract Factory" para modularizar y estandarizar el análisis de estos datos

### Solución
archivo: *ejercicio-01/main.py*



## Ejercicio 2: Sistema Integral de Creación y Gestión de Pizzas Gourmet con Almacenamiento en CSV utilizando el Patrón Builder
### Problema
La reconocida cadena de pizzerías gourmet "Delizioso" ha decidido lanzar una plataforma digital para permitir a sus clientes diseñar y personalizar sus pizzas al máximo detalle. Esta pizzería es conocida por su meticulosidad y su vasto menú de ingredientes, técnicas de cocción y presentaciones. Además de la personalización, "Delizioso" busca almacenar cada pizza diseñada por sus clientes en un archivo CSV para análisis posterior, recomendaciones personalizadas y marketing dirigido.  
  
Objetivos:
- Diseñar un sistema que permita a los clientes construir su pizza paso a paso utilizando el patrón Builder.
- Asegurar que cada elección sea validada para ser compatible con las selecciones previas del cliente.
- Incorporar un sistema de recomendaciones que sugiera ingredientes, técnicas y maridajes basados en las elecciones previas del cliente.
- Desarrollar un módulo que guarde cada pizza personalizada en un archivo CSV, almacenando cada detalle, desde los ingredientes hasta el maridaje recomendado.
- Crear una funcionalidad que lea del archivo CSV y pueda reconstruir la pizza para su visualización, edición o reorden.
- Garantizar la flexibilidad del sistema para futuras adiciones o modificaciones, ya que la pizzería está en constante innovación.
- Desarrollar una interfaz de usuario amigable que guíe al cliente en el proceso de creación, ofreciendo información relevante sobre cada elección y facilitando la toma de decisiones.
- Implementar medidas de seguridad para garantizar la integridad de los datos almacenados y la privacidad de las elecciones de los clientes.
- Al final del ejercicio, el estudiante deberá justificar el uso del patrón Builder y explicar cómo se logra la robustez y adaptabilidad del sistema, destacando las ventajas de su diseño frente a otros posibles enfoques.



### Justificación de uso del patrón Builder
El uso del patrón Builder es una elección sólida para resolver el problema de la gestión de la pizzería por varias razones:

- **Separación de la construcción de objetos y su representación**: El patrón Builder permite separar la lógica de construcción de objetos complejos, como las pizzas personalizadas, de su representación. Esto facilita la creación de diferentes variaciones de pizzas mientras mantiene la estructura del código limpio y fácil de entender.

- **Facilidad de personalización**: El patrón Builder permite a los clientes personalizar pizzas paso a paso. Cada constructor concreto puede tener su propia lógica de construcción, lo que facilita la incorporación de ingredientes y opciones específicas para cada tipo de pizza.

- **Validación y consistencia**: Al utilizar el patrón Builder, se pueden implementar validaciones en cada paso de la construcción de la pizza. Esto garantiza que las selecciones del cliente sean coherentes y válidas, lo que es esencial en una pizzería gourmet.

- **Flexibilidad y escalabilidad**: El patrón Builder es altamente escalable y permite agregar fácilmente nuevos tipos de pizza o características sin modificar el código existente. Esto es fundamental para una pizzería en constante innovación con un extenso menú.

- **Reutilización de código**: Cada constructor concreto puede reutilizar componentes comunes, lo que reduce la duplicación de código y mejora la mantenibilidad.

- **Gestión de pedidos y almacenamiento de datos**: El patrón Builder se integra de manera efectiva con la gestión de pedidos y el almacenamiento de datos, como se vio en la implementación que creamos. Esto permite una fácil asociación de pizzas a pedidos y su posterior almacenamiento en un archivo CSV.

- **Interfaz clara para el cliente**: El patrón Builder proporciona una interfaz clara para que el cliente construya pizzas paso a paso, lo que facilita la toma de decisiones y la personalización.
  
  
Otros patrones creacionales no serían tan adecuados para resolver el problema de la pizzería por las siguientes razones:
- **Abstract Factory**: El patrón Abstract Factory es útil para proporcionar una interfaz para crear familias de objetos relacionados o interdependientes. Esto podría ser adecuado para gestionar la creación de varios tipos de pizzas junto con sus ingredientes, pero podría ser demasiado complejo y mucho menos flexible para manejar las personalizaciones detalladas que un cliente puede hacer en una pizzería gourmet.

- **Factory Method**: El patrón Factory Method delega la creación de objetos a subclases, lo que es útil cuando una clase no puede anticipar la clase de objetos que debe crear. Sin embargo, en el contexto de una pizzería gourmet, donde se construyen objetos complejos con numerosas opciones, el Factory Method solo sería útil para crear instancias de tipos específicos, pero no para gestionar las múltiples opciones y personalizaciones de cada pizza.

- **Prototype**: El patrón Prototype se centra en la creación de objetos clonando instancias existentes. Esto puede no ser adecuado para un sistema en el que las pizzas se crean desde cero con selecciones de ingredientes específicos de cada cliente. No aborda la necesidad de validar y guiar al cliente a través de la personalización.

- **Singleton**: El patrón Singleton garantiza que una clase tenga solo una instancia y proporciona un punto global de acceso a esa instancia. Esto no es adecuado para un sistema en el que se deben crear múltiples instancias de objetos diferentes, como pizzas personalizadas, ya que limita la creación de instancias únicas.

### Solución
archivo: *ejercicio-02/main.py*
