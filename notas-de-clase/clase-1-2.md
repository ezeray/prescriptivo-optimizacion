# Clase 1: Grafos y Aplicaciones

## Grafos Everywhere

Podemos cruzarnos con grafos en una gran diversidad de casos:

- Airflow y DBT con sus DAGs

- Random Forests

- Neural Networks

- Representación de Redes

## Orígenes

La representación en grafos nace cuando Euler busca dar una solución al problemas de los puentes de Konigsberg, que plantea si existe un camino cruzando todos los puentes, pasando por cada uno una única vez (la definición de *path*).

## Definiciones

### Básicas

Un grafo G = (V, E) es una estructura que consiste de dos conjuntos finitos V y E. V es el conjunto de vertices y E el conjunto de ejes queunen vertices.

Un v´rtice tque está conectado por una arista a otro vértice v se denomina vecino de v.

La vecindad de un vértice v (N(v)) se define como todos los vértices vecinos de v. Es decir, $\{ w | (v, w) \epsilon E\}$.

### Extendiendo

Sobre estas ideas básicas, existen un montón de definiciones que dan lugar a otros formalismos:

- Grafo básico sin múltiples aristas ni auticiclos: Grafo Simple

- Múltiples aristas entre un mismo par de vértices: Multigrafo

- Aristas que conectan un nodo consigo mismo: Autociclo

- Grafos sin ciclos: grafo acíclico

- Grafos donde las aristas tiene dirección: grafo dirigido

- Grafos donde las aristas tienen peso: grafos pesados

## Relación con la materia

Un grafo nos permite representar un problema dado como las entidades que interactuan y cómo interactuan, lo que nos va a falicitar la representación de problemas complejos y buscar soluciones a problemas que, al abstraer, tienen una estrctura similar.

## Representaciones de un grafo

Tenemos diversas manears de representas

- Matriz de adyacencia

- Lista de adyacencia

- Lista de incidencias

### Matriz de Adyacencia

Se utiliza una matriz en donde la entrad $ij$ representa la presencia (o el peso) del eje entre el vértice $i$ y el $j$.

Algunas propiedades:

- Espacio cuadrático en los vértices

- O(1) acceder a un eje

- O(1) agregar un eje

- O(V) listar los vecinos de un vértice

### Lista de Adyacencias

Por cada vértice se guarda una lista de las aristas que tienen al vértice como uno de los puntos. Espacialmente se necesita O(V+E).

Los costos temporales dependen de la implementación específica; si se usan listas:

- O(N(V)) acceder a un eje

- O(N(V)) agregar un eje

- O(N(V)) listar los vecines de un vértice

### Lista de incidencias

...

## Grafos Clásicos

- Grafo completo: donde todos los vertices están conectados entre si; tengo $\frac{N(N-1)}{2}$ aristas.

- Grafo bipartito: tenemos dos conjuntos distintos de entidades que se conectan entre si, por ejemplo entre usuarios y productos, o la asignación de operarios con algún recurso.

- Árboles: Es un grafo particular, que no tiene ciclos y en el cual de cualquier vértice puedo llegar a otro vértice. Sé que las aristas son N-1 por definición.

- Grafos Regulares: ...

- Gracos ciclo: el grafo es un ciclo y nada más.

- grafos caino: el grafo es un solo camino y nada más

- Grafos intervalo: un grafo particular en el que el grafo nace de tomar intervalos en una linea, y poner un eje cuando los intervalos se solapan. Si los vértices tienen un solapamiento, pongo eje; las aristas se ponen exactamente.

## Más definiciones

- Camino entre dos vértices: una sucesión de vértices para cada par consecutivo de vertices existe una arista en el grafo.

- Distancia entre vértices: Pensando en un grafo simple, la distancia entre dos vertices es la cantidad de vertices que hay en el camino más corto de los posibles.

- Excentricidad: de un vértice, es la máxima distancia a cualquier otro vértice.

- Diametro: de un grafo, es la máxima excentricidad de todos los vertices.

- Radio: de un grafo, es la mínima excentricidad.

- Vérice Central: ...

- Componentes Conexas: ...
