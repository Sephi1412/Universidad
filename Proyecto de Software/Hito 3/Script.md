  # Apertura
Buenas tardes a todas y todos los presentes. Mi nombre es Cristian Bustos y les comentaré sobre el proyecto que nuestro equipo desarrolló junto a **LVA Indices** durante este semestre: Controles de Límites de Inversión

Primero, daremos un poquito de contexto para entender la necesidad y motivaciones detrás de desarrollar un proyecto como este.

# Contexto
---
Para ninguno de los presentes en este auditorio es ajeno el concepto del dinero, es uno de los pilares fundamentales de la sociedad actual, para bien o para mal.

Dada su relevancia, todos intentan preservarlo o aumentar su valor.

Una alternativa para lograr este fin son los **fondos mutuos**, donde cualquiera puede participar, independiente del capital que posea.

Fondos mutuos hay muchos. Cada uno invierte en cosas distintas de formas distintas. Por ello, cada uno de ellos tiene un reglamento interno, documento en el cual se declaran todas esas cosas.

Las administradoras de dichos fondos deben acreditar a entes como la `Comisión para el Mercado Financiero (CMF)`, quien en este contexto actua como fiscalizador.

Aquí es donde surge el punto de conflicto fundamental: Si las Administradoras de Fondos no respetan su reglamento, sufren sanciones.

Esto es un claro desafío para las AGF. Validar estos reglamentos no es su prioridad ni especialidad. Estos se dedican a hacer inversiones.

# Necesidad
---
Muchos aquí se preguntarán: "*De acuerdo, hay sanciones por cometer errores, entonces simplemente pongamos medidas para evitar que ocurran*". Lamentablemente no es tan simple. Para entenderlo mejor, veamos como se hacen las validaciones actualmente:

Pongámonos en el lugar de un  operador de una AGF que se encarga de ver el reglamento interno:
- La jornada inicia descargando los archivos que contienen la información de inversiones de días previos. Abrir y descargar estos archivos te puede tomar hasta una hora, más si te equivocaste de archivo.
- El resto del día consiste en pasar leyendo los archivos, buscando errores y en caso de haber, identificar la causa de estos.
- Después, enviamos un reporte al area de inversiones de la Administradora de Fondos. Con esa información, el area de inversión trata de regular los excesos o faltas.
- Cabe mencionar que es posible que durante el día ocurran cambios, lo cual supone descargar aún más archivos.

En otras palabras, tenemos un proceso que requiere de una respuesta ágil para corregir las inversiones que hace la AGF, y claramente no es posible en el escenario actual.


## Problema
Ahora bien, existen márgenes para cometer faltas. Asumiendo que estos no son frecuentes se podría considerar un servicio de esta magnitud como una comodidad más que una necesidad. Pero no solo hay problemas con los errores. Actualmente las administradoras de fondos hacen las validaciones mediante Excel. 

Con el volumen de datos que manejan, el mero hecho de abrir un archivo puede tomar hasta una hora, y que se diga de navegar dentro del él.

Estos factores vuelven de un software de validación prácticamente una necesidad para las AGF

## Cliente y Propuesta
Aquí es donde entra LVA Indices. Ellos son una consulta que otorga distintos tipos de servicios, principalmente de predicción y análisis de instrumentos financieros.

Ellos proponen la creación de una aplicación web que valide de forma automática los reglamentos de las AGF

## Motivación
Su principal motivación para formar parte de este mercado es precisamente el hecho de que no existe uno. Ellos darían los primeros pasos en la creación de un ecosistema completo que pueda cubrir todas las funciones relacionadas al control de inversión.


# Solución
## Propuesta Cliente

Esta aplicación propuesta por LVA debe ser capaz de:
- Validar reglamentos internos de fondos mutuos.
- Obtener la reportería sobre los límites de inversión. Por ejemplo, crear un PDF con la información esencial que pueda ser enviada fácilmente por correo.
- Monitorear el estado de límites de inversión. Es decir, tener una interfaz que le permita ver al usuario en cualquier momento el estado de dichos límites.

Además, el stack stack tecnológico debe estar conformado por:
- React como framework para desarrollar el Front End.
- Datomic como back, corriendo este en un servidor de Amazon Web 
- Django para desarrollar una API.

# Desarrollo
Lo primero que hicimos como equipo fue analizar la situación en la que nos encontrábamos. Con poco más de tres meses era necesario considerar la posibilidad de que no ser capaz de concretar absolutamente todo.

Es por ello que nos fijamos objetivos por iteración. Objetivos que le generen el mayor valor a nuestros clientes.

## Iteración 1
Los objetivos fijados para la primera iteración fueron:
- Recibir capacitación necesaria para entender el lenguaje técnico de los reglamentos internos. Esto pues nosotros debíamos ser capaces de entenderlos, para luego crear funciones de validación a partir de ellos
- Probar que el stack tecnológico fijado fuese capaz de crear una aplicación con las características solicitadas.

El resultado de estos objetivos fue una simple vista, en la que cargábamos una regla, su descripción y los resultados de dicha validación.

Mientras tanto, el equipo de LVA diseñó un mock up en donde se especificaban los requisitos estéticos y funcionales de la aplicación

## Iteración 2
A este punto, teniendo el mock up en mano, el siguiente paso era intentar recrearlo. Para esto, dividimos el grupo en dos, donde: 
- Unos se centraron en trabajar sobre el Front End para que este sea lo más parecido posible al mock up. 
- Mientras que el resto se dedicó a trabajar sobre las consultas para traer la información que necesitábamos visualizar.

El resultado es como el que se ve en pantalla. 

Llegados a este punto, teníamos casi todo lo solicitado por el cliente, aunque esto en un contexto controlado, donde solo estábamos trabajando con un solo fondo mutuo. Por ello, el siguiente objetivo era comprobar que el modelo de datos planteado realmente funciona como nosotros lo planeamos.

## Iteración 3

Esta iteración, siendo la final, fue más de cierre. No mucho fue hecho en términos prácticos además de verificar que el modelo propuesto funcionaba. Nos centramos en documentar el código del proyecto y terminar de implementar características menores.


# Aplicación
Ahora, para hacer el showcase de la aplicación, pongámonos en el lugar del mismo operador que mencioné antes. Intentemos hacer lo mismo pero con esta aplicación.

Accedemos a la plataforma y nos recibe un selector de fondos mutuos. Supongamos que ahora mi prioridad es revisar el fondo BICE UF.

Al cliquearlo, me recibe una nueva vista con alguna información general del fondo y abajo, cuadros que representan los items de su reglamento interno.

Al cliquear en uno, se abre una vista más detallada, en donde podemos ver el detalle de la regla. Por ejemplo, el nombre de esta es **Clasificación de Riesgo**. Esta dice que "*el fondo solo puede adquirir instrumentos que cuenten con un riesgo mayor o igual a B*". Con este histograma fácilmente podemos ver que solo se ha invertido en instrumentos con riesgo mayores o iguales B.

También tenemos otras reglas, como **Inversión por Emisor**. Esta regla dice que hay un limite máximo sobre cuanto se puede invertir. Se especifica aquí que el límite es del 10%. Ahora, si nos fijamos en la tabla de instrumentos podemos notar que hay uno en amarillo y que el valor en **% cartera** supera al 10%. 

En otras palabras, esta regla no es respetada. Razón por la cual la regla tiene un punto rojo en su preview.

Esto sería por el apartado de las características principales. También tenemos otras funciones, como la capacidad de generar un PDF de reporte o poder descargar la información asociada a cada regla.

En esta demostración no gastamos más de 3 minutos, claramente superando el rendimiento del sistema de validación actual.

# Aprendizaje
Ahora, para ir cerrando con la presentación: Aprendizajes

- Algo que se dio en un momento dado del proyecto fue las diferencias resultantes entre querer desarrollar una aplicación sólida en términos de diseño y producir resultados pronto. Es algo que en un contexto controlado de la universidad no se podría experimentar. Trabajar con LVA nos ha dejado claro que hay que buscar un balance entre ambas cosas.
- Esto fue algo fructífero gracias a tener una comunicación fluida y constante con nuestros clientes. Todos los días teníamos reuniones en donde recibíamos su feedback y su guía. Haciendo evidente la relevancia de la comunicación y lo importante que es tener la confianza para poder preguntar lo que haga falta.
- Finalmente, la validación de la aplicación con usuarios debe formar parte del cronograma del proyecto. Siempre lo consideramos como una posibilidad, pero al no tener contemplado en que momento hacerlo, se entorpeció un poco el desarrollo de la aplicación al hacerlo al final de este.

# Proyecto fue un Éxito
Para cerrar, toca responder esta pregunta que nuestra profesora nos hizo múltiples veces: "*¿El proyecto fue un éxito?*". 

Cada quien podrá tener una respuesta distinta, pero personalmente creo que si lo fue. En términos tangibles, logramos desarrollar una aplicación que cumple con lo solicitado, pero más allá de eso, todos los miembros del equipo nos llevamos experiencia que solo podríamos haber adquirido en un entorno laboral. 

Por mi lado, el uso de React, metodologías desarrollo ágil de software y la habilidad de poder proyectar mis ideas ante un equipo de desarrollo están siendo claves en mi trabajo de título.

Es por esto y más que creo poder afirmar con firmeza que el proyecto fue un éxito.

