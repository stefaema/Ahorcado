# Requerimientos: 
Se desea crear un juego similar al juego popular el Ahorcado, con la posibilidad de ser jugado por mínimo 2 jugadores (1 adivinadores y 1 acusante por ronda). 
Empieza con la pantalla de carga que tiene:
- Título del Juego ("Ahorcado")
- Animación de carga
Luego se pasa a la pantalla del Menú Principal, que otorgará el contexto al jugador (a modo de storyline) con un botón para proceder al juego como tal.
Previo a proceder al juego se genera una pantalla donde el acusante tiene un input field del teclado para proveer la palabra a adivinar
Dentro de la pantalla de juego, se halla un fondo de naturaleza estética, con un personaje dibujado en la horca, el cual puede cambiar de estado (Estado = vidas faltantes). Al principio, el personaje no tiene ninguna vida faltante y si tiene el máximo de vidas faltantes, termina el juego.
Además, se encuentra allí un input field (el cual es carácter por carácter) que podrá cumplir la función, en conjunto con el botón de adivinar, de realizar una adivinanza.
Esa función de adivinanza, podrá ser correcta o incorrecta. En el caso correcto, la palabra secreta disminuye en ese carácter acertado y el personaje permanece en el mismo estado.
En caso de perder, el personaje cambia de estado y además se agrega una letra a la lista de caracteres probados, los cuales se muestran en pantalla.
Que termine el juego perdiendo supone 6 errores en total, más un nuevo botón para volver a jugar que te lleva a la pantalla de elección de la palabra.
Que termine el juego ganando supone que no se llegó a los errores, más un nuevo botón para volver a jugar que te lleva a la pantalla de elección de la palabra.

# Mockup

![Pantalla de carga](<Imagen de WhatsApp 2024-04-11 a las 17.13.44_673b68b9-1.jpg>)

![Pantalla de menu](<Imagen de WhatsApp 2024-04-11 a las 17.14.04_ecadd698.jpg>)

![Pantalla de elección de palabra](<Imagen de WhatsApp 2024-04-11 a las 17.20.06_31892a42.jpg>)

![Pantalla de juego](<Imagen de WhatsApp 2024-04-11 a las 17.14.26_8b34baa7.jpg>)

![Pantalla de victoria](<Imagen de WhatsApp 2024-04-11 a las 17.15.07_94841613.jpg>)

![Pantalla de derrota](<Imagen de WhatsApp 2024-04-11 a las 17.14.48_01f7508a.jpg>)