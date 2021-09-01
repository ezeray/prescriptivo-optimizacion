# Clase 10: PLE + Solvers

## Elección de Proyectos con Conflictos

Seguimos con el problema de decisión de inversión en proyectos. ¿Qué pasa si, por ejemplo, al avanzar con nuestra inversión descubrimos que hay varios proyectos que pertenecen a competidores, por lo que no podemos invertir en ellos a la vez? Hay un conflicto a solucionar que deberá entrar como restricción en nuestro problema a resolver con el objetivo de no tener que descartar todo lo ya hecho.

En esto se aprovecha que estamos modelando el qué y no el cómo; es decir, le decimos al sover qué problema resolver, en vez de tener que programar los pasos a seguir

### CPLEX Selección de Nodo

mip.strategy.nodeselect

### CPLEX Selección de Variable

mip.strategy.variableselect

## Callbacks

Todo lo que vimos hasta acá son parámetros o directivas **antes** de empezar a resolver el problema, que es cuando invocamos el método *solve*.

Sin embargo, hay veces donde podemos querer "meter mano" **durante** la ejecución agregando componentes propias, código propio para resolver problemas tipo *ad-hoc*. Esto se hace mediante *callbacks*. Así, podemos pedirle a cplex que nos devuelva el control de ejecución para correr algún código propio, por ejemplo meter cortes o validar si los cortes nos sirven, la búsqueda de heurística primales, loggeo de información intermedia, etc.
