# Clase 5: Metaheurísticas

## Clase 4: Presentación del tema

Nos movemos a dar cierto tipo de solución heurística más genérica. Esto porque las heurísticas nos pueden ayudar mucho para obtener buenas soluciones para nuestros problemas, pero en general son procedimientos pensados específicamente para cada problema y no suele haber demasiada posibilidad de genralización.

En las metaheurísticas también nos vamos a conformar con soluciones buenos pero sin garantía de optimalidad, pero vamos a definir esquemas algorítmicos generales que podamos aplicar a muchos problemas.

## Metaheurísticas de Búsqueda Local

En las metaheurísticas de búsqueda local vamos a trabajar en un nivel de abstracción más alto que con las heuristicas. En vez de pensar en el armado de soluciones, vamos a pensar como realizar una búsqueda en el espacio de solcuiones sin importar cuál es el problema subyacente.

En las MH de busqueda local es poder definir si o si una idea de vecindario de soluciones, es decir que dada una solucion, tenemos que poder decir quiénes son las soluciones vecinas. Dicho simple, una "solución vecina" es aquella que por algún motivo sea parecida a la que está bajo observación. El tamaño del vecindario definido implica un tradeoff entre calidad de la solución y tiempo de cómputo.

¿Cuáles son las componentes que necesito para hacer una MHBL? Pensando que MHBL no *es* una única MH, sino que que se refiere a un esquema de MH. Como componentes necesitamos:

- Solución Inicial

- Vecindad

- Función Objetivo

Estas tres componentes son dependientes del problema particular, estas *no* son agnósticas del problema que estoy resolviendo. Sin embargo, la forma de recorrer la vecindad *si* va a ser agnóstica del problema particular. Dentro de las MHBL, hill climbing es una de las más básicas.

### Solucion Inicial

Para comenzar a utilzizar una MHBL como Hill Climbing, en primer lugar necesitamos una solución inicial factible. Cualquier solución factible sirve a fines pr´åcticos, pero suele ser bueno arrancar con la mejor solución posible que se tenga, ya que esto nos ayudará a conseguir un mejor resultado aplicando MHBL. En los casos de coloreo y tsp, podremos comenzar de la solución que nos arroje cualquiera de las heurística que ya hemos mencionado.

### Función Objetivo

Necesitamos de alguna manera comparar los vecinos, para poder guiar la búsqueda viendo cuál es la solución que mejor performa.

¿Podemos usar la misma función objetivo que se usa en el problema a resolver? Depende del problema, en TSP si, pero en Coloreo *no*.

¿Por qué en coloreo no? Porque la función objetivo de coloreo es *muy discreta*. Si utilizamos dicha función seguramente nos cueste mucho prosperar en la vecindad. Podemos entonces proponer una nueva función objetivo. Obviamente la nueva función tiene que guardar alguna relación con la origina porque si no está en concordancia con la original vamos a estar optimizando cualquier cosa. Una función clásica utilizada es $$ - \sum \limits_{i=1}^{K} |C_i|^2 $$

Esta tiene la particularidad de que ..... (explicación buena de fede)

### Vecindad

Definir los vecinos de un punto en el espacio de búsqueda, define la vecindad que se utiliza en la MH, y esta definición tiene que lograr un *trade-off* entre vecindades interesantes pero explorables en un tiempo razonable.

También nos interesa llegar a usar vecindades que cumplan ciertas propiedades, por ejemplo la propiedad de ser una vecindad conectada. ¿Qué quiere decir esto? Define una vecindad que presenta la chance de lelgar desde cualquier solución original a la solución óptima -- esto **no** quiere decir que vayamos a llegar a la solución óptima, porque por ahí tenemos que realizar una gran cantidad de pasos, pero **sí** sería posible con tiempo indefinido.

Para algunos problemas existen vecindades que agrandan el espacio de búsqueda, navegando soluciones infactibles.

#### TSP

- Swap: intercambiar la posición de dos vértices.
- 2-opt: Se sacan 2 aristas del ciclo y se rearma de la única manera posible
- 3-opt: se sacan 3 aristas del ciclo y se rearma de todas las formas posibles.

#### Coloreo

- Kempe Chains: cadenas de intercambio de colores
- Cambiar el color de un solo vértice. En este caso también cambiamos la función objetivo para poder nagevar las infactibilidades sin problemas. Esto tendría como función objetivo: $$ - \sum \limits_{i=1}^{K} |C_i|^2 + \sum\limits_{i=1}^{K} 2|C_i||E_i| $$

### Metaheurísticas Varias

Por más que se definan buenas componentes, un enfoque de *hill climbing* podreia converger a soluciones subóptimas. Por ello, existe un inmenso abanico de MH para atacar el problea de estancarse en un mínimo local:

- GRASP
- Simmulated Annealing
- Algoritmos Genéticos
- Colonia de Hormigas
- Muchos más!

## Algoritmos Genéticos

La idea detrás de esta mh es utilizar los principios de la evolución biológica para crear un esquema algorítmico que logre encontrar buenas soluciones a un problema de optimización. La idea detrás de esto es que la **selección natural** va llevando a soluciones que mejor se adapten a su ambiente, aplicado a la búsqueda de soluciones a los problemas que vamos a ver.

...

### Algunos Conceptos

- Población: Es un conjunto de soluciones
- Generación: es la población correspondiente a una iteración del algoritmo
- Genoma: es la manera de codificar las soluciones en un conjunto de geners o propiedades
- Crossover: es la manera de combinar individuos de una poblacieon para generar nuevas solcuiones
- Mutación: es el hecho de cambiar algo en una solución para generar otra
- Fitness: es la función de evaluación para decidir si una solución es buena
- Selección: es el proceso por el cual serán elegidos los individuos de la nueva generación

### Creación

No hay una receta exacta para un algoritmo genético, se pueden mezclar los componentes definidos de diferentes maneras, por ejemplo, teniendo o no crossover en una generación, etc. Un pseudocódigo para un esquema del algoritmo genético es el siguiente:

1. Generar una población inicial
2. Mientras que no se cumpla el criterio de terminación:
    1. Calcular el fitness de cada individuo
    2. Seleccionar los individuos según su fitness
    3. Seleccionar
    4. AAA

### Individuos

La primer cosa con la que hay que enfrentarse es cómo definir el *genoma* a utilizar. Una solución se representa mediante muchos *genes.* Cada gen es una propiedad de la solución. El cromosoma/genoma completo debería poder identificar correctamente una solución real al problema.

Los cromosomas

### Población Inicial

Para comenzar las iteraciones de un algoritmo genético necesitamos crear la primera generación. Al igual que en BL, necesitamos comenzar de algunas heurísticas para generar soluciones antes de comenzar propiamente con el esquema metaheurístico, pero podemos pensar que dadas las caracteristicas de los AG, nos interesa tener una generación 0 en la que los individuos no sean todos iguales, ya que el algoritmo se nutre de tener variabilidad entre las poblaciones.

Por ello, es totalmente factible arrancar con una generación completamente aleatoria, o generando ruido sobre valores dentro de todo factibles. Esto le dará a la población suficiente versatilidad para no converger rápidamente a soluciones muy parecidas.

### Critero de Terminación

¿Cuándo termina un AG? Es una pregunta muy amplia, así que decimos que *depende*. Hay muchas maneras de terminar el ciclo de iteración y no siempre hay uno correcto. Algunos de los más utilizados son:

- Por convergencia: de alguna manera se mide la diferencia entre la población de una generación y la siguiente y se observa que ya no hay variablildad.
- Por iteraciones: más allá de los resultados del proceso, se suele poner un *pesimista* de cantidad de iteraciones máximas a realizar.
- Por calidad: Cuando se llega a cierto nivel de solución en comparación al óptimo o a algún valor objetivo.
- Combinación de criterios: los criterios mencionados, y otros, se utilizan en conjunto.

### Evaluación (Fitness)

Básicamente, es evaluar que tan buena es una solución/un individo.

Al igual que sucedía con BL, la función objetivo del problema original podría no ser la mejor opción por diversos motivos, como en coloreo. También podría suceder que la función objetivo sea difícil de conseguir o definir, como en un juego adversarial.

Un ejemplo es un juego adversarial es el ajedrez. ¿Cómo se puede definir, en una función objetivo, lo que significa ser bueno en ajedrez?

Otro ejemplo interesante es la simulación de los autos, para la que hay que realizar una simulación, ya que la función objetivo es dificil de definir.

### Crossover

Es la forma de combinar dos individuos para crear uno nuevo. Básicamente, tenemos que mezclar dos tiras de genes entre si para crear un nuevo individuo.

Una de las formas más simples podría ser definir un punto de corte y generar un individuo con la primera parte de un padre y la segunda parte del otro. Existen muchas otras versiones de cómo realizar un crossover.

### Mutación

La mutación es, básicamente, que la expresieon de un gen cambie en un individuo. La mutazión suele utilizarse con una probabilidad muy pequeña para cada gen.

### Método de Selección

Es el método que se utiliza para decidir cuáles individuos de una generación van a reproducirse y cuáles no. Hay muchas maneras de realizar la selección, y además consideraciones adicionales. Por ejemplo, podríamos plantear condiciones para que la población crezca o se achique, etc.

Maneras simples:

- Selección simple: sin utilizar en absoluto el fitness, se eligen individuos al azar.
- Selección ponderada: se utiliza el fitness de cad aindividuo para ordenar o ponderar la selección.
- Competencia: se realiza algún tipo de comparación entre pares de individuos para elegir cuáles serán los elegidos.

## Más metaheurísticas

Hay de todo:

- Simulated annealing
- Ant Colony optimizacion
- Cuckoo Search
- Harmony search
- Particule swarm optimizacion
- Shuffled frog leaping algorithm
