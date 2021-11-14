# To Do

1. Hacer un bot en rasa comun con rasa init
2. Escribir entities: 
    Modos: asistente, representante. Roles: scrummaster, etc etc, y todos los entities que se les ocurran de un proceso de desarrollo de software.
         todas estas entidades se escriben en los ejemplos de intents

3. Definir los ejemplos de intents que permitan ejecutar las acciones para interactuar con el mundo sintetico, siguiendo las buenas practicas recomendadas por rasa (buscarlas en la docu). Todos las entidades tienen que estar participando aca, siendo importante no repetir intents para agregar las entidades.  ¡Escribirlas en rules, las stories quedan vacias!

¿que intenciones deberiamos desarrollar? una intencion por cada metodo en las clases que podemos comunicarnos.
Nosotros podemos comunicarnos con las clases ExchangeManager y Messenger, cuyos metodos son:

Messenger:
+ send_message(agilebot_id: string, activity_name: string, parameters: Dict)
+ create_agilebot(agilebot:_id: string, role: string, mode: string)
+ change_agilebot_role(agilebot_id: string, new_role:string)
+ change_agilebot_mode(agilebot_id: string, new_mode: string)

ExchangeManager:
+ add_exchange(exchange:Exchange):string
+ remove_exchange(exchange_name:string):string
+ remove_all_suscribers(exchange_name: string) 
+ remove_agilebot_from_all(agilebot_id: string) 
+ remove_agilebot_from_some(agilebot_id: string, exchanges: List<string>) 
+ add_subscriber(exchange_name:str, agilebot: Agilebot, activity_name:string):string
+ publish(exchange_name: string, parameters: Dict):string

4. Implementar las acciones que generaran las requests para interactuar con el mundo sintetico. Estas deben responder los parametros que se procesan en el dispatcher (ver cuales) que seran devueltos al commutator si es un mensaje/evento, y  se debe enviar al componente correspondiente, la ejecucion con los parametros obtenidos, deben estar todos, si no informar error, en caso de ser evento, luego de disparado retornar ok, y en caso de ser mensaje debe esperarse la respuesta.

Este ultimo punto hace ref que si viene un mensaje "quiero crear al agilebot franco con el rol scrumm y modo asistente" en la custom action hay que filtrar la data importante, el metodo, crear agilebot. los aprametros rol, modo y nombre/id y eso vuelve al commutator para que lo ejecute


Links a la documentacion de buenas practicas:
https://rasa.com/blog/10-best-practices-for-designing-nlu-training-data/

# Resumen de las buenas practicas

1. Utilice datos reales.

concéntrese en construir su conjunto de datos a lo largo del tiempo, utilizando ejemplos de conversaciones reales . Esto significa que no tendrá tantos datos para empezar, pero los ejemplos que tiene no son hipotéticos, son cosas que han dicho usuarios reales, que es el mejor predictor de lo que dirán los usuarios futuros.

2. Mantenga distintos los ejemplos de entrenamiento en diferentes intenciones.

Esto suena simple, pero clasificar los mensajes de los usuarios en intenciones no siempre es tan claro. Lo que alguna vez pudo haber parecido dos objetivos de usuario diferentes, puede comenzar a recopilar ejemplos similares con el tiempo. Cuando esto sucede, tiene sentido volver a evaluar el diseño de su intención y fusionar intenciones similares en una categoría más general.

Una situación común en la que se pueden fusionar muchas intenciones en una es cuando los usuarios brindan información en respuesta a la pregunta de un asistente. Podría pensar que el mejor enfoque sería crear varias intenciones: proporcionar_nombre, proporcionar_dirección, proporcionar_email. Pero estos mensajes de usuario en realidad no son tan diferentes, difieren principalmente en sus entidades, y las palabras que rodean la oración son bastante similares. En este caso, la mejor manera de avanzar sería crear una única intención de informar y agrupar todos los ejemplos de capacitación en los que un usuario proporciona información debajo

3. Fusionar intenciones, dividir entidades.
¿cómo controlas lo que hace el asistente a continuación, si ambas respuestas residen en una única intención? Lo hace guardando la entidad extraída ( nueva o recurrente ) en un espacio categórico y escribiendo historias que le muestren al asistente qué hacer a continuación según el valor del espacio. Las ranuras guardan valores en la memoria de su asistente y las entidades se guardan automáticamente en las ranuras que tienen el mismo nombre. Entonces, si tuviéramos una entidad llamada status, con dos valores posibles ( nuevo o regresivo ), podríamos guardar esa entidad en una ranura que también se llama status.

6. Aproveche los extractores de entidades previamente capacitados.
Nombres, fechas, lugares, direcciones de correo electrónico ... estos son tipos de entidades que requerirían una tonelada de datos de entrenamiento antes de que su modelo pudiera comenzar a reconocerlos. Eso es porque hay muchos valores posibles.

En lugar de inundar sus datos de entrenamiento con una lista gigante de nombres, aproveche los extractores de entidades previamente entrenados. Estos modelos ya han sido entrenados en un gran corpus de datos, por lo que puede usarlos para extraer entidades sin entrenar el modelo usted mismo.

Hay dos extractores de entidades entrenados previamente disponibles en Rasa. El primero es SpacyEntityExtractor, que es ideal para nombres, fechas, lugares y nombres de organizaciones. DucklingEntityExtractor es otra opción. Se utiliza para extraer cantidades de dinero, fechas, direcciones de correo electrónico, horarios y distancias. Puede encontrar más información en los documentos .

7. Incluya siempre una intención fuera del alcance.
Una intención fuera del alcance es un comodín para cualquier cosa que el usuario pueda decir que esté fuera del dominio del asistente. Si su asistente ayuda a los usuarios a administrar su póliza de seguro, es muy probable que no pueda pedir una pizza. Cuando se detecta una intención fuera de alcance, el asistente puede responder con algo como "Suena interesante, pero esa no es una habilidad que haya aprendido todavía. Esto es lo que puedes preguntarme ...", que es mucho mejor experiencia del usuario que "lo siento, no entiendo".

8. Maneje las palabras mal escritas.
Es un hecho que los mensajes que los usuarios envían a su asistente contendrán errores de ortografía, así es la vida. Muchos desarrolladores intentan solucionar este problema utilizando un componente de corrector ortográfico personalizado en su canal de NLU. Pero diríamos que su primera línea de defensa contra los errores ortográficos deberían ser sus datos de entrenamiento.



instalar pyenv
