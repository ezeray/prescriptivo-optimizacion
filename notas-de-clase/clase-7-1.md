# Clase 7: Programación lineal entera

## Definicion de PLE

$ \max c^T x $
$ s.t. $
$ $
$ x \epsilon \Z$

## Que se puede modelar

Hay cosas que **no** se puede modelar con PLE, pero sí es verdad que absolutamente todos los problemas de optimización que mencionamos hasta el momento en la materia se pueden modelar y resolver mediante este formalismo.

## Problema de la mochila

Variables: Para $i=1,...,n$
$x_i =
    \begin{cases}
        1\ \text{si colocamos al objeto }v_i\ \text{blah} \\
        0 \\
    \end{cases}
    $

## Bin Packing

El problema de bin packing se puede aplicar a problemas reales de forma directa, ya sea pensando en problemas de logística para el transporte de container, como también abstrayendo el container a pensar en la repartija de tareas entre operarios o el envío de datos a través de una conexión para optimizar el envío de datos.

### Formulación del problema

- Función Objetivo: Sumar sobre los $y_j$ y minimizar esa suma.

$$\min \sum \limits_{j=1}^{n} y_{j}$$

- Restricciones:
  - Que se guarden todos los objetos
    $$\min \sum \limits_{i=j}^{n} x_{ij} = 1$$
  - Que los objetos entren en los contenedores

  - El recipiente es usado
  - Cotas e integralidad de las variables:
    $y_{j},x_{ij} \epsilon\{0,1\}\ \ i=1,...,n\ \ j=1,...,n$

Hay muchas cosas para tomar en cuenta en la formulación de arriba, recordar todo lo que aclaró Fede en clase.

## Vertex Coloring

¿Cómo podemos modelar el problema de coloreo de vértices? Tenemos que asignar color a un vértice, minimizando la cantidad de colores usados.

## Modelados

Los modelos que vimos arriba son *una* forma de representarlos, *no* es la única forma de hacerlo, existen otras alternativas para mdoelar los problemas vistos arriba. En PL también sucede esto, pero no era demasiado importante, ya que se tienen algoritmos eficientes mientras que el modelado fuese correcto.

En PLE, dos modelos correctos pero distintos para el mismo problema pueden derivar en tiempos de cómputo muy diversos. ¿Cómo podemos modelar el problema de la mochila de una manera distinta a la presentada?

## PLE - Buscando una Resolución

El cambio que introducimos no es más que un agregado al problema de PL; muchas partes siguen siendo parecidas, como que las restricciones de desigualdades siguen formando un poliedro, con la salvedad de que ahora la región factible son solo los puntos enteros dentro del mismo. De todas formas, *muchas* otras cuestiones cambian, e.g., el óptimo ya no necesariamente está en un extremo del poliedro.

## Relajación Lineal

Sabemos resolver modelos de PL. Una primera idea podreia ser entonces olvidarse por un momento de las condiciones de integralidad y resolver el problema conociendo en el poliedro dado por las restricciones de desigualdades.

El hecho de olvidarnos de algunas restricciones en este caso las de integralidad, es lo que da lugar a una relajación del problema.

La relajación es un problema que podemos resolver de manera fácil. ¿Qué podemos hacer luego con esa solución?

### Redondeo

En algunos casos, el redondeo de los valores de la solución puede ser razonable y en algunos casos puede hasta llegar a ser óptima. Sin embargo, en algunos casos puede suceder que podemos redondear sin problema, pero que la solución sea "muy" subóptimo. En casos más extremos, el redondeo puede llevarnos a una solución que no sea factible!

En algunos casos, redondear puede ni siquiera significar algo claro: ¿qué pasa si todas mis variables son binarias porque son decisiones y la solución es 0.t para todas ellas? En casos así, parecería que *no* podemos resolver problemas de PLE en un mundo de PL para luego hcaerlo **entero**.

Recordar la imagen de redondeo no factible que mostró Fede en los slides.

### Acotando

Cota: una cota es simplemente un valor límite para los valores que puede tomar alguna variable o restricción.

Para diseñar algoritmos de resolución de modelos de PLE, vamos a utilizar el concepto de cotas.

Supongamos que hablamos de un problema de minimización. Una heurística cualquiera sobre el problema nos otorga una *cota superior o primal*. No sabemos el resultado del problema, pero podemos estar seguros que el valor final no es mayor al otorgado por la heurística, ya que ya tenemos una solución factible.

Una *cota inferior o dual* es un valor del cuál podremos tener seguridad que la solución óptima no puede estar por debajo, y lo esencial de esto es que a través del uso d heurísticas *no* contabamos con esto. Básicamente, esto nos ayuda a acotar las soluciones que vamos a analizar; e.g., de forma externa nos viene el conocimiento de que la solución del problema de coloreo no va a ser menos de 4 colores, sin darnos explicación de por qué, solo que le creemos.

En un problema de maximización, la *cota superior* pasa a ser la *cota dual*, mientras que la *cota inferior* pasa a ser la *cota primaal*.

Podremos encontes decir que un problema está resulto cuando nuestra mejor cota superior es igual a nuestra mejor cota inferior (y tenemos una solución que realice esa cota). Ya mencionamos maneras de conseguir cotas superiores (a través de heurísticas), pero ¿cómo hacemos para conseguir cotas inferiores? ¡Relajando!

Como ya se mencionó, una relajación surge de tomar el problema original y *olvidarse* de ciertas restricciones. De esta manera, todo punto factible del problema original es factible de la relajación, pero *no al revés*. Luego, la mejor solución de la relajación debe ser menor o igual a la mejor solución del problema original.

Algunas relajaciones conocidas:

- Relajación Lineal
- Relajación Combinatoria
- Relajación Surrogada
- Relajación Lagrangiana

## Algoritmo Branch & Bound

Como indica el nombre, se basa en dos tipos de operaciones:

- Branch: parir el problema en subproblemas más pequeños y que nos eviten algún inconveniente actual.
- Bound: Utilizar las cotas primales y duales que se vayan consiguiendo en el algoritmo para descartar subproblemas, hasta llegar a suna solución óptima.

EL branching nos va a ir abriendo subprroblemas al ser aplicado de manera sucesiva sobre el problema original. Si tuvieramos que mirar absolutamente todos los subproblemas, terminaría haciendo fuerza bruta. EL objetivo es deshacerse de varios subproblemas mediante *pdoas*.

Podas que se aplicar´ån:

- Poda por integralidad: caso de buena suerte, ya que vamos a tener una solución que nos de enteros, por lo que ya habríamos alcanzado la optimalidad.
- Poda por infactibilidad: puede pasar que al hacer branching nos quede un poliedro vacío; es un poco dificil de visualizarlo, pero si tenemos muchas restricciones nos quedaría algo vacío.
- Poda por cota:

### Pasos generales

1. Comenzamos nuestro árbol de exploración abriendo un único nodo con el problema original
2. Elegimos un subproblema a resolver
3. Resolvemos la relajación lineal asociada
4. CHequeamos si se cumple alguna de laas 3 podas mencionadas para no abrir más subproblemas.
5. Si no se puede podear, entonces realizamos un branching por alguna de las variables fraccionarias de la solución de la relajación lineal.
6. Si quedan nodos abiertos, volvemos al paso 2.
