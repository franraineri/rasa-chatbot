

1. Hacer un bot en rasa comun con rasa init
2. Escribir entities: 
    Modos: asistente, representante. Roles: scrummaster, etc etc, y todos los entities que se les ocurran de un proceso de desarrollo de software.
    Actividades: definir todas actividades que se les ocurran de un proceso de desarollo, por ejemplo crear task, modificar task. todas estas entidades se escriben en los ejemplos de intents

3. Definir los ejemplos de intents que permitan ejecutar las acciones para interactuar con el mundo sintetico, siguiendo las buenas practicas recomendadas por rasa (buscarlas en la docu). Todos las entidades tienen que estar participando aca, siendo importante no repetir intents para agregar las entidades.  ¡Escribirlas en rules, las stories quedan vacias!

4. Implementar las acciones que generaran las requests para interactuar con el mundo sintetico. Estas deben responder los parametros que se procesan en el dispatcher (ver cuales) que seran devueltos al commutator si es un mensaje/evento, y  se debe enviar al componente correspondiente, la ejecucion con los parametros obtenidos, deben estar todos, si no informar error, en caso de ser evento, luego de disparado retornar ok, y en caso de ser mensaje debe esperarse la respuesta.

Este ultimo punto hace ref que si viene un mensaje "quiero crear al agilebot franco con el rol scrumm y modo asistente" en la custom action hay que filtrar la data importante, el metodo, crear agilebot. los aprametros rol, modo y nombre/id y eso vuelve al commutator para que lo ejecute


Links a la documentacion de buenas practicas:
https://rasa.com/blog/10-best-practices-for-designing-nlu-training-data/

# Resumen de las buenas practicas
