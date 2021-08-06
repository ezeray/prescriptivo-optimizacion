# Clase 2

## Problemas Clásicos Sobre Grafos

### ¿Cómo se recorre un grafo de una manera ordenada?

En estos algoritmos no se optimiza nada, a pesar de que el segundo podría utilizarse para camino mínimo (ver debajo).

#### Primer Algoritmo: Depth First Search (DFS)

La idea de este algoritmo es que comenzamos en un nodo cualquiera, y de aquel visitamos un vecino. En vez de seguir visitando los vecinos del primer nodo, seguimos con los vecinos del nodo actual. Cuando llegamos a un punto donde el único vecino del nodo ya lo recorrimos, volvemos inmediatamente hacia atras a buscar los vecinos que quedaban por visitar.

Entonces, la idea es que se mete "en profundidad" todo lo que se pueda por cada camino. Si pensamos en un árbol, tenemos que el algoritmo va caminando por todas las hojas de la rama por la que empieza antes de pasar a la siguiente.

#### Segundo Algoritmo: Breadth First Search (BFS)

Comenzamos en un nodo cualquiera y visitamos un vecino. Antes de ver los vecinos del nodo visitado más recientemente, vemos si quedan vecinos del nodo original por visitar. Al terminar ahí, seguimos con los vecinos de los nuevos vértices.

El motivo por el cual se puede usar para optimizar el camino mínimo entre un vértice y todos los demas cuando las aritstas no tienen peso o tienen todas el mismo peso. Simplemente hay que asociar un número a cada vértice que es uno más que el número del vértice desde el que llegamos.

### ¿Cuál es la mínima distancia entre dos vértices? Shortest Path

Un problema que aparece muchas veces es saber cómo llegar de un vértice a otro en la menor distancia posible. Es nuestro primer problema de optimización combinatoria: de todos los caminos posibles que hay entre el vértice origen y el destino, queremos buscar el que minimiza la distancia recorrida.

Este problema se puede resolver de manera exacta en tiempo polinomial, es decir es un problema "fácil" o "bien resuelto." Fácil, en este contexto, nos indica que se conoce un algoritmo que resuelve el problema en tiempo polinomial. Existen diversos algoritmos que resuelven este problema, cada uno idóneamente utilizado para diversas situaciones de contexto:

- Dijkstra

- Bellman-Ford

- Floyd-Warshall

- Dantzig

- A*

### ¿Cuál es la manera menos costosa de conectar todos los vértices? Minimum Spanning Tree

Dado un grafo con pesos en las aritstas, ¿qué subconjunto de aristas conectan a todos los ejes con la mínima suma posbile? Este problema se conoce como Árbol Generador Mínimo debudo a que la solución siempre es un árbool generador (un árbol que toca todos los vértices).

Es un problema de optimización combinatoria. Lo que se busca es el árbol generador **mínimo**, y este problema pertenece a la clase P.. También ecisten diversos algoritmos para resolverlo:

- Prim

- Kruskal

- Borûvka

### ¿Cómo puedo enviar la mayor cantidad de un commodity de un vértice a otro sujeto a ciertas restricciones? Max-Flow Problem

En muchas aplicaciones se quiere representar el flujo de valores desde un vértice (usualmente llamado Source o s) hasta otro vértice (usualmente llamado Sink o t). Las aristas tienen una restricción de la capacidad máxima que puede fluir por ellas.

De todos los flujos que cumplen las restricciones, nos interesa el que maximiza las unidades transportadas. Este también es un problema de optimización combinatoria.

Max-flow es aplicable, lógicamente, a problemas de logística, pero también nos permite modelar el "envío" de objetos no físicos, por ejemplo la asignación de horas. Es algo ampliamente aplicable, solo hay que tener algo más de creatividad al mirar los problemas; pensar en el ejemplo de los puntajes en torneo que mencionó Federico.

Algoritmos:

- Ford-Fulkerson

- Edmonds-Karp

- ...

### ¿Cuál es la forma menos costosa de recorrer todos los ejes de un grafo? Circuito Euleriano

En el problema del circuito euleriano el objetivo es encontrar un circuito que pase exactamente **una** vez por cada eje. Si bien no es un problema de optimización en si, está intimamente relacionado al Problema del Cartero Chino.

También es un problema que pertenece a la clase de copmlejidad P.

### ¿Cuál es la forma menos costosa de recorrer todos los véretices de un grafo? Circuito Hamiltoniano

El problema del circuito hamiltoniano es el análogo al circuito euyleriano pero ahora el objectivo es pasar por
