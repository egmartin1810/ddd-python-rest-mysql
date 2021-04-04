# Desafío Teórico
Proyecto que consiste en armar un servicio web que exponga un endpoint para leer un archivo, consultar una serie de APIs públicas y cargar una base de datos con los datos del archivo y las consultas a las APIs, construido con patrones de diseño, concurrencia y Domain Driven Design.

### Procesos, hilos y corrutinas

**1.** Un caso en el que usarías procesos para resolver un problema y por qué..

Un caso podría ser un sistema de negociación de acciones (Algorithmic Trading y Traders negociando acciones o bonos de deuda), debido a que es un sistema de misión crítica donde es importante la resiliencia y la seguridad, por usuario o conexión, debido a que los cálculos que se realizan son complejos y requiere bastante uso CPU (intensivo) y si en un modelo de hilos, una petición falla no afecte a todo el programa generando una indisponibilidad.  

**2.** Un caso en el que usarías threads para resolver un problema y por qué..

El caso sería en una aplicación web o servicios web, como un portal público, donde la transaccionalidad no sea tan elevada (10 peticiones/segundo - que esté muy por debajo del límite de hilos del servidor) y tenga que realizar tareas intensivas de instrucciones de E/S como Consultas a Base de Datos o archivos y así alcanzar, debido a que por no tener una alta transaccionalidad o throughput y con tareas intensivas de E/S, sería una aplicación costo/eficiente, no estando en riesgo alcanzar el límite de los hilos de servidor y alcanzando el rendimiento, la velocidad de ejecución esperada y consume menos recursos que utilizando multiprocesos.  

**3.** Un caso en el que usarías corrutinas para resolver un problema y por qué.:

Un caso sería para una aplicación web o un servicio restful, en el cual se tiene una transaccionalidad alta (cargas de trabajo muy elevadas), ya se está llegando al límite de hilos, se tienen los mismos recursos (CPU, Memoria, etc) y se tienen intrucciones intensas de E/S (la red puede estar bloqueada), se podría hacer una optimización de recursos y rendimiento con corrutinas, debido a que la corrutina es mucho más ligera que el hilo, en donde por ser basada en programación asincrónica suspenden su ejecución en momentos (bloqueos),  mientras esperan un determinado recurso y se reanudan  (partes de una aplicación cooperan para cambiar tareas explícitamente en momentos óptimos) 

**4:** Si tuvieras 1.000.000 de elementos y tuvieras que consultar para cada uno de ellos
información en una API HTTP. ¿Cómo lo harías? Explicar.

Lo haría a través de programación concurrente (hilos y co-rrutinas) y asincrónica; usando hilos y corrutinas. Primero buscar el número de hilos óptimo para así configurar el ThreadPool y dentro de cada tarea que ejecuta cada hilo dividir el número de elementos por bloques a procesar (que representaría el procesamiento de un grupo de elementos/hilo  - 1 '000.000/nro de hilos y así partiría el 1'millón de elementos) y la corrutina haría la consulta a la API HTTP (asycrónicamente) por grupo de elementos. 
