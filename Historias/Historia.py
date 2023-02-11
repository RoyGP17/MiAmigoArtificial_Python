## Las importaciones ###
from Libro import libro, libroAventura, libroComedia, libroDrama
from AdminLibros import Admin_Libros

class Historias:

    def leer_libro(self):
        objecto_LibroDrama1 = libroDrama("Henry James", "\n\tLas bostonianas", "Drama",
                                         "\nEl escenario de la historia es Boston y su barrio; relata un episodio relacionado con el denominado «movimiento de la mujer». "
                                         + "\nLos personajes que figuran en ella son en su mayoría personas de tipo reformista radical, "
                                         + "\nespecialmente interesados en lograr que las mujeres se emancipen, concederles el sufragio, "
                                         + "\nliberarlas de la esclavitud, coeducarlas con los hombres, etc. Lo consideran el gran problema "
                                         + "\ndel momento: la reforma más urgente y sagrada. La heroína es una joven muy lista y «talentosa»,"
                                         + "\n relacionada de nacimiento y por las circunstancias con un círculo inmerso en esas opiniones y"
                                         + "\n en toda nueva agitación, hija de antiguos abolicionistas, espiritualistas, trascendentalitas,"
                                         + "\n etc. Ella también se interesa por la causa, pero es objeto de un interés todavía mayor por"
                                         + "\n parte de su familia y amigos, que han descubierto en ella un extraordinario talento natural"
                                         + "\n para hablar en público con el que la creen capaz de convencer a una audiencia numerosa y "
                                         + "\nprestar una gran ayuda en la liberación de su sexo. La quieren como a una especie de apóstol "
                                         + "\no de redentora. Ella está de muy buen ver, y su don para hablar es todo un estímulo. Tiene una "
                                         + "\namiga íntima, otra joven, que procede de un círculo social totalmente distinto (una exclusiva "
                                         + "\nfamilia rica y conservadora) y que se ha lanzado a esas cuestiones con intenso fervor y alberga "
                                         + "\nuna apasionada admiración por nuestra muchacha, sobre la cual, gracias a un carácter completamente "
                                         + "\ndistinto, ha adquirido una gran influencia. Ella tiene dinero propio, pero carece de talento para "
                                         + "\naparecer en público y sueña con que ella y su amiga (una usando su dinero y la otra su elocuencia) "
                                         + "\nconsigan, trabajando codo con codo, revolucionar la condición de las mujeres. Lo considera una "
                                         + "\ntarea noble y ambiciosa, una misión por la que hay que sacrificar todo lo demás, y cuenta tácitamente "
                                         + "\ncon su amiga. Sin embargo, ésta conoce a un joven que se enamora de ella y por el que ella a su "
                                         + "\nvez se interesa enormemente, pero que, debido a su temperamento realista y conservador, se opone "
                                         + "\nfirmemente al sufragio femenino y otras reformas parecidas. Cuanto más ve a la heroína, más la ama "
                                         + "\ny más decidido está a liberarla de las garras de sus amigos reformistas, a los que detesta con toda "
                                         + "\nsu alma. Le pide que se case con él y no le oculta que, si lo hace, deberá renunciar por completo a "
                                         + "\nsu «misión». Ella cree que lo ama, pero que el sacrificio de la citada misión sería terrible y que "
                                         + "\nla decepción que causaría a su familia y amigos, y sobre todo a la joven rica, sería peor. Su amado "
                                         + "\nes un pariente lejano de la joven rica, quien, en mala hora, por casualidad, y antes de haberse "
                                         + "\ninformado de las opiniones del joven (ha pasado diez años en el Oeste), se lo presentó. Le pide a "
                                         + "\nsu amiga que se mantenga firme en nombre de su amistad y de todas las esperanzas depositadas en el "
                                         + "\ntalento de la joven. La historia relata la lucha que se produce en la mente de ésta")

        objecto_LibroDrama2 = libroDrama("Alexandre Dumas", "\n\tLa dama de las camelias", "Drama",
                                         "\nMarguerite Gautier tiene varios amantes, "
                                         + "\nun palco en la Ópera y siempre lleva consigo un ramo de camelias. Es una cortesana por la que"
                                         + "\n los hombres se pelean, y la sociedad parisina la envidia y la crítica a partes iguales. "
                                         + "\nArmand Duval es un joven que no puede costearse el lujo que es Marguerite, pero que está tan"
                                         + "\n enamorado de ella que sería capaz de hacer cualquier cosa para que lo ame del mismo modo."
                                         + "\n Sin embargo, son más que celos o diferencias de clase lo que los separan, y descubrirán que"
                                         + "\n el amor no siempre lo puede todo. La dama de las camelias, escrita por Alejandro Dumas hijo"
                                         + "\n en 1848, se basa en eventos de la vida del propio autor. Un clásico de la literatura"
                                         + "\n francesa, esta novela trata la posible redención de Marguerite gracias al amor de Armand, y "
                                         + "\ncrea un retrato logrado de la sociedad del momento. La protagonista se mueve entre personas que"
                                         + "\n no la aceptan pero que deben soportarla, y muestra el trato que las cortesanas recibían allí "
                                         + "\ndonde fueran, a medio camino entre el asco y la fascinación. Tal fue el éxito de la novela, "
                                         + "\nque inspiró la ópera La traviata, de Giuseppe Verdi. El narrador de los acontecimientos nunca "
                                         + "\nnos revela su nombre, simplemente retransmite los hechos como Armand se los cuenta. Mantiene"
                                         + "\n la primera persona desde la primera página mientras nos guía por la historia para averiguar "
                                         + "\nquién era la verdadera Marguerite Gautier. La novela empieza explicándonos la subasta que tiene"
                                         + "\n lugar después de su fallecimiento, y a partir de ahí retrocedemos hasta el momento en que "
                                         + "\nArmand la conoció. En adelante, descubrimos una preciosa pero dura historia de amor. Esta "
                                         + "\nnovela se alimenta de los sentimientos de los personajes y la relación de los protagonistas "
                                         + "\npara mantener el interés del lector. La trama avanza a buen ritmo y, en apenas doscientas "
                                         + "\npáginas, encontramos una historia compleja y llena de detalles. Nadie será capaz de dejar el "
                                         + "\nlibro hasta averiguar qué se esconde detrás de la misteriosa dama de las camelias.")

        objecto_LibroDrama3 = libroDrama("Anton Chejov", "\n\tLa Dama Del Perrito", "Drama",
                                         "\nFue compuesto este cuento en el año de 1899 en Yalta, "
                                         + "\na orillas del mar Negro, donde estaba radicado el autor desde el año anterior. Se considera "
                                         + "\nautobiografía ya que su protagonista, Dmitrri Dmitrich Gurov, se encuentra en Yalta desde hace "
                                         + "\nquince días, pero su verdadera residencia es Moscú.Se sabe que el tiempo que transcurrió en Yalta,"
                                         + "\n se convirtió para Chejov en un destierro en el cual anhelaba a su capital, pero era consciente de"
                                         + "\n que ya no volvería más debido a que su enfermedad se iba agravando. Gurov encuentra a Ana Serguevna,"
                                         + "\n la “dama del perrito”, en Yalta: “Veía pasar a una dama joven de nediana estatura y tocada con "
                                         + "\nuna boina; tras ella corría un blanco Lulú Este encuentro ocurre como algo casual; pero antes que "
                                         + "\nse lleve a cabo, al narrador se escapa por un momento del asunto principal, para describir el mundo "
                                         + "\nde Gurov, en el cual se puede ver sin mucho esfuerzo la vida del mismo Chejov: “no había cumplido "
                                         + "\naún los cuarenta años… y ahora su esposa parecía dos veces mayor que él.Era esta una mujer alta, "
                                         + "\nde porte severo y glacial, importante y rígida y se hacía llamar haci misma intelectual “. Encontrarse "
                                         + "\ncon ella, Ana Serguevna encanta por su aire de prolongada tristeza.Una aventura ocurre entre los dos, "
                                         + "\ncon todos los eventos que implican este tipo de relación: la previa amistad, las confidencias mutuas, "
                                         + "\netc. Van al hotel donde ella se hospeda. Vienen luego los sentimientos de culpabilidad de Ana por "
                                         + "\nsu conducta indigna. Nuevos encuentros se suceden.El vínculo que une a la pareja es tímido, distraído, "
                                         + "\nmuestra a los ojos del lector un afecto profundo e irremplazable. Los escenarios del idilio son "
                                         + "\ntenues, leves, bordados por la tristeza, otoñales como son los protagonistas, cuyo sosiego se "
                                         + "\nilumina con el resplandor del amor final que Chejov presenta como exiguo, pero que es, en últimas, "
                                         + "\nlo único que poseen.Todo bajo una atmosfera opresiva y angustiosa de lo cotidiano, como representación "
                                         + "\nde la desdicha que asecha a una pación real. El constante que se observa entre el paisaje de neblina "
                                         + "\ny los personajes es como una evocación, un canto de poder del amor; el último homenaje de un escritora "
                                         + "\npara con las sensaciones más elevadas.La vida mata las ilusiones juveniles Demasiadas veces los hombres "
                                         + "\nse reconocen en sus propios fracasos. Pero sola unasola emoción le es dable saborear al hombre en su"
                                         + "\n madurez y senectud: la capacidad de amar de manera mínima, pero como un prodigio capaz de redimirlo"
                                         + "\n de cualquier fracaso.")

        objecto_LibroAventura1 = libroAventura("Julio Verne", "\n\tViaje añ centro de la tierra", "Aventura",
                                               "\nPublicada en 1864, Viaje al centro de la Tierra "
                                               + "\nfue la segunda de las grandes novelas de aventuras que darían fama universal al escritor francés "
                                               + "\nJulio Verne. La acción comienza en la apacible mansión de un viejo barrio de Hamburgo donde reside "
                                               + "\nel profesor Lidenbrock, geólogo y mineralogista. Conviven con el irascible profesor una protegida "
                                               + "\nsuya, Graüben, y un sobrino, Axel, que ayuda en sus trabajos a su tío y está enamorado en secreto de "
                                               + "\nla dulce Graüben. El ritmo normal de las cosas se ve profundamente trastornado a consecuencia de un "
                                               + "\nantiguo criptograma descubierto en un manuscrito rúnico. En tal criptograma un alquimista islandés "
                                               + "\ndel siglo XVI, Arne Saknüssemm, dejó oculta una extraordinaria revelación: por uno de los cráteres "
                                               + "\ndel Sneffels, volcán extinto de Islandia, Saknüssemm había logrado penetrar hasta el centro de la "
                                               + "\nTierra. Sin perder un solo instante, el profesor comienza a organizar la expedición. Y un mes más "
                                               + "\ntarde, el profesor Lidenbrock y su sobrino Axel, junto con Hans Bjelke, un guía islandés tan flemático "
                                               + "\ncomo exaltado es su nuevo jefe, se internan en las entrañas de la Tierra. El viaje está lleno de "
                                               + "\nemocionantes peripecias, sucesos sorprendentes y penalidades imprevistas, desde la falta del agua hasta "
                                               + "\nlas dificultades para orientarse, que llevan a Axel a perderse y a reintegrarse al grupo gracias a los "
                                               + "\necos que difunden la voz de su tío. Algunos de su más interesantes episodios son la travesía en balsa "
                                               + "\nde un mar subterráneo (iluminado por un fenómeno eléctrico desconocido) en cuyas riberas crecen "
                                               + "\nvegetaciones exuberantes de épocas remotas, la lucha mortal entre un ictiosauro y un plesiosauro, "
                                               + "\nla tempestad y el naufragio, el descubrimiento de fósiles humanos y de un cadáver momificado de la "
                                               + "\népoca cuaternaria y el encuentro de un semihumano y gigantesco pastor de una manada de mastodontes. "
                                               + "\nUn puñal oxidado y unas letras grabadas en la roca por el alquimista muestran todavía la ruta que "
                                               + "\ndeben seguir, pero el camino ha sido obstruido por un seísmo. Deciden minar el obstáculo, y la "
                                               + "\nexplosión, esperada desde lejos sobre la balsa, desencadena un cataclismo: los viajeros siguen el "
                                               + "\ncamino del alquimista Saknüssemm, pero empujados por todo un mar. Después de una terrible caída en "
                                               + "\nlos abismos que hierven y rugen, el agua eleva la balsa por un túnel vertical, desapareciendo, "
                                               + "\nevaporadas por el calor, las materias eruptivas que la impelen. Y entre los terroríficos fenómenos "
                                               + "\nde una erupción, los exploradores, que habían entrado en Islandia por el cráter extinto del Sneffels, "

                                               + "\nson expulsados por la actividad del volcán Estrómboli, en la isla italiana del mismo nombre.")

        objecto_LibroAventura2 = libroAventura("H. G. Wells", "\n\tLa máquina del tiempo", "Aventura",
                                               "Un científico inventa "
                                               + "\nuna máquina para viajar a través del tiempo. En un viaje experimental llega al año 802.701 y encuentra la tierra "
                                               + "\nhabitada por los Eloi, pacíficos y ociosos. El Viajero del Tiempo deduce que están tan avanzados "
                                               + "\nque unas máquinas deben de trabajar por ellos. Más tarde descubrirá a los malvados y depredadores "
                                               + "\nMorlocks, y habrá de escapar para salvar la vida. A su regreso al presente su relato es recibido "
                                               + "\ncon escepticismo. La máquina del tiempo, escrita en 1895 por Herbert George Wells, se halla en los "
                                               + "\ninicios de la novela de ciencia-ficción. Sigue conservando el mismo poder de fascinación y vigor "
                                               + "\nnarrativo que le valieron el éxito inmediato en el momento de su publicación. Afortunada síntesis "
                                               + "\nde los conocimientos científicos del autor, del maquinismo, (creencia que confiaba en que las "
                                               + "\nmáquinas serían la salvación de la humanidad), que hacía furor en la época y de la visión escéptica"
                                               + "\n de H.G. Wells (1866-1946) respecto al rumbo tomado por la sociedad que le tocó vivir, el relato "
                                               + "\ndescribe un futuro inquietante en el que dos razas semibestiales, los eloi y los morlock, comparten"
                                               + "\n en una peculiar simbiosis un planeta extraño y desolado sobre el que se han cernido catástrofes "
                                               + "\ny transformaciones, pero en el que brilla aún, como tenue esperanza, un hálito de humanidad.")

        objecto_LibroAventura3 = libroAventura("Lewis Carroll",
                                               "\n\tLas aventuras de Alicia en el país de las maravillas", "Aventura",
                                               "Alicia,"
                                               + "\nla protagonista, es una niña que se encuentra con su hermana, apoyada en un árbol leyendo un libro "
                                               + "\nDe repente ve un conejo blanco que lleva un reloj y habla, y tiene mucha prisa, y decide seguirlo, "
                                               + "\nAl seguir el conejo, Alicia se cae por un pozo en el que tarda mucho tiempo en llegar abajo llega a"
                                               + "\n muchos lugares extraños donde conoce a personajes sumamente extraños, Alicia se encuentra con el "
                                               + "\ngato de la duquesa que le dice los sitios dónde puede ir Alicia se decidir a la casa del sombrerero "
                                               + "\nque está acompañado por la liebre de Marzo y un lirón Luego vuelve a la casa del conejo, coge la "
                                               + "\nllave, se hace pequeña y pasa por la puerta minúscula Ve a unos soldados pintando unas rosas blancas"
                                               + "\n de color rojo, La reina encuentra a Alicia y dice que le corten la cabeza sin motivo alguno. Pero "
                                               + "\nmás tarde se disculpa por haber actuado así, y le propone un partido decroquet muy particular Vuelven"
                                               + "\n a encontrarse con el gato, y como es de la duquesa, y la duquesa estaba en el calabozo, la liberan"
                                               + "\n para que pueda hablar con su gato Alicia se va con un grifo al escuchar la historia de la falsa "
                                               + "\ntortuga. Le cuentan sobre el baile de las cuatro langostas y lo bailan delante de Alicia Finalmente "
                                               + "\nvan a un juicio muy extraño en el que Alicia tiene que declarar y niega haber robado las tartas de "
                                               + "\nla reina Por último Alicia se despierta. Todo ha sido un sueño.")

        objecto_LibroComedia1 = libroComedia("Alfonso de Valdés", "\n\tLa vida de Lazarillo de Tormes", "Comedia",
                                             "La novela cuenta la vida de un niño llamado Lázaro"
                                             + "\n que al principio era inocente, pero se convirtió en pícaro para poder sobrevivir. Sus padres "
                                             + "\nfueron encarcelados por varios crímenes . Lázaro, al verse huérfano, buscó la compañía de algún "
                                             + "\namo y se hizo mozo de un ciego pero no duró mucho tiempo con él . El ciego ganaba mucho dinero, "
                                             + "\npero a él no le daba nada de comer y lo tenía muerto de hambre . Así que lo dejó y fue a buscar "
                                             + "\notro. Un día, que iba mendigando, se encontró a un clérigo que le preguntó que si buscaba amo . "
                                             + "\nLázaro le dijo que sí . El clérigo tenía un arca y en el arca tenía la comida: pan , agua , arroz"
                                             + "\n … Lázaro aprovechó que llegó a su casa un calderero y pidió la llave el arca para coger cosas "
                                             + "\npara comer . Como el arca era vieja y tenía agujeros el clérigo pensó que eran los ratones los "
                                             + "\nque mordisqueaban el pan. Cierto día, el clérigo se dio cuenta y le dijo que no se merecía un criado "
                                             + "\ntan listo. Lo echó y le dijo que buscara amo . Lázaro tuvo suerte de llegar a la gran ciudad de "
                                             + "\nToledo, pues allí encontró de nuevo un amo . Este fue un escudero. El escudero tenía pinta de ser "
                                             + "\nmuy rico pero era pobre . Al escudero le perseguía la justicia porque no pagaba sus deudas . Y Lázaro "
                                             + "\nno quiso estar con él . Unas mujeres que cuidaban a Lázaro le dijeron que se fuera con un fraile "
                                             + "\namigo de ellas . Pero Lázaro solo duró ocho días con él pues andaba mucho y a él no le gustaba andar "
                                             + "\n. A los pocos días sirvió a un buldero . El buldero tenía mucha experiencia para mentir y siempre , "
                                             + "\nsiempre se estaba peleando con un alguacil . Estuvo cuatro años con él pero como era muy mentiroso "
                                             + "\nLázaro decidió dejarlo . Un día que entró en la catedral uno de sus capellanes decidió contratarlo . "
                                             + "\nLe hizo cargo de un burro, cuatro cántaros y un látigo y empezó a vender agua por el pueblo . Y cuando "
                                             + "\nreunió el dinero suficiente, se compró ropa nueva y dejó al capellán . Después de esto sirvió a un "
                                             + "\nalguacil con el que no duró mucho y tiempo porque tenía un oficio muy peligroso . Un día unos delincuentes"
                                             + "\n cogieron al alguacil y lo maltrataron, pero a Lázaro no lo pillaron . Y Lázaro siguió buscando "
                                             + "\namo . Lázaro consiguió por último un oficio real . Y a los pocos días un cura lo casó con una de "
                                             + "\nsus criadas y les alquiló una casa al lado de la suya . Vivieron felices")

        objecto_LibroComedia2 = libroComedia("Graeme Simsion", "\n\tEl proyecto esposa", "Comedia",
                                             "Don Tillman, profesor de "
                                             + "\nGenética en la universidad, un hombre atrapado en una visión de la realidad extremadamente "
                                             + "\nrígida, nunca ha tenido una segunda cita con una mujer. Sin embargo, conocedor de los estudios"
                                             + "\n que demuestran que los hombres que viven en pareja son más felices que los solteros, se "
                                             + "\nembarca de lleno en lo que bautiza El Proyecto Esposa, cuyo primer paso consiste en redactar "
                                             + "\nun cuestionario de dieciséis páginas para encontrar la pareja perfecta: una mujer puntual, que"
                                             + "\n no fume ni beba y se adapte a su reglamentada existencia. Y entonces conoce a Rosie Jarman, "
                                             + "\nque es una mujer guapa, capaz y luchadora, pero trabaja en un bar, fuma, bebe, y llega siempre"
                                             + "\n tarde: ¡totalmente descartada para el Proyecto Esposa! Ella tiene un proyecto propio, encontrar"
                                             + "\n a su padre biológico, y nuestro excéntrico profesor se encontrará inventando excusas a diario "
                                             + "\ny saltándose sus estrictas reglas con tal de verla y ayudarla poniendo sus conocimientos de "
                                             + "\ngenética al servicio de su causa. Don y Rosie se lanzan así a una intrépida, divertidísima "
                                             + "\naventura que demuestra que el amor no se busca sino que acude a nosotros cuando menos lo esperamos.")

        objecto_LibroComedia3 = libroComedia("Christopher Moore", "\n\tUn trabajo muy sucio", "Comedia",
                                             "Nuestra historia comienza con Charlie Asher, "
                                             + "\nun tío que está ya de por si un poco mal de lo suyo, propietario de un edificio enterito en San "
                                             + "\nFrancisco y también de una tienda de segunda mano que tanto amaba su padre, y tanto odia su madre. "
                                             + "\nA parte del éxito laboral, tiene la suerte de estar casado con una mujer preciosa, inteligente, "
                                             + "\ndivertida... Pero Rachel, el centro de su universo y sin duda el amor de su vida, muere después "
                                             + "\nde dar a luz a su hija, Sophie. De repente y sin apenas tener tiempo para darse cuenta, nuestro "
                                             + "\nprotagonista se encuentra totalmente solo con una extraña que no deja de mirarlo con curiosidad."
                                             + "\n Deprimido a más no poder, pero sin llegar a ser pesado, Charlie tendrá que reunir las fuerzas "
                                             + "\nnecesarias para enfrentarse a esta nueva situación. Son muchas las cosas de las que tiene que "
                                             + "\nhacerse cargo, la tienda, sus empleados que no dejan de causarle problemas menores, y ahora esa "
                                             + "\nextraña que tan solo hace tres cosas, típicas de los bebés de su edad. Pero eso no le preocupa a"
                                             + "\n Charlie, no en un principio al menos. Tiene un problema mucho más gordo al que enfrentarse. "
                                             + "\nNadie le cree. Está seguro que ese negro de más de dos metros de altura y vestido de verde menta,"
                                             + "\n al que vio en el cuarto de su mujer antes de hallarla muerta, es el responsable de todo. Tiene "
                                             + "\nque encontrarlo. Pero sucesos extraños comienzan a ocurrir a su alrededor, que en un principio parecen "
                                             + "\nfrutos de la casualidad. Sin embargo, pronto nos daremos cuenta que hasta el más insignificante "
                                             + "\nde los problemas de Charlie guarda una relación directa son su nuevo trabajo a jornada completa: "
                                             + "\nes la muerte. Una historia que bien le puede parecer una pérdida de tiempo total a algunos, en mi "
                                             + "\nopinión cumple con creces la idea principal del autor, la de divertir a su público y es algo que el "
                                             + "\nseñor Moore consigue sin duda. No es ni de lejos lo mejor que he leído, pero guardo un extraño "
                                             + "\ncariño a esta novela en mi interior, infundido quizás por el buen rato que me hizo pasar años atrás. "
                                             + "\nAdemás, sus personajes un poco chiflados (unos más que otros) despiertan un profundo sentimiento de "
                                             + "\ncariño y simpatía en mi interior. Charlie sin duda si soportas su constante depresión de las primeras "
                                             + "\npáginas, y te acostumbras a su locura, se convertirá en un protagonista que hará la novela mucho "
                                             + "\nmás llevadera y divertida. Pero si no consigues conectar con él desde casi el mismisimo principio, "
                                             + "\nme temo que te llevarás un buen chasco, pues lo que es la historia en sí sin Charlie no es gran cosa."
                                             + "\nDe los demás personajes sin duda destacar a la dulce e inocente criatura Sophie que se hace querer. "
                                             + "\nAdemás, tendrá un papel importante a lo largo de toda la historia. Luego están sus queridos perritos "
                                             + "\nque se comen extintores y destruyen autobuses... ¡hasta los malos son divertidos! Vamos, que en su "
                                             + "\nconjunto los personajes están bastante bien logrados. Si hablamos del ritmo, claro que hay algunos "
                                             + "\nbajones pero en general siempre está pasando algo, menos al principio que puede aburrir un poco y "
                                             + "\nla parte del final resultar desconcertante e inesperada, te mantiene bastante bien enganchado y "
                                             + "\nse lee en un suspiro. ")

        ##CREAMOS UN OBJETO  DE ADMI_LIBROS

        admin_libros1 = Admin_Libros()

        admin_libros1.agrega_libro(objecto_LibroDrama1, "DRAMA", 0)
        admin_libros1.agrega_libro(objecto_LibroDrama2, "DRAMA", 1)
        admin_libros1.agrega_libro(objecto_LibroDrama3, "DRAMA", 2)

        admin_libros1.agrega_libro(objecto_LibroAventura1, "AVENTURA", 0)
        admin_libros1.agrega_libro(objecto_LibroAventura2, "AVENTURA", 1)
        admin_libros1.agrega_libro(objecto_LibroAventura3, "AVENTURA", 2)

        admin_libros1.agrega_libro(objecto_LibroComedia1, "COMEDIA", 0)
        admin_libros1.agrega_libro(objecto_LibroComedia2, "COMEDIA", 1)
        admin_libros1.agrega_libro(objecto_LibroComedia3, "COMEDIA", 2)

        admin_libros1.menu()