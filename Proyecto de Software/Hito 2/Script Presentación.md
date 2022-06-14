# Apertura
Compañeras, compañeros, cuerpo docente y Victor, que viene en representación de nuestros clientes. A continuación, yo, Cristian Bustos les contaré sobre el estado actual del proyecto que nuestro equipo está desarrollando para **LVA Indices**: Controles de Límites de Inversión

Han pasado cerca de 2 meses desde que estuve frente a ustedes, así que les daré un breve repaso sobre los conceptos vistos en la presentación anterior.

## Contexto

Antes definimos los fondos mutuos como una potencial alternativa para gente que quiera ahorrar dinero sin que pierda su valor, como por ejemplo por la inflación.

Estos fondos mutuos tienen un reglamento interno que indica como y en que dicho fondo va a invertir el dinero de quienes participan en él. Las *administradoras de los fondos* deben verificar que estén cumpliendo su reglamento y luego la *Comisión para el Mercado Financiero* se encarga de fiscalizar dichas validaciones.

Todo esto tiene como propósito proporcionarle seguridad a quienes decidan invertir en fondos mutuos.


## Problema

Actualmente esas validaciones se hacen manualmente en planillas excel, y por multitud de factores vistos en la presentación anteriores, el error humano es una posibilidad, pero no es algo admisible. Ya que una falta de este tipo supone sanciones en formas de oficio o multas. Lo primero es particularmente peligroso para un fondo mutuo, ya que esto es sinónimo de ser poco confiable. Y siendo la confianza un factor clave en cualquier negocio, incluso puede significar el fin del fondo.

## Cliente

Aquí es donde entra nuestro cliente: LVA Indices, una consulta que ofrece distintos tipos de servicios a las *Administradoras Generales de Fondos*. Ellos, viendo un potencial mercado en esto, proponen una solución.

## Solución

Dicha solución, tal y como mencioné durante la presentación anterior, consiste en el desarrollo de una aplicación web que se encargue de validar de forma automática el reglamento de un fondo mutuo.


# Demo

## Trabajo Previo

Durante la iteración 1, nosotros desarrollamos un prototipo bastante primitivo, pero cumplía con los objetivos básicos: Seleccionar una regla de un fondo mutuo y verificar si este la cumple o no.

Pero si lo comparamos con el mock up creado por LVA, deja mucho que desear. Aquí podemos ver una vista general donde podemos al mismo tiempo el estado de todas las reglas usando una interfaz bastante amigable para el usuario final, pero ya no más.


## Iteración 2

Ahora, veamos el estado actual del proyecto: Accediendo al dominio que nos fue otorgado por LVA podemos ver como opera la aplicación en un entorno controlado, que debo decir, se parece bastante al mock up que nos dieron como guía.

Lo primero que notamos es esta fila de cajas de texto que le indica al usuario que es lo que está viendo. En este caso: La validación del reglamento interno del fondo BICE del día 2 de marzo del 2022.

Debajo de estos nos topamos con el corazón de la aplicación: Distintos *containers* que contienen un "summary" del estado de cada regla. Aquí podemos apreciar que cada uno de los *containers* una barra con porcentajes, que a primera vista, quizás no se entienda que representan. Pero al cliquear una de las reglas, se abre este drawer lateral que contiene la información al detalle de la regla seleccionada:

-  En la zona superior vemos el nombre de la regla
- Por debajo, la descripción. Aquí le indicamos al usuario en que consiste esta regla, que es lo que se busca representar
- Luego, los porcentajes límite del reglamento y cual es el porcentaje que presenta en estos momentos la regla
- Finalmente, tenemos una tabla que contiene a todos los instrumentos que responden ante esta regla, y aquellos que no la cumplen, se muestran en color amarillo.

A estas alturas queda claro lo relevante que es mostrarle al usuario si cada regla se respeta o no. Esto lo podemos ver en distintas partes, por ejemplo:

- En clasificación de riesgos, el "porcentaje actual de inversión está amarillo, notificando que hay conflicto". Del mismo modo, en la barra de porcentajes, también se ve de color amarillo. Esto se hace evidente si comparamos *Clasificación de Riesgo* y *Moneda*.
- Lo otro está en la side bar que contiene las categorías. Si una de estas está marcada con un círculo rojo, significa que una de las reglas que está asociada a esa categoría presenta un conflicto. Y si seleccionamos dicha categoría, hará un filtro de las reglas. Esto permitirá al usuario que en caso de haber muchas reglas por revisar, pueda buscar solo lo que le interese.


Finalmente, tenemos dos características que aún están en desarrollo. La primera es *descargar un reporte en PDF*. Este busca condensar todo la información que ve el usuario en un PDF para luego poder enviarlo a quien haga falta. Mientras que la otra es la capacidad de descargar un archivo CSV de las tablas asociadas a cada regla


### Modelo

En cuanto al modelo seguido para diseñar la aplicación está representado en este diagrama de flujo:
1. Desde el front end se manda una request con la llave primaria de los fondos: **Su RUN**
2. La API carga los archivos asociados a ese RUN, siendo estos uno que contiene la información del fondo y otro que contiene la información de todas las reglas del fondo
	1. Luego entraremos en detalle de porque se hizo esto
3. Entonces, el front end por el momento, solo renderiza los datos del fondo, como su nombre, fecha actual, etc.
4. En este punto, se hace un loop que permite de manera paralela, instanciar estos "bloques de reglamento" donde cada uno de ellos se encarga de hacer una request con la información de cada regla del fondo

### Que hay implementado
En síntesis, con el estado actual del proyecto podemos:
1. Consultar y definir nuevas reglas de un fondo
2. Validar dichas reglas
3. Y un sistema de caché para las request.

# Problemas Enfrentados

A lo largo de esta iteración, nos enfrentamos a un problema importante: Si nosotros corríamos el proyecto de forma local, todo funciona fantástico, pero al pasarlo a producción el servidor explotaba -figurativamente hablando-. 

La conclusión a la que llegamos con LVA es que el servidor donde almacenaban datomic simplemente no podía responder a la carga que le exigían. Así por nuestro lado tuvimos que diseñar un sistema de caché y optimizar las consultas a la Datomic para que disminuir dicha carga.

Actualmente la API genera cada 1 hora los archivos de cada reglamento y esta responde con esa  información  en vez de preguntarle directamente a la base de datos por cada request

El otro problema fue que al no poder modificar Datomic, tuvimos que separar la lógica en distintos archivos o módulos, de modo que el proyecto fuese fácil de mantener. Por ejemplo, cada fondo mutuo tendrá un JSON que contiene los datos generales de este o las definiciones de cada regla, como su titulo o descripción




