# Parcial-3-Corte
### JUAN TINOCO - SANTIAGO SERRANO
A continuacion en este repositorio, podran encontrar 1 carpeta con el codigo de python y un readme explicando ese proyecto, y el documento "Juego pokemon" con un link de drive, el cual es la carpeta del proyecto del juego pokemon en c++.
## Indicaciones codigo c++
para poder correr el codigo se necesita realizar los siguientes pasos:
1. en el link de drive encontraran un archivo comprimido el cual deben descomprimir.
2. visual studio debe estar en debug y x64.
3. se necesita descargar la libreria SFML y descomprimir el archivo: https://www.sfml-dev.org/files/SFML-2.6.0-windows-vc17-64-bit.zip
4. ahora debe configurar visual studio, ingresa a propiedades del proyecto y realiza las siguientes indicaciones:
   - ve a c/c++, luego general y directorios de inclusion adicionales, debe añadir la direccion de la carpeta de nombre include que se encuentra en la carpeta SFML.
   - luego en enlazador, general y directorios de bibliotecas adicionales, debe añadir la direccion de la carpeta lib que se encuentra en la carpeta SFML.
   - en enlazador luego en entrada y dependencias adicionales, debe pegar lo siguiente:
sfml-graphics-d.lib
sfml-window-d.lib
sfml-system-d.lib

Si presenta errores, el siguiente link es el tutorial de la pagina oficial: https://www.sfml-dev.org/tutorials/2.6/start-vc.php
### adicionales juego pokemon
El juego tiene los siguientes adicionales:
- esta ilustrado en SFML
- los personajes tienen movimiento a la hora de cumplir la accion
- hay 4 pokemones distintos y el jugador puede escoger cualquiera
- el enemigo escoge un pokemon distinto al que el jugador eligio
- hay 4 opciones:
  1. golpe normal
  2. golpe especial( mayor daño pero te quita vida)
  3. defenderse
  4. huir
- en la interfaz se muestran los personajes, la vida de ambos, el menu y la accion que realiza el enemigo
# IMPORTANTE
Para jugar se debe correr el programa, escoger el pokemon en la terminal y ya se puede jugar en la ventana batalla pokemon.
