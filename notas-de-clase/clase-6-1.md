# Programación Lineal

## Falta la primera mitad casi

## Componentes

## Representación Geométrica/Gráfica

**Polihedro Convexo**: fundamental para visualizar las soluciones factibles de un problema de programación lineal. Esto lo pensamos como la *región factible* del problema.

Hay dos cosas a tomar en cuenta:

1. No siempre las restricciones nos van a llevar a un polihedro que sea "tan lindo"

2. Siempre hablamos de desigualdad, no de mayor o menor estricto. ¿Por qué? Si tenemos un estricto, tenemos una solución no cerrada, etc etc.

## Solcuiones y Posibles Óptimos

Podemos tener:

- Un único óptimo

- Infinitos óptimos

- Infactible

- No acotado: cuando el polihedro no está cerrado y siempre puedo encontrar configuraciones que den mejor.

## Algoritmos

Existen algoritmos que pueden resolver el problema de PL (i.e. una instanciación del modelo), y lo bueno es que la solución (o una de) siempre estará en un extremo del poliedro y en base a esto se pueden diseñar diferentes algoritmos.

En 1947 Dantzi diseña el algoritmo Simplex, que va recorriendo los extremos del poliedro hasta encontrar la solución óptima. En el peor caso puede llegar a ser exponenical, aunque en la pr´åctica es muy utilizado y corre en muy buenos tiempos. En 1984, Karmarkar diseña un algoritmo con diferentes fundamentos que resulta polinomial, mostrango que el problema de PL es de complejidad P.

## Software y Librerias

## Más Allá de la Programación lineal

A veces PL no nos alcanza, ya que hay muchos casos donde quiero que mis variables sean **enteras**. Por ejemplo:

- ¿Qué pasa si tengo que product un bien que no se puede partir? Es posible que este caso no sea tan grave.
- ¿Qué pasa si el bien que no se puede partir es algo muy costoso y ya no es despreciable *lo que sobra*? Por ejepmlo, al tratar con containers y logística de envíos globales
- ¿Cómo hacemos si queremos representar en una variable una decisión binaria de hacer o no hacer una determinada tarea? Con PL **no** podemos representar una decisión binaria, por ejemplo si tomo o no un camino.

PL se queda corta en estos casos, y por el momento la clase P también.
