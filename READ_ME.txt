El juego se ejecuta desde el archivo Alea_iacta_est

QUIERO QUE JUEGUES ANTES PARA NO SPOILEAR

Consta de una intro escapeable, un menu de inicio, un nivel 1 , transición al nivel 2 con marcador, level 2 y lvl 3
A su vez, si se pierde, salta una ventana para jugar de nuevo o rendirse. Si ganas ventana de victoria.

Una intro estupenda haciendo homenaje a la saga de las sagas

En el nivel 1 más allá de lo evidente (juego de nave con disoparos):
- está una API climatica la cual se controla desde el archivo tiempop.py donde se elige la ciudad. (podría haberlo incluido en el menu de inicio... lo sé)
- esta API alimenta diversas cositas en la interface. velocidad del viento, los grados que mueven una brújila y el clima. EN funcion de si lluve, hace bueno o nubes salen unas imágenes y sonido diferente.
(quería ponerla como "resistencia" la velocidad, no sería dificil, meter una velocidad negativa en función de los grados en la clase nave si entre 0 y 180 -m/s y entre y de 181 a 360 +m/s)
- metí en su momento rotación a los meteoritos, pero al inyectarlo en el for me hacían cosas raras...puedes ver en el git los push en los que lo consigo...mucha ilusión para luego no usarlo...
- No podía faltar nuestros amados numeros romanos LOs cuales le dan el tema al juego. Son el marcador, meteoritos y la temática básicamente. xDDDDDDDDDDDDDDDDDD
- Un fondo animado, se mueven con cada segundo que pasa.
- Hay una aceleración en la nave, no muy lograda pero bueno, estar está
- Genero un marcador en función del tiempo que has tardado en conseguir los puntos requeridos, el cual se resta a la preción y la vida, las cuales cuanto más mejor.
- Me ha encantado conectar la base de datos, creo que tiene un sin fin de utilidades, quería meter una especie de top 5, pero es un verdadero coñazo ya que pygame no permite escribir en más de una línea
tendría que hacer una funcióne especifica contando caracteres etc... era demasié.
- Si pierdes en el nlvl sale un menu de nuevo con PLAY o Rendirse.
- Hay una transición al lvl dos con el marcador pra que no sea tan brusco.
- Como recurso, he aprendido lo de los sprits, útiles pero un quebradero de cabeza.

En el nivel 2 está la sorpresa.
- Un shooter. EN que **** momento se me ocurrió meterme en este lio. 
- No ha habido forma humana de hacerlo con los sprites, o conseguía el movimiento de los pjts o conseguía la alternancia de los fotograma, al final una clase de toda la vida y chin pum
- Tenía creada una cruceta que en función de si hacías click se ponia una imagen y si soltabas otra, una chorrada estética.
- Me ha costado el movimiento de los enemigos y lcoalizarlos con el ratón, no estoy del todo convencido con el resultado, pero me ha hecho gracia.
- Quería poner varios enemigos diferentes, pero no he tenido tiempo suficiente.
- Del mismo modo que en el lvl 1 si pierdes tienes el propio menú para reiniciar o salir.
- Aquí no hay tiempo, es meramente simbólico, simplemente con matarnos unas cuantas veces saltas al siguiente lvl que es una chorrada.


Soy consciente de lo caótico que es, pero he hecho una especie de mecano, ya que intentaba sacar tiempo en el trabajo de debajo de las piedras, me lo pasaba a un pen y toido lo he sacado de videos de youtube y foros.

Que es algo que he tenido siempre en cuenta, he querido hacerlo todo solo, estamparme contra todo por mi cuenta y que considero que es la única forma de aprender, eso y muchas horas.
(me van a echar del curro y la novia me va a dar pal pelo, menos mal que ya termina...)
Igualmente, he disfrutado como un enano y cosas que me he dejado en el tintero.

Como anotación personal:

No tenía ni de lejos pensado hacer el pygame. De hecho, te entendí mal hace un mes o así y creía que el proyecto era o una página web / sitio web / API o pygame. Y me he hecho una página web personal
con django y css/sass durante todo el mes de septiembre (por eso no fui a las últimas clases de FLASK) Es evidente que me salió el tiro por la culata, pero he aprendido muchíiiisimo.
Estoy francamente enamorado de ese framework.




