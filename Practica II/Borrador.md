# Resumen

La presente práctica fue realizada en Tech-K, consultora que da asesoría comercial. Actualmente desarrollan multiples proyectos de forma paralela y decidieron desarrollar proyectos que intenten dejar un beneficio a la sociedad. Por ello crearon Bag App, una aplicación que busca dar empleo y remunerar a gente que no tiene otra opción que trabajar desde su hogar.

El stack tecnológico empleado para desarrollar el proyecto consiste en React Native y Django REST. Siendo estos frameworks que no se ven en la universidad, el practicante tuvo que pasar por procesos de capacitación intensivos.

Con dichos conocimientos, tuvo que dedicarse a solventar la deuda técnica que el proyecto venía arrastrando desde hace meses, para luego trabajar sobre el sistema de pagos que emplea la aplicación.

Debido a esto, el estudiante desarrolló múltiples fortalezas en el área de desarrollo web y móvil, en particular con JavaScript y Python.  Gracias al desafío enfrentado, se comprendió de primera mano valores como la responsabilidad, compromiso y la relevancia de tener iniciativa en un trabajo colaborativo.

# Descripción general de la práctica

- Tech-K está desarrollando una aplicación llamada \textbf{Bag App}, la cual tiene como objetivo ofrecer servicios de lavado y planchado ropa a domicilio. El principio de acción es similar a otras aplicaciones de \textit{delivery}, donde el usuario contrata un servicio, alguien en un vehículo viene a retirar el producto, en este caso ropa, y se la lleva a otra persona que se encarga de lavarla y plancharla.
  
- Este proyecto ha sido desarrollado en una ventana de tiempo bastante acotada, lo cual ha derivado en poca o nula documentación de código, lo cual ha dificultado la implementación de nuevas características a la aplicación. Es por ello, que los objetivos principales de la práctica son \textit{Documentar el código para solventar la deuda técnica preexistente, de modo que también el practicante se familiarice con la infraestructura de la aplicación y luego añada una característica a la misma.}



# Problemas a abordar
1. Capacitación
   - Quizas no sea necesario señalarlo (?)
2. Deuda técnica
    - Dada a la falta de experiencia de la gente que desarrolló la aplicación desde sus inicios y la velocidad a la que se debían producir los resultados iniciales, todo está desordenado, en especial el front end. Al principio eso no era un problema, pero mientras más se desarrollaba la aplicación y más gente se unía al equipo, más evidente se hacía que la situación no era sostenible a largo plazo. 
    - Naturalmente esto no hizo más que empeorar el desarrollo de la aplicación. Era costoso en tiempo, pero no era posible desviarse del curso de acción para reordenar todo porque era necesario centrarse en levantar el proyecto lo antes posible. Por ello una de los principales problemas era reordenar todos los archivos y documentar la mayor cantidad de código posible sin alterar el funcionamiento de la aplicación en el proceso. Esto también tenía como propósito permitir familiarzarse con el proyecto al tener que leer el código fuente del mismo.





3. Establecer un método de pago seguro y fácil de usar
    - Al igual que cualquier otro servicio de delivery, es necesario permitir a sus usuarios pagar de forma cómoda, rápida y sencilla. Si bien es cierto que usar transferencias es una opción válida, suele ser lento de validar por parte de la empresa y también lento de usar por parte del cliente.



# Objetivos

- Los objetivos principales de la práctica son:
  - Ordenar el proyecto lo máximo posible de modo que esto sea más legible y fácil de entender
  - Implementar un sistema de pago fácil de usar

- Es por ello que los hitos en orden cronológico fueron
    1. Tomar cursos de capacitación en React Native para poder entender mejor el código del proyecto
    2. Analizar la infraestructura de la aplicación
    3. Ordenar el Front End de la aplicación
    4. Documentar código
    5. Implementar una API de algún portal de pagos para gestionar las transacciones de los clientes
- Se tuvo en tiempo la duración de la práctica para definir estos hitos. Es por ello, por ejemplo, que la documentación del Back End o la API fueron dejados de lado, ya que estos están más ordenados.


# Metodologías

## Desarrollo de la aplicación

Se emplearon repositorios de GitHub para poder gestionar el versionado del proyecto. Especificamente, cuatro para cada una de las partes fundamentales de este: bag-admin, bag-backend, bag-api y bag-client. Se empleó un sistema de workflow simple en donde los repositorios tenían una rama nueva por cada nueva característica a implementar. Las cuales al ser finalizadas eran fusionadas en una rama de desarrollo, en donde se hacían pruebas para luego pasar a la rama principal.  Lamentablemente, al finalizar la práctica el proyecto fue dado de baja por problemas logísticos con quienes se encargan de transportar los pedidos. Es por ello que se solicitó sacar fotos y grabar videos sobre como opera la aplicación en caso de que en el futuro se reactivo el proyecto.

## Reuniones Administrativas

Estas ocurrían una sola vez a la semana y su principal objetivo era que los distintos integrantes del proyecto reportaran sus avances en las tareas semanales. Los primeros en presentar era el equipo de desarrollo, donde cuentan los avances y contratiempos que han tenido a la hora de implementar las características solicitadas por recursos humanos y los inversionistas. Luego venía el equipo financiero, el cual contaba los beneficios percibidos por la aplicación. Finalmente recursos humanos hace llegar al resto del equipo el feedback recibido por parte de usuarios, como por ejemplo, que cosas fallan, que cosas se podrían mejorar o que características se esperan en la aplicación.

Una vez que todos presentan sus resultados, el resto del equipo analiza la situación actual en conjunto para definir el curso de acción para la proxima semana de trabajo.

## Programar en Parejas

Siempre se intentó coordinar entre los desarrolladores para poder programar en conjunto. Esto permitía sacar a la luz ideas más interesantes, notar errores más rápido y lo más importante, aprender más.



# Solución

## Capacitación

Tal como se mencionó previamente, el inicio de la práctica se centró exclusivamente en capacitación sobre React Native y Django REST Framework. Esto se llevó a cabo mediante distintos cursos online de la plataforma Code With Mosh. En ella se presentan una serie de videos en los que enseñan al espectador las herramientas fundamentales del lenguaje o framework en cuestión.

Allí se tomaron los siguientes cursos:
- Introduction to React Native
- React Native (Advanced)
- Mastering Django REST
  
## Infraestructura App
- Se parte analizando desde App.JS y luego se comienza a ver progresivamente todos los llamados de funciones. 

## Ordenar Front End
- Comenzamos a clasificar las funciones en Hooks, Utility, Screen, Navigation, Contexts y Components

