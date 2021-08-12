# Clase 4: Arrancando con Análisis Prescriptivo

## Problemas Clásicos en Investigación Operativa

Así como vimos problemas con resolucieon definida en teoría de grafos, existen problemas clásicos en investigación operativa. Si buen muchos no tienen solución exacta, ya que pertenecen a la clase NP, sí tienen un extenso tratamiento que es myt útil en la práctica.

- Problema de la mochila (knapsack)

  - Formas de

- Problema del viajante de comercio (Traveling Salesman Problem)

- Ruteo de vehículos con capavidades (VRP)

  - Similar al del viajante, pero teniendo algo así como una x cantidad de vehículos que además tienen una capacidad determinada.

- Bin Packing (BP)

  - Con una determinada cantidad de objetos físicos, cual es la mínima cantidad de contenedores para almacenarlos.

- Problema del coloreo de grafos (graph coloring)

  - Pintar con colores los vértices de un grafo

## Complejidad Algorítmica

Existen clases de copmlejidades en donde se puede categorizar a los diferentes problemas de decisión. Dos clases importantes son las clases *Polinomial* (*P*) y *No Polinomial* (*NP*). Esto es lo que lleva a que haya un tratamiento tan especial para estos problemas que hemos ido viendo.

La diferencia entre P y NP son muchos, pero resumiendo podemos usar definiciones que vimos antes. La clase *P* es *fácil* de resolver y chequear, mientras que **NP** es *difícil* de resolver pero *fácil* de chequear.

## Problemas fáciles y difíciles

Ya mencionamos muchos problemas en la materia que caen en las diferentes categorías.

Fáciles: DFS, BFS, Camino Mínimo, MST, Max Flow, Cricuito Euleriano

Difíciles: TSP, Problema de la Mochila, Super Mario

## Función Objetivo y Restricciones

En muchos problemas de optimización, vamos a hablar en términos de una función objetivo y las restricciones.

- Función Objetivo: Es lo que vamos a evaluar en el problema, lo que queremos optimizar (maximizar o minimizar). En el problema de la mochila, la f.o. es la suma de los beneficios de los ítems elegidos.

- Restricciones: son las condiciones que debe cumplir una potencial solución para ser considerada factible. En el problema de la mochila, hay $2^n$ formas de elegir ítems; solamente las que cumplan que la suma de sus pesos es menor o igual a la capacidad de la mochila serán consideradas factibles.

## Problema de la Mochila

Tenemos un conjunto de items que tienen dos valores asociados: un peso (o una medida de cuánto ocupa el item) y un beneficio (o una meida de cuánto nos interesa que ese ítem sea elegido). Además, tenemos una mochila con una capacidad limitada. ¿Cuál es la mejor manera de elegir los ítems que podemos llevar en la mochila de tal manera de poder mazimizar el beneficio?

### Complejidad

¿Es difícil Todo depende de una condición en particular: ¿se permite partir los ítems o no? Si permitimos partir, el problema se lo llama fraccionario y tiene una solucíon *greedy* muy simple: se ordenan los items según el ratio beneficio/peso y llenamos la mochila hasta lo que se pueda.

En cambio, si no permitismos partir ítems, entonces el problema se vuelve difícil. Por ahora, no se conoce un algoritmo polinomial que resuelva el problema. Por ejemplo, el algoritmo *greedy* ya no funciona de manera general; es fácil de ver con un ejemplo simple: una mochila de 20kg, un item de 11kg y $4 y dos items de 10kg y $2 de beneficio.

### Aplicaciones del Problema de la Mochila

- El problema de asignación de pedidos a shoppers que ya mencionamos.

- Optimización de carteras de inversión.

- Cualquier elección de subconjuntos sujeta a una capacidad de recursos.

- Restricciones Knapsack.

## Coloreo de Grafos (Vertex Coloring)

Dado un grafo, se quiere pintar los vértices de tal manera que dos adyacentes no tengan el mismo color. Lo que se busca es utilizar la mínima cantidad de colores. En grafos generales, es un problema *difícil*.

Es un problema que también sirve para modelar muchas situaciones reales. Existen también muchas variantes de este problema:

### Aplicaciones

## Problema del Viajante de Comercio (TSP)

Es seguramente **EL** problema emblemático de Investigación Operativa. Dado un grafo con pesos en las aristas, tenemos que encontrar la mejor manera de comenzar en un vértice, visitar todos los demás exactamente una vez y volver al original.

También un problema *dificil* pero con un montón de tratamiento en la literatura. AL igual que los problemas que venimos presentando, es importante por la cantidad de aplicaciones que abstrae y también porque tiene varias variantes vasamente utilizadas y estudiadas.

Variantes:

- TSP con *time windows*, en donde ciertos vértices sólo se puede visitar en determinados *time windows*.

- TSP angular, donde se tiene en cuenta el angulo para doblar.

## Heurísticas

Los 3 problemas planteados son *dificiles*. Vamos a ver variasformas de atacar estos problemas según el contexto de aplicación y las aspiraciones. Una de las primeras maneras para abordar estos problemas es mediante heurísticas.

Una heurística es un algoritmo para abordar un problema que no garantiza optimalidad. Es, en palabras simples, una idea razonable para conseguir una solución aceptable a nuestro problema, seguramente con un costo computacional bajo.

### Heurísticas para Problema de la mochila

En base a lo que se definió hasta el momento, ¿cuál sería una heurística para el problema de la mochila? El algoritmo *greedy* que vimos antes se podría aplicar, adaptandolo para que nos otorgue una solución factible al problema entero.

### H para Coloreo de Grafos

Una primera aproximación simple:

1. Ordenamos los vértices de alguna manera.

2. Luego, a cada vértice asignarle el color actual, si no se puede, usar uno nuevo.

Un procedimiento muy simple que no da ningún tipo de garantía, pero que para algunos tipos de grafos puede dar soluciones muy razonables y con un cómputo muy simple.

Arreglando esta regla de recién, podemos hacer:

1. Ordenar los vértices de alguna manera.

2. A cada vértice asignarle el primer colos que se pueda entre los ya utilizados. Si no se puede, usar uno nuevo.

Ahora es más difícil encontrar casos muy patológicos, pero sigue habiendo, por lo cual seguimos sin garantías del funcionamiento de esta heurística.

### H para TSP

¿Qué idxeas simples, y no tan simples, se pueden usar para armar soluciones para el TSP?

- Vecino más cercano

- Vecino más lejano

- Tour Bitónico

- Árbol Generador Mínimo + Duplicación de aristas

  - La idea aquí es buscar la mejor manera de unir los vértices; pensar en el ejemplo del grafo completo que mencionó fede en clase.

- Otros....

En estas heurísticas más desarrolladas, ya empezamos a conseguir cierto certificados de garantía de cuán lejos están del óptimo.
