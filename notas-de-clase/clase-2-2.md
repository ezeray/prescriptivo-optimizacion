# Clase 2: Simulación

## Qué es una simulacion

Una simulación es la generación de una historia artificial de uns sistema, y la observación de esa historia, para sacar conclusiones respecto del comportamiento y las caracteristicas oepracionales del sistema real. Esta simulación puede ser a mano o en una computadora.

### Simulación simple

Podemos pensar en simular en un programa tirar una moneda una X cantidad de veces.

## Simulación y Análisis Prescriptivo/Optimización

¿Qué tiene que ver la simulación con la optimización de toma de decisiones? En muchos casos, vamos a optimizar una función objetivo que, dada una solución posible al problema, será calculable analíticamente. Sib embargo, en otros casos la simulación podría ser la respuesta, especialmente si podemos modelar fricciones y potenciales fallas en simulación pero que sea dificil modelarlo en la función objetivo.

Por otro lado, hay ciertos contextos donde sabremos si una solución es factible porque se chequean las restricciones de manera analítica. En otros casos, la simulación no s puede ayudar en el chequeo.

Adicionalmente, en ciertas aplicaciones el contexto que determina el input para el problema de optimización puede ser variable; en casos así, una simulación nos puede ayudar a bajar la incertidumbre contextual. Entonces, suponiendo que tanto al función objetivo como las restricciones se puedan resolver analíticamente, pero el input puede variar según algún otro factor, dandole variabilidad.

## Cuando simular

Hay ciertos casos donde las interacciones son dificles de abstraer en una función objetivo, ya que estamos frente a un sistema complejo. En estos casos, simular nos ayuda. Relacionado a esto, podemos pensar en casos donde las variables de entrada pueden variar y la simulación nos permite realizar un análisis de sensibilidad adecuado.

Cuando se quiere experimentar cambios abruptos que tendrían un alto riesgo en la realidad.

Para verificar soluciones analíticas

La prueba en la realidad puede ser muy costosa en tiempo y/o dinero.

Los planes y soluciones se pueden visualizar

## Cuando NO Simular

- Muchas veces el resultado de la simulación se puede conocer analíticamente.

- Si la simulación es más dificil o costosa que la prueba directa.

- Si la simulación es más costosa que los posibles ahorros

- Si la simulación tarda más de lo que se puede permitir

- Si la situación real es extremadamente compleja aún para una simulación

## Tipos de Simulación

Vamos a tocar la superficie, pero hay un **muchísima** bibliografía y métodos al respecto. De hecho, hasta hay sub-áreas para atacar problemas de simulación.

Algunas de las más conocidas:

- Discrete Event Simulation: Simula secuencia de eventos y las entidades que interactúan.

- System Dynamics: Se usa para modelar flujos complejos dentro de un sistema.

- Agent Based Simulation: Se usa más para cuando las entidades involucradas son agentes y no procesos sampleables de distribuciones.
