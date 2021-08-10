# Clase 3: Simulación, pt. 2

## Ejemplos que veremos

### Ejemplo de Simulación - Una Cola en la Panaderia

Una panaderia con una sola caja donde se hace un embudo; queremos ayudar a mejorar. Eventos relevantes para simular

- Un cliente llega la caja

- La caja comeinza a atender al cliente

- La caja termina de atender al cliente

Para poder simular los 3 eventos mencionados, necesitamos caracterizar dos inpits:

1. Rate de llegada de un nuwvo cliente.

2. Tiempo de atención a un cliente en caja.

En general, para determinar los valores de la entrada, se modelan usando algún tipo de distribución de probabilidad, que tengan un fundamento en el evento real. En este ejemplo usaremos:

1. Rate de lelgada: Cada minuto un cliente llega con probabilidad 0.25

2. Tiempo de atención: Distribución uniforme entre 3 y 6 minutos

#### Métricas sobre los Resultados de la Simulación

Las métricas impmortantes varían según el tipo de simulación. Por ejemplo, en el ejemplo de la panadería nos interesan metricas como el tiempo de espera promedio de los clientes, el tiempo "muerto" en la caja, etc.

### Ejemplo: Rotonda de la Ruta 11

Las rotondas son muy efectivas para ciertos lugares, pero ¿siempre son la mejor opción? Una simulación en este caso puede directamente derivar en una optimización y una toma de decisión.

### Ejemplo: Servicio de Gruas

Una empresa de servicio de remolque necesita asignar a su personal para atender llamadas. Tiene datos históricos de cómo varían los pedidos según el día, la hora y otros factores. Más allá de una predicción, se puede luego simular sobre esa base y realizar optimizaciones simples.

### Ejemplo: Asignación de Shoppers

Las empresas de envíos de pedidos de supermercados muchas veces trabajan por "slots". Toman los pedidos hasta cierta hora, y todos esos pedidos son asignados a un siguiente slot horario donde serán atendidos. Los shoppers no son trabajadores que cambian de locación por lo quedebmos realizar una asignación raznoable al comenzar el día.

### Ejemplo: Power Bidding Optimization

En algunos países, las redes de energía son bidireccionales y se permite vender y comparar energía. Suelen funcionar mediante un sistema de subasta en el cual tenemos que planificar con anterioridad quee vamos a hacer. Muchas veces no sabemos qué va a pasar mañana con variables importantes como el tiempo o el precio.

Si supiéramos exacto que va a suceder con el tiempo y los precios, podemos resolver un problema de optimización complejo para tener la mejor forma de operar. Como no lo sabemos, podemos simular muchos escenarios razonables (tomando como base una buena predicción) y resolver el problema de optimización asociado.

## Simulación en Python: SimPy

AL simular con estos formalismos, hay varias cuestiones que son comunes a todas las simulaciones. Hay librerías, como SImPy, que modelan algunos de estos conceptos útiles como "procesos" y "ambientes".

## Simulación En Anylogic: software específico

Existe software específico para hacer simulación que ya tienen un montón de stiuaciones precargadas listas para usar. No solo realizan la simulación, sino que además proveen visualizaciones bi- y tridimensionales que ayudan a entender mejor el modelo y el resultado.
