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
