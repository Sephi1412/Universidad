# Introducción
Compañeras, compañeros, cuerpo docente. A continuación, yo, Cristian Bustos les contaré sobre el estado actual del proyecto que nuestro equipo está desarrollando para **LVA Indices**: Controles de Límites de Inversión

# Contexto
Antes de iniciar, un pequeño contexto.

Para sorpresa de nadie, el dinero es uno de los pilares fundamentales de la sociedad actual, para bien o para mal. Es por ello que la gente busca ahorrarlo. Muchos usan la estrategia del colchón, otros usan bancos esperando que su dinero no pierda valor.

Pero otra alternativa poco conocida son los **fondos mutuos**, donde cualquiera puede participar, independiente del capital que uno posea.

Naturalmente, entregarle tu dinero a un desconocido no es algo tan simple, se necesitan garantías sobre como este será empleado. Es por ello que cada fondo mutuo como tiene un **Reglamento Interno** en donde se declaran el tipo de inversiones y como será invertido el dinero de sus participes.

Dicho reglamento es fiscalizado por instituciones como la `Comisión para el Mercado Financiero (CMF)`, para evitar que las Administradoras Generales de Fondos (AGF) resulten ser estafas.

Pero entonces ¿Dónde entra nuestro cliente en todo esto y cual es el problema a resolver?

# Cliente
## ¿Que hace?

**LVA Indices** es una consultora que otorga distintos tipos de servicios a las **AGF**, principalmente de análisis y predicciones sobre instrumentos financieros, mediante el uso de herramientas digitales. Estos servicios buscan ofrecer a sus clientes maximizar sus beneficios. 

## ¿Que busca?

En busca de crecer más y ofrecer un servicio más completo, **LVA** propone la creación de una herramienta que permita ayudar a las **AGF** validar que sus movimientos respeten su reglamento interno.

## ¿Quien es el Usuario?
Tal y como di a entender recién, el usuario serían las Administradoras Generales de Fondos. Esto principalmente porque su personal no son expertos en este tipo de validaciones. Por lo que pueden demorarse o cometer errores en el proceso.

## ¿Por que es necesario?
Quizás alguno de ustedes se esté haciendo esta pregunta. Previamente, mencioné que existe un ente fiscalizador ¿Para que se necesitaría una herramienta que valide los reglamentos? 

La respuesta es simple: La **CMF** se limita a comprobar una pequeña parte de los reglamentos, ya que es imposible revisarlos todos.

Esto supone que la responsabilidad cae totalmente en las **AGF**. Y si ellos se equivocan, pueden recibir penalizaciones como multas por ello

Y bueno, es bastante probable que ocurran errores. Por ejemplo:
- Tiempo limitado
- Errores humanos por dicho tiempo limitado
- Usan excel y son demasiados datos, toma mucho tiempo cargarlos y luego analizarlos

Como dije, los errores pueden resultar en multas o incluso afectarnos a nosotros o a nuestras familias. Por ejemplo, un error de este tipo puede indirectamente afectar a la pensión de muchos chilenos. **Los errores simplemente no son admisibles**

# Solución
Fue un largo contexto, pero se logró. Ahora ¿que solución proponemos?
- *Crear una aplicación web que automáticamente verifique si los movimientos de hechos por las Administradoras de Fondos respetan el reglamento*

## ¿Razones?
Al ser una app web, es accesible para todos y todas independiente del equipo, y al ser automático, eliminamos el error humano de la ecuación

## Arquitectura
Tu dale mi rey, chamulla como un campeón


# Que hay implementado
## Capacidad de definir un reglamento interno
Se definió un modelo de datos Django que permite definir el reglamento interno de un fondo mutuo

## Consultas Reglamento
Capacidad de hacer consultas al reglamento y validar si los instrumentos de un fondo mutuo los respetan

## Mostrar Validaciones
Se puede mostrar en front end si se cumple o no el reglamento



# Punteo de presentación

- Inicio con saludo
- Primero, contexto
- Dinero como pilar fundamental de la sociedad
- Alternativas de ahorro: Fondos Mutuos
- CMF como entidad reguladora para fomentar la confianza al invertir en los fondos
- ¿Donde entra LVA en todo esto?