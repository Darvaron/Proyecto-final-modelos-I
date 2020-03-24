# Proyecto final de modelos I  
David Armando Rodríguez Varón - 20181020041	
Juan Sebastián Sánchez Tabares -20181020008  


Se implementaron los siguientes patrones:  
- Builder: El patron builder fue usado en la generacion de cada una de las salas (mapGeneration)como a su vez en
la generacion de la partida (matchGeneration) debido a que estan compuesto de varios objetos y su creación posee complejidad.  
- Abstract Factory: Este patron fue usado para la generación de las partes que componen un enemigo, se encuentra en la carpeta abstractFactory.  
- Decorator: Fue usado para los power-ups del personaje permitiendo asi distintos comportamiento dependiendo de los power-ups que haya adquirido, evitando la proliferación de clases.  
- Chain of responsability: Patron usado para el manejo de la música.  
- Composite: Fue usado para el manejo de las puertas que conectan las distintas salas.  
- Observer: Usado para desplegar información al agarrar un poder.  
- State: Manejo de las puertas, si todos los enemigos estan muertos cambia el estado del juego permitiendo asi el cambio de sala.  
- Command: Patron usado para el manejo de las fabricas del abstract factory, en la clase NormalMatch  


¿En que consiste el juego?  
El juego consiste en eliminar a todos los enemigos del mapa, el mapa esta compuesto por varias sala que estan unidas entre si por puertas, que solo se desbloquean si la sala actual no tiene enemigos, es decir que todos los enemigos
estan muertos. Cada sala a su vez posee agujeros, los cuales mataran al jugador al caerse en ellos a excepción de que este lleve el sobrero negro, que es uno de los items que pueden encontrar en las salas del juego. Existen varios tipos 
de enemigos, cada uno con sus distintos atributos, unos más rapido y otros no tanto, como algunos más fuertes y poderosos que otros. Existen dos items más, la manzana y la espada, siendo la manzana una mejora de velocidad y la espada 
una mejora  de alcance de daño, es decir que tan lejos el personaje puede pegar, los items son acumulables, en el mapa también existen obstaculos que impedirán el avance del jugador. El juego cuenta con opciones de música tanto como con
opciones de resolución, gracias a su aleatoriedad se consigue que cada mapa, cada partida sea única.
