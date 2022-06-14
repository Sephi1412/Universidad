# Presentación
Compañeras, compañeros, cuerpo docente. A continuación, yo, Cristian Bustos les contaré sobre el estado actual del proyecto que nuestro equipo está desarrollando para **LVA Indices**: Controles de Límites de Inversión

# Contexto (Repaso)

## ¿Quien es nuestro cliente?
**LVA Indices** es una consultora que otorga distintos tipos de servicios a las *Administradoras Generales de Fondos* principalmente de análisis y predicciones sobre instrumentos financieros mediante el uso de herramientas digitales. Estos servicios buscan ofrecer a sus clientes maximizar sus beneficios. 

## ¿Cual es el problema?
Tal y como mencionamos en la presentación anterior, los fondos mutuos tienen un **reglamento interno**, el cual actúa como una garantía para quienes decidan participar en dicho fondo. Este reglamento declara el tipo de inversiones y como será.

En el caso de que no respeten dicho arreglo, pueden recibir distintos tipos de sanciones, siendo la más significativa: *perder la confianza de los inversores*.

Es por ello que respetar este reglamento interno es de suma relevancia, pero validarlos puede ser una tarea tediosa y en la que fácilmente uno puede cometer errores. Esto pues tienen una ventana de tiempo acotada para revisar la data y actualmente eso se hace en Excel. Con pasar a llevar el teclado por accidente uno puede romper todo el sistema.

## ¿Cual es la solución?
Considerando la naturaleza de la tarea que se debe hacer, se propone *crear una aplicación web que automáticamente verifique si los movimientos de hechos por las Administradoras de Fondos respetan el reglamento*. 

# Iteración 1
## Imágenes Proyecto Anterior
En ese momento, solo éramos capaces de hacer consultas a la base de datos y recibir la información en la aplicación web para mostrarlas en tablas, pero nada más.

## Mock Up
Si lo comparamos frente al mock up, nada se parecía, pero tal y como nos comentó la profesora durante la presentación del hito anterior: "los pilares base de la aplicación estaban ahí".


# Estado Iteración II

Basándonos en los mock up y la arquitectura definida en la primera iteración, desarrollamos la presente aplicación:

## Demo
Como podrán ver, la aplicación ahora tiene una apariencia y funcionalidades mucho más próximas a las solicitadas por el cliente mediante el mock up. Para poder explicar mejor y en más detalle como opera la aplicación, pongámonos en el papel de un *operador de una administradora de fondos*: 

### Interfaz:

![[Pasted image 20220531181617.png]]

El portal nos recibe con una vista general, en donde podemos apreciar información como el fondo mutuo que estamos chequeando o la fecha sobre la cual estamos solicitando la información.

En la zona izquierda tenemos una "sidebar" que nos permite filtrar que elementos vemos en pantalla. Estos "rectángulos" representan a cada regla del fondo y contienen a su vez un resumen del estado actual de dichas reglas.

Si cliqueamos en uno de esos "rectángulos", aparecerá en pantalla un "Drawer" que contiene el detalle de cada regla. Aquí podemos ver específicamente que instrumentos financieros generan conflicto con la regla, siendo representados por el color amarillo.

Además, la sidebar que mencioné antes tiene algunos items marcados con un punto rojo. Esto nos notifica que en esa categoría existe algún reglamento que no se está respetando, ya que es posible que un fondo mutuo tenga muchas reglas y sea difícil de navegar por una vista que las contenga a todas al mismo tiempo

### Arquitectura y modelo del sistema
Durante la primera iteración, definimos el presente modelo como como arquitectura:
![[Pasted image 20220531184208.png]]
Aunque simple, nos sirvió como base para desarrollar el siguiente modelo:

*Insertar imagen de nuevo modelo, lo hago mañana. Pero debe ser un diagrama secuencial de como interactúa el cliente con el servidor*


- Por cada hora que transcurre, el sistema genera caché que contendrá la información de cada regla del fondo mutuo. 
- El cliente envía una request back end con el RUN identificador del fondo mutuo
- El back end le responde al cliente señalándole todas las reglas que tiene disponibles y las categorías de estas
- El cliente envía una request al servidor por cada regla en forma paralela
- Por cada regla, el back end le responde al cliente con la información almacenada en caché



# Objetivos para Iteración III
1. Optimizar consultas 
   (Vincular con el item de arquitectura, porque se implementó el sistema de caché)
2. Dejar en producción con múltiples fondos mutuos
3. Documentación

# Cierre y preguntas


# Notas
1. ¿LVA es una consultora o es otra cosa?