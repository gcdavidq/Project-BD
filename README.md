[![AWS](https://img.shields.io/badge/AWS-%20-101010?style=for-the-badge&logo=amazon-aws&logoColor=white&labelColor=FF9900)](https://aws.amazon.com/)
[![Pygame](https://img.shields.io/badge/Pygame-%20-101010?style=for-the-badge&logo=python&logoColor=white&labelColor=3776AB)](https://www.pygame.org/)
[![OS](https://img.shields.io/badge/OS-%20-101010?style=for-the-badge&logo=linux&logoColor=white&labelColor=FCC624)](https://en.wikipedia.org/wiki/Operating_system)
[![SQL](https://img.shields.io/badge/SQL-%20-101010?style=for-the-badge&logo=postgresql&logoColor=white&labelColor=336791)](https://www.postgresql.org/)
[![VS Code](https://img.shields.io/badge/VS_Code-%20-101010?style=for-the-badge&logo=visual-studio-code&logoColor=white&labelColor=007ACC)](https://code.visualstudio.com/)
[![HTML](https://img.shields.io/badge/HTML-%20-101010?style=for-the-badge&logo=html5&logoColor=white&labelColor=E34F26)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Numpy](https://img.shields.io/badge/Numpy-%20-101010?style=for-the-badge&logo=numpy&logoColor=white&labelColor=013243)](https://numpy.org/)
[![Sys](https://img.shields.io/badge/Sys-%20-101010?style=for-the-badge&logo=linux&logoColor=white&labelColor=FCC624)](https://docs.python.org/3/library/sys.html)

<p align="center">
  <a href="https://github.com/DenverCoder1/readme-typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com?font=Time+New+Roman&color=F1C40F&size=25&center=true&vCenter=true&width=600&height=100&lines=UNIVERSIDAD+PERUANA+CAYETANO+HEREDIA">
  </a>
</p>

## BIENVENIDOS A NUESTRO REPOSITORIO GRUPAL
Aquí encontrarán los trabajos, entregables, proyectos del curso de Bases de Datos.

## Integrantes de equipo:
+ Aybar Escobar Edithson Ricardo
+ Llanos Angeles Leily Marlith 
+ Luque Mamani Magno Ricardo 
+ Mendoza Villar Antony Iván 
+ Quezada Marceliano Gian Carlos 
## Docente: 
+ Montalvo Garcia Peter Jhonatan 

<div align="center">
  <h1> JUEGO DEMOCRATICO EMPLEADO BASE DE DATOS  INFORME DEL AVANCE ACTUAL  </h1>
</div>

## INTRODUCCIÓN  
En el presente informe se detallarán los avances alcanzados, las dificultades encontradas 
y las posibles soluciones planteadas en el desarrollo del proyecto. Cada uno de estos aspectos será abordado de manera minuciosa, respaldado con la evidencia correspondiente. El propósito del proyecto es aplicar nuestros conocimientos en bases de datos, lo cual constituye el componente central del desarrollo del juego. Por lo tanto, la base de datos debe ser robusta, escalable y estar debidamente optimizada para soportar un número significativo de jugadores. 
Esto no implica que las demás áreas del proyecto sean menos importantes; para garantizar 
un sistema estable y funcional, es fundamental que todos los componentes se integren de manera eficiente. En cuanto al desarrollo del videojuego, buscamos crear una experiencia de usuario intuitiva, accesible y entretenida. Adicionalmente, estamos enfrentando desafíos en el despliegue del videojuego en una plataforma web, lo cual buscamos realizar sin comprometer la funcionalidad esencial del sistema. 

## DESCRIPCIÓN DEL PROYECTO: 
### 1. Videojuego: 

El juego se escogió pensando en la buena interacción y fluides con el usuario. Siendo así, optamos por el juego ‘Bloxorz’, el cual es un juego 3D, pero para hacerlo más práctico, lo implementamos solo en 2D.  Bloxorz es un juego de rompecabezas de lógica basado en la web, que desafía al jugador a mover un bloque rectangular a través de un tablero flotante compuesto de fichas, hasta llevarlo a un agujero final. Fue creado por Damian Clarke y se hizo popular como un juego en línea que combina estrategia, habilidad y paciencia.  

![image](https://github.com/user-attachments/assets/d5288528-2425-4fd3-a80c-f95d661a8bf5)

#### Objetivo: 
El objetivo principal de `Bloxorz` es manipular un bloque rectangular y llevarlo al agujero cuadrado que se encuentra al final de cada nivel. El bloque puede ser movido en varias direcciones (arriba, abajo, izquierda, derecha) y puede estar de pie o acostado sobre el tablero. Debes mover el bloque con cuidado para evitar que se caiga fuera de los límites del tablero. 

#### Mecánica: 
##### • Movimiento del Bloque: 
El bloque puede ser movido en dos posiciones: de pie o acostado. Cada movimiento cambia la orientación del bloque, y la forma en que el bloque se coloque determinará el siguiente paso posible. 
##### • Botones y Puentes: 
Algunos niveles contienen botones en el suelo que deben activarse para abrir puentes o activar nuevos caminos. Estos botones pueden requerir que el bloque esté en una posición específica (por ejemplo, algunos solo se activan cuando el bloque está de pie). 

## Base de Datos:
La creación y el despliegue de la base de datos se llevaron a cabo en la plataforma Railway 
(ver imagen adjunta). Inicialmente, configuramos una base de datos MySQL y obtuvimos las credenciales necesarias para el acceso. Posteriormente, utilizando HeidiSQL, creamos credenciales específicas para cada integrante del equipo, además de una credencial general para los usuarios que deseen jugar, de manera que solo dispongan de los permisos estrictamente necesarios, siguiendo así las mejores prácticas de seguridad.

![image](https://github.com/user-attachments/assets/0ab54171-ace1-40a3-9fd9-d05d2e9b9430)

En cuanto a la estructura de la base de datos, consideramos óptimo crear únicamente tres tablas, con el objetivo de reducir el tiempo de respuesta de las consultas y, de esta forma, mejorar la experiencia del usuario durante el juego. Utilizamos MySQL Workbench para diseñar el diagrama de la base de datos, y posteriormente, a través de un proceso de ingeniería inversa, logramos implementar las tablas de manera efectiva.

### - Tabla VOTOS: 
Esta tabla es responsable de registrar los votos emitidos por cada 
usuario. Está compuesta por las siguientes columnas:

✓ id_votos 

✓ tiempo_registro 

✓ voto 

✓ nivel 

✓ posicion_x 

✓ posicion_y 

### - Tabla VERIFICACION: 
Esta tabla tiene la función de validar la información necesaria para permitir que la tabla HISTORIAL procese los movimientos. 

### - Tabla HISTORIAL: 
Esta tabla es la encargada de calcular y enviar el siguiente movimiento al juego, basándose en el voto más repetido. Está compuesta por las siguientes columnas: 

✓ Contiene las siguientes tablas: 

  ✓ id_historial 
  
  ✓ decisión  
  
  ✓ nivel 
  
  ✓ posicion_x 
  
  ✓ posicion_y 

## Despliegue: 
Aunque el proyecto no requiere explícitamente un despliegue en la web, como equipo 
consideramos que su implementación aportaría un valor significativo. Existen diversas opciones para el despliegue del sistema, siendo una de las más destacadas el uso de Flask combinado con SocketIO, lo cual permitiría la creación de un entorno web y una comunicación eficiente entre cliente y servidor. 
Otra alternativa viable es la creación de una instancia en AWS EC2 para alojar la 
aplicación. Esta opción es particularmente conveniente en caso de un incremento en el número de usuarios, ya que AWS proporcionaría una infraestructura escalable y servicios que facilitarían la administración y el mantenimiento del sistema.


## AVANCES REALIZADOS  
### Adaptación del Juego Bloxorz 

Como se mencionó anteriormente, el juego original 'Bloxorz' está desarrollado en 3D; sin 
embargo, para los propósitos de este proyecto se optó por realizar una versión en 2D. Para llevar a cabo este cambio dimensional, utilizamos herramientas de Inteligencia Artificial que facilitaron la conversión inicial, y posteriormente adaptamos el juego a nuestras necesidades específicas. Entre las adaptaciones realizadas se incluyen: la ampliación del número de niveles, la implementación de una doble pantalla, la integración con SQL para la gestión de datos, y la mejora de la interfaz de usuario, entre otros aspectos. 
### Versión Actual del Juego: 
De acuerdo con los requisitos especificados en el enunciado del proyecto, se desarrollaron 
dos pantallas principales: 

#### • Primera Pantalla: Esta pantalla combina la visualización del juego con la opción 
de movimiento, lo que permite a los usuarios votar por el próximo movimiento a realizar. Esta característica fomenta la participación y la dinámica de votación en el juego. 
#### • Segunda Pantalla: La segunda pantalla está destinada únicamente a la 
visualización del juego. En esta pantalla, el usuario puede observar el progreso del juego, pero no tiene la capacidad de votar para determinar el próximo movimiento. Esto asegura una separación clara entre la interacción activa y la observación pasiva del juego. 

Entonces, para integrar ambas pantallas de manera amigable, creamos un menú, en el cual el usuario puede seleccionar si quiere: 
-  ver y jugar
-  solo ver
-  salir del juego

### Menú principal: 
![image](https://github.com/user-attachments/assets/4e2532ca-c67a-43cc-8b6f-46bc90b56c21)

### Pantalla Ver y Jugar:
![image](https://github.com/user-attachments/assets/662f3600-1266-4826-a755-2606742b7e40)

### Pantalla solo ver: 
![image](https://github.com/user-attachments/assets/b375c43c-63c7-4b7f-8e79-45f0d2a7036f)

## Implementación de la dinámica de votación: 
Actualmente, este es nuestro diagrama de la base de datos:
![image](https://github.com/user-attachments/assets/30b3b52e-d3a8-4459-9a72-84968b492eeb)
El diagrama muestra la relación entre tres tablas que consideramos importantes para realizar las diferentes consultas en el sistema. En primer lugar, tenemos la tabla votos, que registra la interacción del usuario con las opciones del juego. Esta tabla incluye las siguientes columnas:

- id_votos: Clave primaria que identifica de manera única cada voto.
- tiempo_registro: Almacena el tiempo en el que se realizó la inserción del voto. 
- voto: Representa la opción que seleccionó el usuario (por ejemplo, arriba, abajo, izquierda, derecha). 
- votos_id_historial: Clave foránea que referencia a la tabla historial. 
- nivel: Indica el nivel o la dificultad del juego en el momento en que se emitió el voto. 
- posicion_x y posicion_y: Almacenan las coordenadas del bloque en el juego.

En segundo lugar, tenemos la tabla historial, que almacena las decisiones finales del 
juego basadas en los votos recibidos. Las columnas en esta tabla incluyen: 
- id_historial: Clave primaria que identifica cada registro en el historial. 
- decision: Almacena la decisión tomada (opción votada mayoritariamente).
- nivel: Indica el nivel del juego en ese momento. 
- posicion_x y posicion_y: Guardan las coordenadas del bloque al momento de tomar la decisión final.

Por último, está la tabla verificaciones, que se encarga de registrar si un voto ha sido 
verificado o no. Sus columnas son: 
- id_verificaciones: Clave primaria que identifica cada verificación. 
- verificacion: Indica si un voto ha sido verificado (1) o no (0). 
- verificaciones_id_votos: Clave foránea que enlaza la verificación con el voto correspondiente en la tabla votos. 
Estas tres tablas están relacionadas de tal manera que se puede rastrear el historial de decisiones tomadas en el juego basadas en los votos de los usuarios, asegurando que solo los votos verificados se consideren en las decisiones finales.

## Ejemplos de cómo funciona la base de datos:
![image](https://github.com/user-attachments/assets/ac30dfe5-94b9-41b4-92e9-0b3e4d3321d3)

## Despliegue del juego. 
Como se mencionó anteriormente, existen diversas formas de realizar el despliegue del 
videojuego. En principio, nosotros optamos por subirlo a una instancia de EC2 y de ahí realizar su distribución. Esto principalmente porque es una buena alternativa debido a las múltiples herramientas que integra AWS (Balanceo de Carga, Elasticidad, etc), permitiendo así un buen entorno en caso el juego lo requiera. 
Para realizar este despliegue, empezamos con la creación de una instancia EC2

![image](https://github.com/user-attachments/assets/c687d5a7-aef5-4c22-9e4d-412008504bd1)

Con ayuda del PowerShell de Windows, nos conectamos a la instancia creada, dentro de esta creamos una máquina virtual, para así descargar los paquetes requeridos, entre los principales las librerías del juego y XRDP (Servidor de Protocolo de Escritorio Remoto).  
Tuvimos que subir el juego a la instancia desde nuestra computadora local:
![image](https://github.com/user-attachments/assets/6e801908-0f9f-4794-b8d0-e1403b7011c9)

Luego, dentro de la consola de administración de AWS, tuvimos que configurar el puerto correspondiente para que se realicé la conexión con el escritorio remoto: 
![image](https://github.com/user-attachments/assets/027fadf8-33c9-42f1-a3c7-1bfa93108d23)

Por último, accedemos al programa ‘conexión a control remoto’ desde nuestra computadora local.

![image](https://github.com/user-attachments/assets/cf54d74d-98a0-42c8-94d9-060dde97caeb)
Colocamos las credenciales de nuestra instancia (ip_publica y usuario), para finalmente poder ingresar a la máquina virtual.

![image](https://github.com/user-attachments/assets/5b1d4fe8-c5ee-4286-9d4d-809423181b89)

En este punto, buscamos el archivo del juego, lo ejecutamos y podremos jugar desde la máquina virtual.
![image](https://github.com/user-attachments/assets/0c9ebd24-b377-4f5f-a06e-0fa948039356)


## Dificultades Encontradas 
Hasta el momento de la elaboración del presente informe, las principales dificultades 
giran en torno a la integración de la base de datos con el juego y el despliegue de este.

En cuanto a la integración de la base de datos con el juego, una de las principales dificultades fue definir correctamente las relaciones entre las tablas. Fue crucial asegurarse de que las claves primarias y foráneas mantuvieran una relación adecuada, ya que en un principio se definieron dos tablas principales: "votos" e "historial". El registro de los votos de los usuarios en la tabla "votos" no presentó mayores problemas, gracias a que se implementó un procedimiento almacenado que permitía realizar la inserción directamente desde el juego. El siguiente proceso involucra la elección de los votos más frecuentes en un lapso de cinco segundos, a partir de la primera inserción no verificada hasta la última registrada dentro de dicho periodo. En este caso, cuando se insertaba un nuevo registro en la tabla "votos", un trigger se encargaba de verificar si dicho voto cumplía con la condición del tiempo permitido. El principal problema surgió al intentar actualizar la columna verificación (de 0 a 1) en la tabla "votos". Como esta tabla estaba vinculada a un trigger, no se permitían las actualizaciones automáticas, lo que generó dificultades para realizar operaciones de verificación. Otro de los desafíos fue el manejo del lapso de espera de cinco segundos, que debía respetarse para que, en base a los votos registrados en ese tiempo, se pudiera tomar una decisión sobre el movimiento del bloque en el juego. 
Durante el desarrollo del juego en Pygame, `Bloxorz en 2D`, se han presentado diversas dificultades técnicas que requirieron soluciones específicas para garantizar su funcionamiento óptimo. Una de las principales áreas de complejidad fue la generación del terreno de juego, donde identificar cada cuadro en su posición dentro de la matriz tomó tiempo considerable. Dado que el terreno está compuesto por una cuadrícula donde cada celda tiene una ubicación precisa, fue necesario implementar un sistema eficiente que asegurara que cada elemento estuviera en su lugar correcto. La dificultad residía en gestionar dinámicamente esta disposición, ya que errores en las coordenadas podrían afectar la jugabilidad. 



Otra dificultad importante se presentó con la lógica de movimiento del bloque. Aunque solo se permiten cuatro movimientos—arriba, abajo, izquierda y derecha—, el bloque cambia de estado dependiendo de su orientación, ya sea vertical, horizontal o parado. Cada estado implica diferentes reglas de desplazamiento, lo que complicó el desarrollo de la lógica correspondiente y la correcta visualización del bloque durante cada movimiento. Asimismo, fue necesario gestionar los límites del terreno para evitar que el bloque saliera de la matriz o se quedara en una posición inválida, aumentando la complejidad del sistema. 
La implementación de la lógica de las múltiples palancas dentro de los niveles presentó desafíos adicionales. Existen diversos tipos de palancas, cada una con funciones específicas como activar o desactivar partes del terreno, y su interacción con el bloque debía ser gestionada con precisión. Además, algunas palancas interactúan de manera diferente según el bloque que las activa, lo que exigió un diseño cuidadoso de las interacciones para asegurar que las acciones desencadenadas fueran coherentes y no provocaran errores. Este sistema requería una sincronización precisa entre la activación de las palancas y los cambios en el entorno, lo que añadió una capa de complejidad al desarrollo. 
Por otro lado, al momento de realizar el despliegue, consideramos que no tenemos una secuencia clara de este, he ahí la primera dificultad. Pues, si bien existen muchos métodos y herramientas para hacerlo, cada uno tiene sus ventajas y contras, por lo que no nos decidimos por uno en particular. En principio, lo que el proyecto pide es que el juego se pueda jugar en 5 computadores remotamente. Sin embargo, consideramos que el juego tiene potencial para que se despliegue y se juegue en la web. Líneas arriba se menciona que el juego se puede subir a una instancia EC2, lo cual es bastante beneficioso si queremos cumplir con dicho despliegue. Aquí es donde entra la dificultad por no saber que metodología emplear:

- Uso de Flask y socket IO 
- Uso de VNC y NOVNC 
- Uso de solamente XRDP 
La forma en la que se trató de emplear cada una de estas alternativas se detallará más adelante.

Posibles soluciones 
### - Para la integración de la base de datos con el juego   
En cuanto al problema de actualización de la tabla "historial", se identificaron dificultades relacionadas con el trigger vinculado a la tabla "votos". Este problema surgía porque MySQL no permitía realizar cambios en la misma tabla que activaba el trigger. Para solucionar esta limitación, se creó una nueva tabla denominada "verificaciones". Esta tabla actúa como intermediaria, permitiendo que, al momento de verificar si los registros evaluados tenían un valor igual a 0, se actualice su estado sin problemas. Una vez verificado el registro en la tabla "verificaciones", se permite la actualización sin interferencias y, posteriormente, la inserción de un nuevo registro en la tabla "historial" se realiza correctamente, respetando las restricciones de tiempo previamente mencionadas, que es un lapso de 5 segundos.


### - Para la mejora del juego 
Para resolver la dificultad en la generación del terreno, se implementó un sistema basado en matrices que mapea la disposición de cada celda en el tablero. El código asigna coordenadas específicas a cada cuadro dentro de la matriz, lo que permite una identificación precisa de la posición de cada celda. Esto asegura que los elementos del terreno se coloquen correctamente y se eviten errores en la disposición de las celdas. 
En cuanto al movimiento del bloque, la solución se desarrolló dividiendo su comportamiento en tres estados principales: vertical, horizontal y "punto". Dependiendo de su estado actual, las reglas de desplazamiento cambian. Además, se creó una función que valida la posición del bloque en cada movimiento, verificando si alguna parte del bloque está fuera de los límites del tablero o en una celda no válida. Esta validación asegura que el bloque no pueda moverse a una posición incorrecta y permite un manejo adecuado de los límites del terreno. 
Para la implementación de las palancas, se diseñó un sistema de interacción específico. Cada tipo de palanca activa o desactiva ciertas áreas del terreno, y algunas requieren que el bloque esté en un estado específico, como en posición "punto". Se implementaron condiciones adicionales en la lógica del juego para que las interacciones sean coherentes, y se añadió una sincronización precisa entre la activación de la palanca y los cambios en el entorno.

### - Para el despliegue del juego 
La primera opción que consideramos para el despliegue del juego es la de usar solamente XRDP, cuando recién implementamos esta opción, no sabíamos que solamente servía para conectarse remotamente desde una sola computadora a la vez, es decir, que si un usuario se conectaba a la máquina virtual (desplegada en AWS EC2), entraba al juego y jugaba todo iba excelente, pero si otro usuario se conectaba a la misma máquina virtual, el propio entorno quitaba la sesión al primer usuario para dárselo al segundo. Un punto para resaltar es que el avance se mantenía (Es decir, se guardaba el avance del juego que hizo el primer usuario para que el segundo lo continue).

Adjuntamos un video con evidencias de lo mencionado: https://drive.google.com/file/d/1uKaPJ5XWATHuOSpzlhJn3006on3HEm6D/vie w?usp=sharing 
















