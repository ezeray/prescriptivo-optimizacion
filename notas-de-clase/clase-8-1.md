# Clase 8: Programación Lineal Entera 2

## Algoritmo Branch & Bound (continuación)

### Recordando Pasos Generales del Algoritmo

1. Comenzamos nuestro árbol de exploración abriendo un único nodo con el problema original
2. Elegimos un subproblema a resolver
3. Resolvemos la relajación lineal asociada
4. CHequeamos si se cumple alguna de laas 3 podas mencionadas para no abrir más subproblemas.
5. Si no se puede podear, entonces realizamos un branching por alguna de las variables fraccionarias de la solución de la relajación lineal.
6. Si quedan nodos abiertos, volvemos al paso 2.

### B&B: Decisiones

En el esquema general dado arriba, hay algunos pasos que no están lo suficientemente especificados y, según cómo se implementen, podría dar lugar a árboles (binarios) de ejecución

#### Selección de Nodo

La primera elección es acerca de qué nodo será el próximo a tratas por el algoritmo. Esta es una decisión **muy** importante porque impacta en el camino del algoritmo, cuánta memoria y cuánto tiempo va a usar el algoritmo, y también en la calidad de las cotas obtenidas.

- DFS (Depth-First Search) (Profundidad FIFO):
  - Nodos que están nivel más bajo en el árbol.
  - Es una buena elección para cuando una sabe que puede haber temas con la memoria, ya que no aumenta rápido la cantidad de elementos en la lista de nodos abiertos.
  - "Permite" encontrar soluciones factibles rápidamente.
  - En lo que es **malo** es que se lleva mucho tiempo en explorar profundo una parte del árbol, por lo que puede que pase mucho tiempo antes de encontrar
- BFS (Breadth-First Search) (LIFO):
  - Nodos en orden en que fueron creados.
  - Es muy bueno para encontrar....?
  - Al ir abriendo más nodos, va a ir usando bastante memoria, ya que los nodos se duplican por nivel.
  - No es bueno cuando podemos no tener una solución factible.
- Best Bound (mejor cota):
  - Nunca se dividirá un nodo con cota inferior mayor que el óptimo, es decir vamos con el que mejor relacación lineal tenga.

#### Selección de Branching

Una vez que se resuelve la relaajcieon lineal, hay muchas maneras de tomar la importante decisión de por cuál variables vamos a ir ramificando para obtener los subproblemas.

Algunas estrategias:

- Variable más fraccionaria: Elijo la variable que más se "aleja" de ser entera, En la práctica, este criterio da algo mejor que hacer random pero no demasiado mejor, así que se suelen usar otros criterios.
- Pseudocostos: ...
- Strong Branching: Es bastante pesada. Significa branchear por *todas* las variables y fijarme por cuál de ellas conseguí la mejor separación.
- Branching sobre restricciones: (no lo entendí muy bien la verdad).

## Algoritmo Planos de Corte

Este algoritmo toma un camino de reducción del poliedro, pero directamente *descartando los puntos que sobran*, es decir aquellos que tienen partes fraccionarias.

Hay una región dentro del poliedro original que denominamos la *cápsula convexa de S*, y es el poliedro más chico que contiene a todos los puntos factibles sin dejar ninguno por fuera del poliedro original, es decir seguimos teniendo todos los puntos factibles. Este conjunto de puntos factibles son aquellos que son combinación convexa de los puntos de S.

$$conv(S) = \{x \epsilon \R^n \text{tal que } x = \sum \alpha_{i}x_{i}, \sum \alpha_{i} = 1, \alpha_{i} \ge 0\}$$

- Es e
- El cálculo así de arriba es bastante costoso computacionalmente porque podemos estar en situaciones donde trabajamos en dimensiones muy grandes, donde no es claro qué significa estar en el borde del poliedro.

El objetivo será ir encontrando planos de corte para ir acercándonos desde el poliedro original hacia la cápsula convexa.

### Pasos

Do **loop**

1. Resolver la relajación lineal de la formulación
2. Si la solución es entera o infactible, tenemos la solución. **break**
3. Si no, generamos una desigualdad válida que no se cumpla en la solución de la relajación lineal. Agregamos dicha desigualdad a la formulación. Volvemos al paso 1.

### Desigualdades Válidas

¿Cómo generamos desigualdades válidas para un problema?

- Aplicando ideas que dependan del problema subyacente.
- Utilizando familias de desigualdades vealidas que, potencialmente, aplican a cualquier problema:
  - Cortes de Chvatal-Gomory
  - Cortes de Gomory
  - Cortes de MIR (Mixed Integer Rounding)
  - Cortes *lift-and-project*
  - Y más...

En estos algoritmos, hay nuevos desarrollos de empezar a usar machine learning para predecir cuáles son las ramas a tomar, así ayudando a que las decisiones sean guiadas según el context en vez de ser determinísticas según la definición del algoritmo.

### Desigualdades de Bin Packing

Más allá de fórmulas generales, algunas desigualdades pueden surgir de analizar el problema en sí, las variables que tiene la formulación, y así enunciar alguna desigualdad válida.

Ejemplo: si un subconjunto de *n* items no entra en un mism ocontenedor, entonces la suma de sus variables de pertenencia no puede ser más grande que *n-1*.

### Desigualdades Cover

La desigualdad que enunciamos para Bin Packing enr ealidad es un poco más abarcativa; se puede aplicar siempre que tengamos una restricción de "tipo mochila", que vendreia a ser un problema donde hay que asignar sujeto a que la suma de los pesos sean menores o iguales a la capacidad total.

Supongamos que tenemos un conjunto de puntos S sujeto a una restricción tipo mochila y C cualquier conjunto de items que sobrepasa la capacidad de la mochila. EN un caso así, llamaremos *desigualdad cover sobre C* al hecho de no poder considerar a todos los items juntos en la mochila, es decir:

$$ \sum \limits_{i \epsilon C} x_{i} \le |C| - 1$$

### *Lifteando* Desigualdades

Una vez que se piensan desigualdades apra un problema, muchas veces se puede *liftear* esas desigualdades. Esto vendría a ser extender algunas desigualdades cover para incluir aquellas variables donde los pesos/coeficientes son más grandes o iguales que el coeficiente más grande del *cover*.

## Branch & Cut

Es un algoritmo que mezcla un poco de B&B y un poco de Planos de Corte.

Al resolver la relajación lineal de un nodo, en vez de directamente pasar a realizar el branching, intenta realizar un corte a través de reducción del poliedro.

Cuanto más se descarte en los nodos superiores, menor región factible es la que llegará a los subproblemas más profundos. Es por eso que muchas veces se hace énfasis en encontrar muchos cortes pronto, idealmente en el nodo raíz.
