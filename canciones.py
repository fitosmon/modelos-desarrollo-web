from fastapi import FastAPI

app= FastAPI()

canciones = {
    1:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Se quiere, se mata'},
    2:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Quiero'},
    3:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Te necesito'},
    4:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Antologia'},
    5:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Donde estas corazon'},
    6:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Pies descalzos'},
    7:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Te espero sentada'},
    8:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Estoy aqui'},
    9:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Pienso en ti'},
    10:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Un poco de amor'},
    11:{'Artista': 'Shakira', 'Album': 'Pies Descalzos', 'Cancion': 'Vuelve'},

    12:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Ciega, Sordomuda'},
    13:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Si te vas'},
    14:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Moscas en la casa'},
    15:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'No creo'},
    16:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Inevitable'},
    17:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Octavo dia'},
    18:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Que vuelvas'},
    19:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Tu'},
    20:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Donde estan los ladrones'},
    21:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Sombra de ti'},
    22:{'Artista': 'Shakira', 'Album': 'Donde estan los ladrones', 'Cancion': 'Ojos asi'},

    23:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Objection'},
    24:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Underneath your clothes'},
    25:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Whenever, Wherever'},
    26:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Rules'},
    27:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'The one'},
    28:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Ready for the good times'},
    29:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Fool'},
    30:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Te dejo Madrid'},
    31:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Poem to a Horse'},
    32:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Que me quedes tu'},
    33:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Eyes like yours'},
    34:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Suerte'},
    35:{'Artista': 'Shakira', 'Album': 'Laundry Service', 'Cancion': 'Te aviso, Te anuncio'},

    36:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'En tus pupilas'},
    37:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'La Pared'},
    38:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'La tortura'},
    39:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'Obtener un si'},
    40:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'Dia especial'},
    41:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'Escondite ingles'},
    42:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'No'},
    43:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'Las de la intuicion'},
    44:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'Dia de enero'},
    45:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'Lo imprescindible'},
    46:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'La pared'},
    47:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 1', 'Cancion': 'La tortura remix'},

    48:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'How do you do'},
    49:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Dont bother'},
    50:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Illegal'},
    51:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'The day and the time'},
    52:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Animal city'},
    53:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Dreams for plans'},
    54:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Hey you'},
    55:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Your embrace'},
    56:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Costumes makes the clown'},
    57:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Something'},
    58:{'Artista': 'Shakira', 'Album': 'Fijacion Oral vol 2', 'Cancion': 'Timor'},

    59:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'She wolf'},
    60:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Did it again'},
    61:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Long time'},
    62:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Why wait'},
    63:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Good stuff'},
    64:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Men in this town'},
    65:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Gypsy'},
    66:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Spy'},
    67:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Mon amour'},
    68:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Lo hecho esta hecho'},
    69:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Anios luz'},
    70:{'Artista': 'Shakira', 'Album': 'She wolf', 'Cancion': 'Loba'},

    71:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'El elias'},
    72:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Tanto'},
    73:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Miercoles'},
    74:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'En el vaticano'},
    75:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Sunny Blue'},
    76:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Buen dia'},
    77:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Sweater geek'},
    78:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Si supieras'},
    79:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'El gran McGee'},
    80:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Muneca'},
    81:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Gripa y mundial'},
    82:{'Artista': 'Pxndx', 'Album': 'Arroz con leche', 'Cancion': 'Te invito a mi fiesta'},

    83:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Christina'},
    84:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Claro que no '},
    85:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Hola'},
    86:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'El chango de los 2 platanos'},
    87:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Corazon de un cuento roto'},
    88:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Doble gracias'},
    89:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Quisiera no pensar'},
    90:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Ya no jalaba'},
    91:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Cortame con unas tijeras pero no se te olvide el resistol para volverme a pegar'},
    92:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Senor payaso'},
    93:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Ando pedo y ella esta aqui'},
    94:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Ilasha'},
    95:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Mala suerte'},
    96:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Amiguito'},
    97:{'Artista': 'Pxndx', 'Album': 'La revancha del principe charro', 'Cancion': 'Maracas'},

    98:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Reflexiones de una mente perturbada'},
    99:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Disculpa los malos pensamientos'},
    100:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Y de la gasolina renacio el amor'},
    101:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Cita en el quirofano'},
    102:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Ya no es suficiente lamentar'},
    103:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': '3+1'},
    104:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Mi huracan llevaba tu nombre'},
    105:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Promesas/Descepciones'},
    106:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Descanso: odiame'},
    107:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Cuando no es como debiera ser'},
    108:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Miedo a las alturas'},
    109:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Hasta el final'},
    110:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Figura decorativa sobre fondo ornamental'},
    111:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'No tienes oportunidad contra mi antipatica imaginacion'},
    112:{'Artista': 'Pxndx', 'Album': 'Para ti con desprecio', 'Cancion': 'Porque todavia podemos decir una vez mas'},

    113:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'La estrategia perdida'},
    114:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'So violento so macabro'},
    115:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'El infame estar y no estar'},
    116:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Estoy mas solo que ayer pero menos que manana'},
    117:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Narcisista por excelencia'},
    118:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Procedimientos para llegar a un comun acuerdo'},
    119:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Tripulacion, armar toboganes'},
    120:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Pathetica'},
    121:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Los malaventurados no lloran'},
    122:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Tus palabras punzocortantes'},
    123:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Atratctivo encontramos en lo mas repugnante'},
    124:{'Artista': 'Pxndx', 'Album': 'Amantes sunt amentes', 'Cancion': 'Ah pero como vendo cassettes'},

    125:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Popurri para ti'},
    126:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Fascinante'},
    127:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Conversacion casual'},
    128:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'El cuello perfecto'},
    129:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Espiritu pionero'},
    130:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Solo a terceros'},
    131:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Abigail'},
    132:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Casi nula autoestima'},
    133:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Del rapto y otros pormenores'},
    134:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Nuestra afliccion'},
    135:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Que tu cama sea mi hogar'},
    136:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Adheridos separados'},
    137:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Martirio de otro'},
    138:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Soy un ganador'},
    139:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Lascivamente'},
    140:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Un tipo de indulgencia'},
    141:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Amnistia'},
    142:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Agradable locura temporal'},
    143:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Espejismos y visiones'},
    144:{'Artista': 'Pxndx', 'Album': 'Poetics', 'Cancion': 'Quinta real'},

    145:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Papercut'},
    146:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'One step closer'},
    147:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'With you'},
    148:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Points of authority'},
    149:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Crawling'},
    150:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Runaway'},
    151:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'By myself'},
    152:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'In the end'},
    153:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'A place for my head'},
    156:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Forgotten'},
    157:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Cure for the itch'},
    158:{'Artista': 'Linkin Park', 'Album': 'Hybrid theory', 'Cancion': 'Pushing me away'},

    159:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Foreword'},
    160:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Dont stay'},
    161:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Somewhere i belong'},
    162:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Lying from you'},
    163:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Hit the floor'},
    164:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Easier to run'},
    165:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Faint'},
    166:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Figure.09'},
    167:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Breaking the habit'},
    168:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'From the inside'},
    169:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Nobody is listening'},
    170:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Session'},
    171:{'Artista': 'Linkin Park', 'Album': 'Meteora', 'Cancion': 'Numb'},

    172:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Wake'},
    173:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Given up'},
    174:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Leave out all the rest'},
    175:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Bleed it out'},
    176:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Shadow of the day'},
    177:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'What ive done'},
    178:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Hands held high'},
    179:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'No more sorrow'},
    180:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'Valentines day'},
    181:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'In between'},
    182:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'In pieces'},
    183:{'Artista': 'Linkin Park', 'Album': 'Minutes to midnight', 'Cancion': 'The little things give you away'},

    184:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'The requiem'},
    185:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'The radiance'},
    186:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Burning in the skies'},
    187:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Empty spaces'},
    188:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'When they come for me'},
    189:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Robot boy'},
    190:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Jornada del muerto'},
    191:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Waiting for the end'},
    192:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Blackout'},
    193:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Wretches and kings'},
    194:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Wisdomw, justice and love'},
    195:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Iridescent'},
    196:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Fallout'},
    197:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'The catalyst'},
    198:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'The messenger'},
    199:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'New divide'},
    200:{'Artista': 'Linkin Park', 'Album': 'A thousand suns', 'Cancion': 'Black birds'}
}



@app.get("/canciones")
async def imprimir():
    return (canciones)
    
@app.get("/canciones/Shakira")
async def imprimir():
    lista = {} #crea nuevo diccionario
    for key, value in canciones.items(): #recorre el diccionario original
        #for llave, valor in value.items(): recorre el valor del primer item
        if value['Artista']=='Shakira': 
            lista[key]=value    #agrega TODO el valor del primer item a la lista
    return(lista)

@app.get("/canciones/Shakira/pies-descalzos")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        if value["Artista"]=='Shakira':
            if value["Album"]=='Pies Descalzos':
                lista[key]=value
    return(lista)

@app.get("/canciones/Shakira/donde-estan-los-ladrones")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        if value["Artista"]=='Shakira':
            if value["Album"]=='Donde estan los ladrones':
                lista[key]=value
    return(lista)

@app.get("/canciones/Shakira/Laundry-service")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        if value["Artista"]=='Shakira':
            if value["Album"]=='Laundry Service':
                lista[key]=value
    return(lista)

@app.get("/canciones/Shakira/Fijacion-oral-vol-1")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        if value["Artista"]=='Shakira':
            if value["Album"]=='Fijacion Oral vol 1':
                lista[key]=value
    return(lista)

@app.get("/canciones/Shakira/Fijacion-oral-vol-2")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        if value["Artista"]=='Shakira':
            if value["Album"]=='Fijacion Oral vol 2':
                lista[key]=value
    return(lista)

@app.get("/canciones/Shakira/She-wolf")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        if value["Artista"]=='Shakira':
            if value["Album"]=='She wolf':
                lista[key]=value
    return(lista)

@app.get("/canciones/Pxndx")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                lista[key]=value
    return(lista)
    
@app.get("/canciones/Pxndx/Arroz-con-leche")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                if value["Album"]=='Arroz con leche':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Pxndx/La-revancha-del-principe-charro")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                if value["Album"]=='La revancha del principe charro':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Pxndx/Para-ti-con-desprecio")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                if value["Album"]=='Para ti con desprecio':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Pxndx/Amantes-sunt-amentes")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                if value["Album"]=='Amantes sunt amentes':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Pxndx/Poetics")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                if value["Album"]=='Poetics':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Linkin-Park")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Linkin Park':
                lista[key]=value
    return(lista)

@app.get("/canciones/Linkin-Park/Hybrid-theory")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Linkin Park':
                if value["Album"]=='Hybrid theory':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Linkin-Park/Meteora")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Linkin Park':
                if value["Album"]=='Meteora':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Linkin-Park/Minutes-to-midnight")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Linkin Park':
                if value["Album"]=='Minutes to midnight':
                    lista[key]=value
    return(lista)

@app.get("/canciones/Linkin-Park/A-thousand-suns")
async def imprimir():
    lista = {}
    for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Linkin Park':
                if value["Album"]=='A thousand suns':
                    lista[key]=value
    return(lista)

#forma alternativa que hice para agregar de manera manual (ineficaz)
"""                 lista[key]={llave: valor}
                lista[key]["Anio"]=value["Anio"]
                lista[key]["Album"]=value["Album"] """

# otra forma alternativa que hice recorriendo cada valor. En realidad puede buscar directamente el
# programa la key-value con mayor precision, quiero suponer
""" for key, value in canciones.items():
        for llave, valor in value.items():
            if valor=='Pxndx':
                lista[key]=value
    return(lista)
 """
#prueba para ver como se comportan los ciclos en diccionarios
"""                lista[key]["Artista"]=value["Artista"]
                lista[key]={llave: valor}
                lista[key]["Cancion"]=value["Cancion"]


  #              lista[key]={value[llave]: value[valor]}
 """


