from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Canciones(BaseModel):
    id: int
    Artista: str
    Album: str
    Cancion: str 
    Lanzamiento: int
    Sencillo: str

canciones_list=[
    Canciones(id=0, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Se quiere, se mata', Lanzamiento= 1995, Sencillo= "Si"),
    Canciones(id=1, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Quiero', Lanzamiento= 1995, Sencillo= "No"),
    Canciones(id=2, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Te necesito', Lanzamiento= 1995, Sencillo= "No"),
    Canciones(id=3, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Antologia', Lanzamiento= 1995, Sencillo= "Si"),
    Canciones(id=4, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Donde estas corazon', Lanzamiento= 1995, Sencillo= "Si"),
    Canciones(id=5, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Pies descalzos', Lanzamiento= 1995, Sencillo= "No"),
    Canciones(id=6, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Te espero sentada', Lanzamiento= 1995, Sencillo= "No"),
    Canciones(id=7, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Estoy aqui', Lanzamiento= 1995, Sencillo= "Si"),
    Canciones(id=8, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Pienso en ti', Lanzamiento= 1995, Sencillo= "No"),
    Canciones(id=9, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Un poco de amor', Lanzamiento= 1995, Sencillo= "Si"),
    Canciones(id=10, Artista="Shakira", Album= 'Pies Descalzos', Cancion= 'Vuelve', Lanzamiento= 1995, Sencillo= "No"),

    Canciones(id=11, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Ciega, Sordomuda', Lanzamiento= 1998, Sencillo= "Si"),
    Canciones(id=12, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Si te vas', Lanzamiento= 1998, Sencillo= "No"),
    Canciones(id=13, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Moscas en la casa', Lanzamiento= 1998, Sencillo= "Si"),
    Canciones(id=14, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'No creo', Lanzamiento= 1998, Sencillo= "Si"),
    Canciones(id=15, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Inevitable', Lanzamiento= 1998, Sencillo= "Si"),
    Canciones(id=16, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Octavo dia', Lanzamiento= 1998, Sencillo= "No"),
    Canciones(id=17, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Que vuelvas', Lanzamiento= 1998, Sencillo= "No"),
    Canciones(id=18, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Donde estan los ladrones', Lanzamiento= 1998, Sencillo= "No"),
    Canciones(id=19, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Sombra de ti', Lanzamiento= 1998, Sencillo= "No"),
    Canciones(id=20, Artista="Shakira", Album= 'Donde estan los ladrones', Cancion= 'Ojos asi', Lanzamiento= 1998, Sencillo= "Si"),
    
    Canciones(id=21, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Objection', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=22, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Underneath your clothes', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=23, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Whenever, Wherever', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=24, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Rules', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=25, Artista="Shakira", Album= 'Laundry Service', Cancion= 'The one', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=26, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Ready for the good times', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=27, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Fool', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=28, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Te dejo Madrid', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=29, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Poem to a Horse', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=30, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Que me quedes tu', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=31, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Eyes like yours', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=32, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Suerte', Lanzamiento= 2001, Sencillo= "No"),
    Canciones(id=33, Artista="Shakira", Album= 'Laundry Service', Cancion= 'Te aviso, Te anuncio', Lanzamiento= 2001, Sencillo= "No"),

    Canciones(id=34, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'En tus pupilas', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=35, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'La Pared', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=36, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'La tortura', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=37, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'Obtener un si', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=38, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'Dia especial', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=39, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'Escondite ingles', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=40, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'No', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=41, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'Las de la intuicion', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=42, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'Dia de enero', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=43, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'Lo imprescindible', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=44, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'La pared', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=45, Artista="Shakira", Album= 'Fijacion Oral vol 1', Cancion= 'La tortura remix', Lanzamiento= 2005, Sencillo= "No"),

    Canciones(id=46, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'How do you do', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=47, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Dont bother', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=48, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Illegal', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=49, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'The day and the time', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=50, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Animal city', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=51, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Dreams for plans', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=52, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Hey you', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=53, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Your embrace', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=54, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Costumes makes the clown', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=55, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Something', Lanzamiento= 2005, Sencillo= "No"),
    Canciones(id=56, Artista="Shakira", Album= 'Fijacion Oral vol 2', Cancion= 'Timor', Lanzamiento= 2005, Sencillo= "No"),

    Canciones(id=57, Artista="Shakira", Album= 'She wolf', Cancion= 'She wolf', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=58, Artista="Shakira", Album= 'She wolf', Cancion= 'Did it again', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=59, Artista="Shakira", Album= 'She wolf', Cancion= 'Long time', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=60, Artista="Shakira", Album= 'She wolf', Cancion= 'Why wait', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=61, Artista="Shakira", Album= 'She wolf', Cancion= 'Good stuff', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=62, Artista="Shakira", Album= 'She wolf', Cancion= 'Men in this town', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=63, Artista="Shakira", Album= 'She wolf', Cancion= 'Gypsy', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=64, Artista="Shakira", Album= 'She wolf', Cancion= 'Spy', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=65, Artista="Shakira", Album= 'She wolf', Cancion= 'Mon amour', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=66, Artista="Shakira", Album= 'She wolf', Cancion= 'Lo hecho esta hecho', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=67, Artista="Shakira", Album= 'She wolf', Cancion= 'Anios luz', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=68, Artista="Shakira", Album= 'She wolf', Cancion= 'Loba', Lanzamiento= 2009, Sencillo= "No"),
    
    Canciones(id=69, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'El elias', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=70, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Tanto', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=71, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Miercoles', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=72, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'En el vaticano', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=73, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Sunny Blue', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=74, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Buen dia', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=75, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Sweater geek', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=76, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Si supieras', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=77, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'El gran McGee', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=78, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Muneca', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=79, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Gripa y mundial', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=80, Artista="Pxndx", Album= 'Arroz con leche', Cancion= 'Te invito a mi fiesta', Lanzamiento= 2000, Sencillo= "No"),

    Canciones(id=81, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Christina', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=82, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Claro que no', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=83, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Hola', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=84, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'El chango de los 2 platanos', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=85, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Corazon de un cuento roto', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=86, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Doble gracias', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=87, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Quisiera no pensar', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=88, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Ya no jalaba', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=89, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Cortame con unas tijeras pero no se te olvide el resistol para volverme a pegar', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=91, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Senor payaso', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=92, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Ando pedo y ella esta aqui', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=93, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Ilasha', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=94, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Mala suerte', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=95, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Amiguito', Lanzamiento= 2002, Sencillo= "No"),
    Canciones(id=96, Artista="Pxndx", Album= 'La revancha del principe charro', Cancion= 'Maracas', Lanzamiento= 2002, Sencillo= "No"),

    Canciones(id=97, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Reflexiones de una mente perturbada', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=98, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Disculpa los malos pensamientos', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=99, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Y de la gasolina renacio el amor', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=100, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Cita en el quirofano', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=101, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Ya no es suficiente lamentar', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=102, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= '3+1', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=103, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Mi huracan llevaba tu nombre', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=104, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Promesas/Descepciones', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=105, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Descanso: odiame', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=106, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Cuando no es como debiera ser', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=107, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Miedo a las alturas', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=108, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Hasta el final', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=109, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Figura decorativa sobre fondo ornamental', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=110, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'No tienes oportunidad contra mi antipatica imaginacion', Lanzamiento= 2004, Sencillo= "No"),
    Canciones(id=111, Artista="Pxndx", Album= 'Para ti con desprecio', Cancion= 'Porque todavia podemos decir una vez mas', Lanzamiento= 2004, Sencillo= "No"),

    Canciones(id=112, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'La estrategia perdida', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=113, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'So violento so macabro', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=114, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'El infame estar y no estar', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=115, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Estoy mas solo que ayer pero menos que manana', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=116, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Narcisista por excelencia', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=117, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Procedimientos para llegar a un comun acuerdo', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=118, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Tripulacion, armar toboganes', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=119, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Pathetica', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=120, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Los malaventurados no lloran', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=121, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Tus palabras punzocortantes', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=122, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Atratctivo encontramos en lo mas repugnante', Lanzamiento= 2006, Sencillo= "No"),
    Canciones(id=123, Artista="Pxndx", Album= 'Amantes sunt amentes', Cancion= 'Ah pero como vendo cassettes', Lanzamiento= 2006, Sencillo= "No"),
    
    Canciones(id=124, Artista="Pxndx", Album= 'Poetics', Cancion= 'Popurri para ti', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=125, Artista="Pxndx", Album= 'Poetics', Cancion= 'Fascinante', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=126, Artista="Pxndx", Album= 'Poetics', Cancion= 'Conversacion casual', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=127, Artista="Pxndx", Album= 'Poetics', Cancion= 'El cuello perfecto', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=128, Artista="Pxndx", Album= 'Poetics', Cancion= 'Espiritu pionero', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=129, Artista="Pxndx", Album= 'Poetics', Cancion= 'Solo a terceros', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=130, Artista="Pxndx", Album= 'Poetics', Cancion= 'Abigail', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=131, Artista="Pxndx", Album= 'Poetics', Cancion= 'Casi nula autoestima', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=132, Artista="Pxndx", Album= 'Poetics', Cancion= 'Del rapto y otros pormenores', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=133, Artista="Pxndx", Album= 'Poetics', Cancion= 'Nuestra afliccion', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=134, Artista="Pxndx", Album= 'Poetics', Cancion= 'Que tu cama sea mi hogar', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=135, Artista="Pxndx", Album= 'Poetics', Cancion= 'Adheridos separados', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=136, Artista="Pxndx", Album= 'Poetics', Cancion= 'Martirio de otro', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=137, Artista="Pxndx", Album= 'Poetics', Cancion= 'Soy un ganador', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=138, Artista="Pxndx", Album= 'Poetics', Cancion= 'Lascivamente', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=139, Artista="Pxndx", Album= 'Poetics', Cancion= 'Un tipo de indulgencia', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=140, Artista="Pxndx", Album= 'Poetics', Cancion= 'Amnistia', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=141, Artista="Pxndx", Album= 'Poetics', Cancion= 'Agradable locura temporal', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=142, Artista="Pxndx", Album= 'Poetics', Cancion= 'Espejismos y visiones', Lanzamiento= 2009, Sencillo= "No"),
    Canciones(id=143, Artista="Pxndx", Album= 'Poetics', Cancion= 'Quinta real', Lanzamiento= 2009, Sencillo= "No"),

    Canciones(id=144, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Papercut', Lanzamiento= 2000, Sencillo= "Si"),
    Canciones(id=145, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'One step closer', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=146, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'With you', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=147, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Points of authority', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=148, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Crawling', Lanzamiento= 2000, Sencillo= "Si"),
    Canciones(id=149, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Runaway', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=150, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'By myself', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=151, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'In the end', Lanzamiento= 2000, Sencillo= "Si"),
    Canciones(id=152, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'A place for my head', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=153, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Forgotten', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=154, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Cure for the itch', Lanzamiento= 2000, Sencillo= "No"),
    Canciones(id=155, Artista="Linkin Park", Album= 'Hybrid theory', Cancion= 'Pushing me away', Lanzamiento= 2000, Sencillo= "No"),

    Canciones(id=156, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Foreword', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=157, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Dont stay', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=158, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Somewhere i belong', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=159, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Lying from you', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=160, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Hit the floor', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=161, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Easier to run', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=162, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Faint', Lanzamiento= 2003, Sencillo= "Si"),
    Canciones(id=163, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Figure.09', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=164, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Breaking the habit', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=165, Artista="Linkin Park", Album= 'Meteora', Cancion= 'From the inside', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=166, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Nobody is listening', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=167, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Session', Lanzamiento= 2003, Sencillo= "No"),
    Canciones(id=168, Artista="Linkin Park", Album= 'Meteora', Cancion= 'Numb', Lanzamiento= 2003, Sencillo= "Si"),

    Canciones(id=169, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Wake', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=170, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Given up', Lanzamiento= 2007, Sencillo= "Si"),
    Canciones(id=171, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Leave out all the rest', Lanzamiento= 2007, Sencillo= "Si"),
    Canciones(id=172, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Bleed it out', Lanzamiento= 2007, Sencillo= "Si"),
    Canciones(id=173, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Shadow of the day', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=174, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'What ive done', Lanzamiento= 2007, Sencillo= "Si"),
    Canciones(id=175, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Hands held high', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=176, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'No more sorrow', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=177, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'Valentines day', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=178, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'In between', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=179, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'In pieces', Lanzamiento= 2007, Sencillo= "No"),
    Canciones(id=180, Artista="Linkin Park", Album= 'Minutes to midnight', Cancion= 'The little things give you away', Lanzamiento= 2007, Sencillo= "No"),
    
    
    Canciones(id=181, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'The requiem', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=182, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'The radiance', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=183, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Burning in the skies', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=184, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Empty spaces', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=185, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'When they come for me', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=186, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Robot boy', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=187, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Jornada del muerto', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=188, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Waiting for the end', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=189, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Blackout', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=190, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Wretches and kings', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=191, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Wisdomw, justice and love', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=192, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Iridescent', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=193, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Fallout', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=194, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'The catalyst', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=195, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'The messenger', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=196, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'New divide', Lanzamiento= 2010, Sencillo= "No"),
    Canciones(id=197, Artista="Linkin Park", Album= 'A thousand suns', Cancion= 'Black Birds', Lanzamiento= 2010, Sencillo= "No"),

]


@app.get('/canciones')
async def canciones():
    return canciones_list

@app.get('/canciones/{id}')
async def canciones(id:int):
    nueva= filter (lambda Canciones: Canciones.id==id, canciones_list)
    try:
        return list(nueva)[0]
    except:
        return{"error": "No se ha encontrado el usuario"}
    
@app.get('/canciones2/')
async def canciones(artista:str, album:str):
    nueva= filter(lambda Canciones: Canciones.Artista==artista, canciones_list)
    nueva1=filter(lambda Canciones: Canciones.Album==album, nueva)
    try:
        return list(nueva1)
    except:
        return {"error": "no se ha encontrado el usuario"}
    

@app.get('/canciones3/')
async def canciones(artista:str, lanzamiento:int):
    nueva= filter(lambda Canciones: Canciones.Artista==artista, canciones_list)
    nueva1=filter(lambda Canciones: Canciones.Lanzamiento==lanzamiento, nueva)
    try:
        return list(nueva1)
    except:
        return {"error": "no se ha encontrado el usuario"}
    
@app.get('/canciones4/')
async def canciones(artista:str, sencillo:str):
    nueva= filter(lambda Canciones: Canciones.Artista==artista, canciones_list)
    nueva1=filter(lambda Canciones: Canciones.Sencillo==sencillo, nueva)
    try:
        return list(nueva1)
    except:
        return {"error": "no se ha encontrado el usuario"} 

@app.get('/canciones/artista/{artista}')
async def canciones(artista:str):
    nueva= filter (lambda Canciones: Canciones.Artista==artista, canciones_list)
    try:
        return list(nueva)
    except:
        return{"error": "No se ha encontrado el usuario"}
    
@app.get('/canciones/album/{album}')
async def canciones(album:str):
    nueva= filter (lambda Canciones: Canciones.Album==album, canciones_list)
    try:
        return list(nueva)
    except:
        return{"error": "No se ha encontrado el usuario"}
    
@app.get('/canciones/cancion/{cancion}')
async def canciones(cancion:str):
    nueva= filter (lambda Canciones: Canciones.Cancion==cancion, canciones_list)
    try:
        return list(nueva)[0]
    except:
        return{"error": "No se ha encontrado el usuario"}