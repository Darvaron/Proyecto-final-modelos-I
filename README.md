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
- Factory Method: Patron usado para la creación de los powerups, se encuentra en la carpeta mapGeneration/parts/concretePowerups, fue usado para permitir en tiempo de ejecucción la instanciación de una u otro power.

No se usaron los siguientes patrones:  
- Prototype: No se usó ya que poseiamos enemigos mediante otro patrón y los queriamos lo más independientes posibles puesto que se verificaria su muerte al final de la sala además de que la generación de enemigos es aleatoría por ende no se podría clonar siempre al mismo enemigo.
- Singleton: No se usó puesto que todo fue facíl de instanciar mediante los accesos entre clases.
- Adapter: No se usó puesto que no tuvimos una interfaz de una clase distinta la cual adaptar.
- Bridge: No se usó ya que no queriamos desvincular la abstracción de la implementación.
- Facade: Nuestro programa no posee un conjunto de subinterfaces que deban ser unificadas en una sola de alto nivel.
- Flyweight: No necesitamos el hecho de crear un objeto intermedio para cada entidad que ibamos a usar, pues unas heredaban a las otras.
- Proxy: No lo usamos puesto que no necesitabamos un representante de acceso a otro objeto.
- Interpreter: No lo vimos necesario puesto que define una representación gramática y su interprete, cosa que no hay en este juego.
- Iterator: No se usó puesto que accedimos a los array de elementos o colecciones de objetos de otra forma.
- Mediator: No se hizo uso de una clase mediadora para la comunicación enre objetos.
- Memento: No se hizo uso de la restauración de un objeto a estados anteriores.
- Strategy: No fue necesario la agregación de estrategias para manejar un objeto, lo hicimos a través de otro patrón.
- Template Method: No se hizo uso de una plantilla por lo que se recurrio a la herencia normal.
- Visitor: No se implementaron funcionalidades adicionales a clases por esto no se usó.


¿En que consiste el juego?  
El juego consiste en eliminar a todos los enemigos del mapa, el mapa esta compuesto por varias sala que estan unidas entre si por puertas, que solo se desbloquean si la sala actual no tiene enemigos, es decir que todos los enemigos
estan muertos. Cada sala a su vez posee agujeros, los cuales mataran al jugador al caerse en ellos a excepción de que este lleve el sobrero negro, que es uno de los items que pueden encontrar en las salas del juego. Existen varios tipos 
de enemigos, cada uno con sus distintos atributos, unos más rapido y otros no tanto, como algunos más fuertes y poderosos que otros. Existen dos items más, la manzana y la espada, siendo la manzana una mejora de velocidad y la espada 
una mejora  de alcance de daño, es decir que tan lejos el personaje puede pegar, los items son acumulables, en el mapa también existen obstaculos que impedirán el avance del jugador. El juego cuenta con opciones de música tanto como con
opciones de resolución, gracias a su aleatoriedad se consigue que cada mapa, cada partida sea única.
