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
























