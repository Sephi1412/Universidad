# Estructura de Trabajo
## Pasos
1. Capacitación de Three.JS 
2. Definir formato de modificación del terreno
   - Herramientas para que el usuario pueda definir el terreno sobre el cual quiera trabajar
3. Implementación de texturas sobre el terreno
4. Creación de agua como componente fundamental
   - Propiedades como físicas de su movimiento, interacción con el terreno.
5. Mezclar terreno y agua en una escena
   - **ESTO DEBERÍA SER EL MINIMO LOGRADO DURANTE ESTE SEMESTRE**
6. Importar modelos 3D como arboles o plantas a la escena 
7. Permitir dar propiedades particulares a distintas áreas del terreno
   - Por ejemplo: Tierra normal, suelo blando, arena, etc.
8. Definir la interacción entre la vegetación, terreno y agua


# Ideas
## Heightmap para definir el terreno

Actualmente, una de las estrategias más utilizadas para el modelado de terrenos es el uso de [*heightmaps*](https://docs.unity3d.com/es/2019.4/Manual/StandardShaderMaterialParameterHeightMap.html). En términos simples, esto permite dar las instrucciones a un interprete como Unity o WebGl de como generar un modelo 3D a partir de una imagen en escala de grises.

Es por ello, que podría ser una buena opción que la aplicación tenga dos vistas:
1. Una en donde se vea el terreno en 3D, y se pueda ver la simulación
2. Otra en donde el usuario pueda "dibujar el terreno". Dicho dibujo, mediante un script sería transformado a una imagen en escala de grises que será procesada por Three.JS y luego renderizada en la vista anterior.
   
   Naturalmente, esta herramienta otorga velocidad, pero no precisión a la hora de definir un terreno. Es por ello que la primera vista permitiría tomar "aristas" del wireframe para hacer pequeñas correcciones

![[heightmap_dibujo.gif]]

Esta opción puede ser interesante, porque la lógica puede ser gestionada por un sistema de grillas, siendo cada una de ellas un `Object`. En ese caso, podemos rescatar la información de la altura mediante la imagen, pero también podemos definir otros atributos.


## Propiedades del terreno
Eventualmente, será necesario darle propiedades al terreno, ya sea en terminos de cuanta agua puede absorber, el material u otras cosas. Una opción es dividir el terreno en tiles, al menos en términos estructurales/lógica de la aplicación. Este video [*How to Subdivide a plane into even squares*](https://www.youtube.com/watch?v=oQbfy8QP8Lc) puede ser de utilidad


# Cosas Interesantes
1. Diamond-Square Algorithm: Permite definir de manera procedural un terreno. Quizás se puede rescatar parte de este algoritmo para ver como organizar la información a nivel estructural.
2. Tutorial de Mapping: https://www.youtube.com/watch?v=HsCYEA_UuZA&list=WL&index=3
3. Setup de Three.JS: https://www.youtube.com/watch?v=1Id6dzPjjjg&list=WL&index=4
4. Tutorial para novatos - Three.JS: https://youtu.be/xJAfLdUgdc4




# Correo Andrew
- Propuesta aprobada
- Deadline siguiente entrega
- Acordar fecha de reunión mensual
	- Doodle
- Establecer "motivo" de la reunión
- ¿Enviar correos puntuales?
	- **Preguntar en la reunión**
- ¿Mock-Up?



# Apunte Jéremy
- Borrador de la entrega final