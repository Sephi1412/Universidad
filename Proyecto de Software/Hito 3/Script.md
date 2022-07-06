# Apertura
Compañeras, compañeros, cuerpo docente. A continuación, yo, Cristian Bustos les comentaré sobre el proyecto que nuestro equipo desarrolló junto a **LVA Indices**: Controles de Límites de Inversión

Antes de iniciar, un poco de contexto.

# Contexto
---
Para sorpresa de nadie, el dinero es uno de los pilares fundamentales de la sociedad actual, para bien o para mal. Es por ello que la gente busca ahorrarlo. Muchos usan la estrategia del colchón, otros usan bancos esperando que su dinero no pierda valor.

Una alternativa poco conocida son los **fondos mutuos**, donde cualquiera puede participar, independiente del capital que posea.

Naturalmente, entregarle tu dinero a un desconocido no es algo tan simple, se necesitan garantías sobre como este será empleado. Es por ello que cada fondo mutuo como tiene un **Reglamento Interno** en donde se declara como y en qué este dinero será invertido. 

Las administradoras de dichos fondos deben acreditar a entes como la `Comisión para el Mercado Financiero (CMF)`, que están respetando dicho reglamento. Por otro lado, la CMF se encarga de validar que lo que informan las Administradoras de Fondos, sea real. En caso de no serlo, se emiten sanciones.

# Necesidad
---
Esto es un claro desafío para las AGF. Validar estos reglamentos no es su prioridad ni especialidad. Estos se dedican a hacer inversiones. No solo deben gastar recursos en algo que no les produce beneficios, sino que están expuestos a cometer errores.

Las sanciones recibidas pueden suponer perdida de confianza por parte de inversionistas. Siendo esta fundamental para toda clase de negocios, cometer faltas es inadmisible.

Aca es donde claramente se identifica la necesidad de un posible servicio que valide sus reglamentos internos.


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





# Historia de Usuario
- Horario de Ingreso: 9.00
- Descargar Data para revisarla
	- 40-50 minutos (Eso sin considerar errores)
- Transcurso jornada:
	- Cambio en la cartera por reproceso: Bajarla nuevamente 
- Recién a 10 AM puedes trabajar
	- Investigar excesos y encontrar la razón de estos
- A las 11 AM:
	- Enviar correos al area de inversión
- Con esa información, el area de inversión trata de regular los excesos
- Horario Fin: 12 AM

# Ruta usuario y motivaciones

- Alguien que está a cargo del control de inversiones de un fondo
- Es importante notificar ya que esto va a la CMF
- **Multas** 
- La AGF debe tener todo en orden. Multa y van a llamar la atención.