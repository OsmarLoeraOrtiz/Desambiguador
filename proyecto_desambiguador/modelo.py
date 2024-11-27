import time
import google.generativeai as genai
import pandas as pd
import seaborn as sns
import time
import matplotlib.pyplot as plt
genai.configure(api_key="AIzaSyATWFJFyhguScg6T0M1CeBj8hlu6Qpg4EQ")

base_model = "models/gemini-1.5-flash-001-tuning"


training_data =[
{'text_input': 'RNF1\nTodas las bicicletas contar‼an con un freno electr‼onico en la parte delantera, un GPS incrustado y un\nn‼umero de bicicleta para identi\n                                carlas. Asimismo, las bicicletas contar‼an con un sistema de seguridad,\nya sea mediante un candado electr‼onico que bloquee las ruedas o mediante la activaci‼on de los frenos.\n8\nCibiUAM Informe de especi\n                         caci‼on de requisitos', 'output': '[\"Todas las bicicletas contarán con un freno electrónico en la parte delantera, un GPS incrustado y un número de bicicleta para identificarlas.\",\n\"Las bicicletas contarán con un sistema de seguridad, ya sea mediante un candado electrónico que bloquee las ruedas o mediante la activación de los frenos.\"]' }, 
{'text_input': 'caci‼on de requisitos\nRNF2\nTodas las estaciones contar‼an con una pantalla, un teclado y un lector de carnet de la UAM.\nRNF3\nEn total, habr‼a 240 bicicletas y 30 estaciones con 8 anclajes cada una.\nRNF4\nEl ‼ambito geogr‼a\n                  co del sistema abarcar‼a los campus de Cantoblanco y Medicina de la UAM.', 'output': '[\"Todas las estaciones contarán con una pantalla, un teclado y un lector de carnet de la UAM.\",\"En total, habrá 240 bicicletas y 30 estaciones con 8 anclajes cada una.\",\"El ámbito geográfico del sistema abarcará los campus de Cantoblanco y Medicina de la UAM.\"]' }, 
{'text_input': 'RNF5\nSe har‼a uso de la aplicaci‼on Google Maps para la ubicaci‼on geogr‼a\n                                                                     ca de usuarios, bicicletas y esta-\nciones.\nRNF6\nEl sistema debe validar que los usuarios que intentan identi\n                                                            carse pertenezcan a la UAM mediante el\nuso del servicio externo proporcionado por el cliente para dicho\n                                                                 n.\nOperacionales\nRNF7\nLos usuarios se autenticar‼an por medio del carnet universitario.\nRNF8\nLa fotograf‼►a que se permite adjuntar en el reporte de incidencias, seg‼un se describe en RF11, podr‼a\nser tomada en el momento o cargada desde la galer‼►a.', 'output': '[\"Se hará uso de la aplicación Google Maps para la ubicación geográfica de usuarios, bicicletas y estaciones.\",\"El sistema debe validar que los usuarios que intentan identificarse pertenezcan a la UAM mediante el uso del servicio externo proporcionado por el cliente para dicho fin.\",\"Los usuarios se autenticarán por medio del carnet universitario.\",\"La fotografía que se permite adjuntar en el reporte de incidencias, según se describe en RF11, podrá ser tomada en el momento o cargada desde la galería.\"]' }, 
{'text_input': 'Evita delimitadores   \"```json\"\n\n                      caci‼on de requisitos\nRNF2\nTodas las estaciones contar‼an con una pantalla, un teclado y un lector de carnet de la UAM.', 'output': '[\"Todas las estaciones contarán con una pantalla, un teclado y un lector de carnet de la UAM.\"]' }, 
{'text_input': 'RNF3\nEn total, habr‼a 240 bicicletas y 30 estaciones con 8 anclajes cada una.', 'output': '[\"En total, habrá 240 bicicletas y 30 estaciones con 8 anclajes cada una.\"]' }, 
{'text_input': 'evita los delimitadores\nRNF4\nEl ‼ambito geogr‼a\n                  co del sistema abarcar‼a los campus de Cantoblanco y Medicina de la UAM.\nRNF5\nSe har‼a uso de la aplicaci‼on Google Maps para la ubicaci‼on geogr‼a\n                                                                     ca de usuarios, bicicletas y esta-\nciones.\nRNF6\nEl sistema debe validar que los usuarios que intentan identi\n                                                            carse pertenezcan a la UAM mediante el\nuso del servicio externo proporcionado por el cliente para dicho\n                                                                 n.\nOperacionales', 'output': '[\"El ámbito geográfico del sistema abarcará los campus de Cantoblanco y Medicina de la UAM.\",\"Se hará uso de la aplicación Google Maps para la ubicación geográfica de usuarios, bicicletas y estaciones.\",\"El sistema debe validar que los usuarios que intentan identificarse pertenezcan a la UAM mediante el uso del servicio externo proporcionado por el cliente para dicho fin.\"]' }, 
{'text_input': 'RNF5\nSe har‼a uso de la aplicaci‼on Google Maps para la ubicaci‼on geogr‼a\n                                                                     ca de usuarios, bicicletas y esta-\nciones.', 'output': '[\"Se hará uso de la aplicación Google Maps para la ubicación geográfica de usuarios, bicicletas y estaciones.\"]' }, 
{'text_input': 'RNF6\nEl sistema debe validar que los usuarios que intentan identi\n                                                            carse pertenezcan a la UAM mediante el\nuso del servicio externo proporcionado por el cliente para dicho\n                                                                 n.\nOperacionales', 'output': '[\"El sistema debe validar que los usuarios que intentan identificarse pertenezcan a la UAM mediante el uso del servicio externo proporcionado por el cliente para dicho fin.\"]' }, 
{'text_input': 'RNF11\nLa informaci‼on de los usuarios recogida por el sistema ser‼a encriptada utilizando el m‼etodo RSA para\ngarantizar su privacidad.', 'output': '[\"La información de los usuarios recogida por el sistema ser‼a encriptada utilizando el método RSA para\ngarantizar su privacidad.\"]' }, 
{'text_input': 'RNF8\nLa fotograf‼►a que se permite adjuntar en el reporte de incidencias, seg‼un se describe en RF11, podr‼a\nser tomada en el momento o cargada desde la galer‼►a.', 'output': '[\"La fotografía que se permite adjuntar en el reporte de incidencias, según se describe en RF11, podrá ser tomada en el momento o cargada desde la galería.\"]' }, 
{'text_input': 'RNF9\nPara realizar una reserva, ser‼a necesario rellenar un formulario indicando fecha, hora y lugar de\nrecogida. De forma opcional y a cambio de una boni\n                                                  caci‼on (RF29), el usuario podr‼a indicar hora y\nlugar de devoluci‼on de la bicicleta.', 'output': '[\"Para realizar una reserva, será necesario rellenar un formulario indicando fecha, hora y lugar de recogida. De forma opcional y a cambio de una bonificación (RF29), el usuario podrá indicar hora y lugar de devolución de la bicicleta.\"]' }, 
{'text_input': 'RNF10\nElsistema noti\n              car‼aal usuariotras realizaruna reserva. La noti\n                                                              caci‼oncontendr‼aun c‼odigode reserva\ny los datos de la misma, introducidos en el formulario descrito en RNF9.', 'output': '[\"El sistema notificará al usuario tras realizar una reserva. La notificación contendrá un código de reserva y los datos de la misma, introducidos en el formulario descrito en RNF9.\"]' }, 
{'text_input': 'RNF12\nSe utilizar‼a el protocolo HTTPS para el intercambio de informaci‼on en la red.', 'output': '[\"Se utilizará el protocolo HTTPS para el intercambio de información en la red.\"]' }, 
{'text_input': 'RNF12\nSe utilizar‼a el protocolo HTTPS para el intercambio de informaci‼on en la red.\nRNF13\nEl sistema no permitir‼a recordar contrase~nas de usuarios. Estas ‼unicamente estar‼an almacenadas en\nla base de datos, no en los sistemas de las estaciones.\nLegales', 'output': '[\"Se utilizará el protocolo HTTPS para el intercambio de información en la red.\",\n\"El sistema no permitirá recordar contraseñas de usuarios. Estas únicamente estarán almacenadas en la base de datos, no en los sistemas de las estaciones.\"]' }, 
{'text_input': 'RNF14\nLa informaci‼on de los usuarios recogida por la aplicaci‼on ser‼a tratada conforme a la Ley Org‼anica de\nProtecci‼on de Datos.\nInterfaz', 'output': '[\"La información de los usuarios recogida por la aplicación será tratada conforme a la Ley Orgánica de Protección de Datos.\"]' }, 
{'text_input': 'RNF13\nEl sistema no permitir‼a recordar contrase~nas de usuarios. Estas ‼unicamente estar‼an almacenadas en\nla base de datos, no en los sistemas de las estaciones.\nLegales', 'output': '[\"El sistema no permitirá recordar contraseñas de usuarios. Estas únicamente estarán almacenadas en la base de datos, no en los sistemas de las estaciones.\"]' }, 
{'text_input': 'RNF15\nLa aplicaci‼on seguir‼a un dise~no\nresponsive\n, permitiendo adaptarse a distintos tama~nos de pantalla.', 'output': '[\"La aplicación seguirá un diseño responsive, permitiendo adaptarse a distintos tamaños de pantalla.\"]' }, 
{'text_input': 'RNF18\nLa aplicaci‼on podr‼a utilizarse en castellano e ingl‼es, debido a que ser‼a utilizada por un p‼ublico\ninternacional.', 'output': '[\"La aplicación podrá utilizarse en castellano e inglés, debido a que será utilizada por un público internacional.\"]' }, 
{'text_input': 'Las noti\n        caciones del sistema llegar‼an tanto a la bandeja de entrada de la cuenta del usuario en el\nsistema como a la aplicaci‼on m‼ovil.', 'output': '[\"Las notificaciones del sistema llegarán tanto a la bandeja de entrada de la cuenta del usuario en el sistema como a la aplicación móvil.\"]' }, 
{'text_input': 'La informaci‼on de disponibilidad para realizar una reserva se podr‼a mostrar tanto de forma textual\ncomo en un mapa.', 'output': '[\"La información de disponibilidad para realizar una reserva se podrá mostrar tanto de forma textual como en un mapa.\"]' }, 
{'text_input': 'RF43\nLas estaciones contar‼an, en total, con tantos anclajes disponibles como bicicletas haya en el\nsistema. En el caso de que alg‼un anclaje sufra una aver‼►a, se deber‼an retirar temporalmente\ntantas bicicletas como sea necesario para equilibrarlo.\nRF44\nEl sistema ofrecer‼a un \\\nmodo parada\n\", que permitir‼a que el usuario deje la bicicleta bloqueada\nen cualquier lugar y que nadie pueda retirarla. El precio que se cobra por minuto en este modo\nse reduce a la mitad.', 'output': '[\"Las estaciones contarán, en total, con tantos anclajes disponibles como bicicletas haya en el sistema. En el caso de que algún anclaje sufra una avería, se deberán retirar temporalmente tantas bicicletas como sea necesario para equilibrarlo.\", \"El sistema ofrecerá un \\\"modo parada\\\", que permitirá que el usuario deje la bicicleta bloqueada en cualquier lugar y que nadie pueda retirarla. El precio que se cobra por minuto en este modo se reduce a la mitad.\"]' }, 
{'text_input': 'RIE-IS-4. El sistema se comunicará con el banco con el que SELAE paga sus premios mayores.\nRIE-IS-5. El sistema se deberá comunicar con el sistema de los puntos de venta físicos.\nRIE-IS-6. El sistema se deberá comunicar con la base de datos de la Dirección General de\nOrdenación del Juego.', 'output': '[\"El sistema se comunicará con el banco con el que SELAE paga sus premios mayores.\", \"El sistema se deberá comunicar con el sistema de los puntos de venta físicos.\", \"El sistema se deberá comunicar con la base de datos de la Dirección General de Ordenación del Juego.\"]' }, 
{'text_input': 'RF-MNDR-1. El sistema permitirá al usuario identificado jugador cargar su monedero\nelectrónico.\nRF-MNDR-1.1. El sistema permitirá elegir el medio de pago. Los medios de pago disponibles\nson:\nRF-MNDR-1.1.1. Tarjeta de crédito/débito.\nRF-MNDR-1.1.2. Traspaso rápido (mediante transferencia bancaria).', 'output': '[\"El sistema permitirá al usuario identificado jugador cargar su monedero electrónico.\", \"El sistema permitirá elegir el medio de pago. Los medios de pago disponibles son: Tarjeta de crédito/débito, Traspaso rápido (mediante transferencia bancaria).\"]' }, 
{'text_input': 'RF-MNDR-1.2. El sistema proporcionará una opción de ayuda al usuario por cada medio de\npago.\nRF-MNDR-1.3. El sistema permitirá seleccionar la cantidad de dinero que el usuario quiera\ncargar.\nRF-MNDR-1.3.1. El sistema comprobará que la cantidad seleccionada sea superior a\nCANTIDAD_MINIMA_CARGA_MONEDERO.\nRF-MNDR-1.3.1.1.1. El valor por defecto de CANTIDAD_MINIMA_CARGA_MONEDERO\nes de 1€.\nRF-MNDR-1.3.1.1.2. CANTIDAD_MINIMA_CARGA_MONEDERO debe poder ser\nconfigurado por el administrador del sistema.\nRF-MNDR-1.3.1.1.2.1. El sistema verificará que el valor de\nCANTIDAD_MINIMA_CARGA_MONEDERO sea mayor de 0.\nRF-MNDR-1.3.2. El sistema comprobará que la cantidad no sobrepase los límites de carga:\nRF-MNDR-1.3.2.1. Límite de carga diario (ver RF-MNDR-2.6.1).\nRF-MNDR-1.3.2.2. Límite de carga semanal (ver RF-MNDR-2.6.2).\nRF-MNDR-1.3.2.3. Límite de carga mensual (ver RF-MNDR-2.6.3).', 'output': '[\"El sistema proporcionará una opción de ayuda al usuario por cada medio de pago.\", \"El sistema permitirá seleccionar la cantidad de dinero que el usuario quiera cargar.\", \"El sistema comprobará que la cantidad seleccionada sea superior a CANTIDAD_MINIMA_CARGA_MONEDERO. El valor por defecto de CANTIDAD_MINIMA_CARGA_MONEDERO es de 1€. CANTIDAD_MINIMA_CARGA_MONEDERO debe poder ser configurado por el administrador del sistema. El sistema verificará que el valor de CANTIDAD_MINIMA_CARGA_MONEDERO sea mayor de 0.\", \"El sistema comprobará que la cantidad no sobrepase los límites de carga: Límite de carga diario (ver RF-MNDR-2.6.1), Límite de carga semanal (ver RF-MNDR-2.6.2), Límite de carga mensual (ver RF-MNDR-2.6.3).\"]' }, 
{'text_input': 'RF-MNDR-1.4. El sistema mostrará la siguiente información antes de acceder al medio de\npago:\nRF-MNDR-1.4.1. La cantidad que se va a cargar.\nRF-MNDR-1.4.2. La cantidad ya presente en el monedero electrónico.\nRF-MNDR-1.4.3. La suma total de ambas cantidades', 'output': '[\"El sistema mostrará la siguiente información antes de acceder al medio de pago: la cantidad que se va a cargar,  la cantidad ya presente en el monedero electrónico y la suma total de ambas cantidades\"]' }, 
{'text_input': 'RF-MNDR-1.2. El sistema proporcionará una opción de ayuda al usuario por cada medio de\npago.', 'output': '[\"El sistema proporcionará una opción de ayuda al usuario por cada medio de pago.\"]' }, 
{'text_input': 'RF-MNDR-1.5. En caso de pago con tarjeta de crédito/débito.\nRF-MNDR-1.5.1. El sistema utilizará la pasarela de pago Redsys, que solicitará al jugador\nlos siguientes datos de forma obligatoria:\nRF-MNDR-1.5.1.1. El número de tarjeta.\nRF-MNDR-1.5.1.2. La fecha de caducidad.\nRF-MNDR-1.5.1.3. El CVV.\nRF-MNDR-1.5.2. El sistema proporcionará la opción de utilizar los datos de una tarjeta\nintroducidos en una carga anterior.', 'output': '[\"En caso de pago con tarjeta de crédito/débito, el sistema utilizará la pasarela de pago Redsys, que solicitará al jugador los siguientes datos de forma obligatoria: el número de tarjeta, la fecha de caducidad y el CVV.\", \"El sistema proporcionará la opción de utilizar los datos de una tarjeta introducidos en una carga anterior.\"]' }, 
{'text_input': 'RF-MNDR-1.6. En caso de pago con traspaso rápido:\nRF-MNDR-1.6.1. El sistema mostrará los bancos disponibles a través de los que pagar\nRF-MNDR-1.6.2. El sistema mostrará la cantidad mínima a cargar en cada uno.\nRF-MNDR-1.6.3. El sistema redirigirá a la banca personal de la entidad bancaria\nseleccionada, donde el jugador podrá introducir sus credenciales y confirmar el pago', 'output': '[\"En caso de pago con traspaso rápido: el sistema mostrará los bancos disponibles a través de los que pagar, el sistema mostrará la cantidad mínima a cargar en cada uno y el sistema redirigirá a la banca personal de la entidad bancaria seleccionada, donde el jugador podrá introducir sus credenciales y confirmar el pago\"]' }, 
{'text_input': 'El sistema deberá permitir el registro de una nueva cita indicando el día, hora, y profesional que la atenderá.', 'output': '[\"El sistema deberá permitir el registro de una nueva cita indicando el día, hora, y profesional que la atenderá.\"]' }, 
{'text_input': 'Los gestores del sistema podr‼an\neliminar o a~nadir\ntanto estaciones como bicicletas al sistema, ya\nsea temporalmente (a causa de alguna incidencia) o permanentemente.\nRF42\nLos gestores del sistema podr‼an actualizar la informaci‼on relativa a los\nprecios\nen cualquier\nmomento.\n\nCaracter\n‼\n►sticas del sistema', 'output': '[\"Los gestores del sistema podrán eliminar o añadir tanto estaciones como bicicletas al sistema, ya sea temporalmente (a causa de alguna incidencia) o permanentemente.\", \"Los gestores del sistema podrán actualizar la información relativa a los precios en cualquier momento.\"]' }, 
{'text_input': 'Los gestores del sistema dispondr‼an de\ninformaci‼on adicional\nen tiempo real del sistema para\nconocer el estado del mismo en cuanto a posibles incidencias, por ejemplo si existen bicicletas\naveriadas o si hay alguna estaci‼on sin anclajes libres.', 'output': '[\"Los gestores del sistema dispondrán de información adicional en tiempo real del sistema para conocer el estado del mismo en cuanto a posibles incidencias, por ejemplo si existen bicicletas averiadas o si hay alguna estación sin anclajes libres.\"]' }, 
{'text_input': 'Cualquier usuario podr‼a\nconsultar las tarifas\ndel servicio. Asimismo, podr‼a consultar una\nesti-\nmaci‼on del precio\nque costar‼a realizar un trayecto determinado.\nRF39\nEl sistema ofrecer‼a la posibilidad de\nprobar de forma gratuita\nel servicio durante 30 minutos.\n\nGestores del sistema', 'output': '[\"Cualquier usuario podrá consultar las tarifas del servicio. Asimismo, podrá consultar una estimación del precio que costaría realizar un trayecto determinado.\", \"El sistema ofrecerá la posibilidad de probar de forma gratuita el servicio durante 30 minutos.\"]' }, 
{'text_input': 'Los usuarios podr‼an alquilar\nmaterial adicional\nen las propias estaciones de reserva, como cascos,\nlinterna, cestas para bicicleta y sill‼►n para ni~nos.', 'output': '[\"Los usuarios podrán alquilar material adicional en las propias estaciones de reserva, como cascos, linterna, cestas para bicicleta y sillín para niños.\"]' }, 
{'text_input': 'Los usuarios podr‼an\nincorporar su propia bicicleta\nal sistema durante el tiempo que deseen. A\ncambio, recibir‼an un c‼odigo de uso ilimitado del material del servicio vigente durante el tiempo\nque su bicicleta permanezca en el mismo. Para ello deber‼an acudir a la o\n                                                                         cina central del servicio\ndel campus de Cantoblanco.', 'output': '[\"Los usuarios podrán incorporar su propia bicicleta al sistema durante el tiempo que deseen. A cambio, recibirán un código de uso ilimitado del material del servicio vigente durante el tiempo que su bicicleta permanezca en el mismo. Para ello deberán acudir a la oficina central del servicio del campus de Cantoblanco.\"]' }, 
{'text_input': 'Los usuarios registrados podr‼an\nconsultar el estado del servicio\n(como la disponibilidad de bici-\ncletas en una estaci‼on o la hora prevista de devoluci‼on de bicicletas en alguna estaci‼on) en todo\nmomento a trav‼es de la aplicaci‼on m‼ovil o de las pantallas instaladas en las estaciones repartidas\npor el campus.\n7\nCibiUAM Informe de especi\n                         caci‼on de requisitos', 'output': '[\"Los usuarios registrados podrán consultar el estado del servicio (como la disponibilidad de bicicletas en una estación o la hora prevista de devolución de bicicletas en alguna estación) en todo momento a través de la aplicación móvil o de las pantallas instaladas en las estaciones repartidas por el campus.\"]' }, 
{'text_input': 'Los usuarios deber☼an poder\nregistrarse en el sistema proporcionando\ninformaci◄n b★sica como:\nnombre, correo electr►nico y contrase¤a.', 'output': '[\"Los usuarios deberán poder registrarse en el sistema proporcionando información básica como: nombre, correo electrónico y contraseña.\"]' }, 
{'text_input': 'El sistema permitir☼a a los usuarios\nconsultar su hist●rial de\nactividades y movimientos realizados en los ♣ltimos 6 meses.\nAdministraci◄n de Recursos', 'output': '[\"El sistema permitirá a los usuarios consultar su historial de actividades y movimientos realizados en los últimos 6 meses.\"]' }, 
{'text_input': 'Los administradores tendr☼an acceso al\npanel de control para gestionar los\nrecursos del sistema en tiempo ℜeal.', 'output': '[\"Los administradores tendrán acceso al panel de control para gestionar los recursos del sistema en tiempo real.\"]' }, 
{'text_input': 'El sistema deber☼a mantener un\nregistro detallado de todas las\ntransac¢iones y operaciones realizadas por\ncada usuario del sistema.\nGesti♠n de Incidencias', 'output': '[\"El sistema deberá mantener un registro detallado de todas las transacciones y operaciones realizadas por cada usuario del sistema.\"]' }, 
{'text_input': 'Los usuarios podr☼an reportar\nincidencias o problemas t↕cnicos\na trav♣s de un formulario\nespec☼fico.', 'output': '[\"Los usuarios podrán reportar incidencias o problemas técnicos a través de un formulario específico.\"]' }, 
{'text_input': 'El sistema notificar☼a autom★ticamente\na los administradores cuando se\ndetecten anomal☼as en el\nfuncionamiento del servicio.\nCaracter◄sticas T♣cnicas', 'output': '[\"El sistema notificará automáticamente a los administradores cuando se detecten anomalías en el funcionamiento del servicio.\"]' }, 
{'text_input': 'El sistema deber☼a ser capaz de\nprocesar al menos 1000 peticiones\nsimult★neas sin degradar su\nrendimiento.', 'output': '[\"El sistema debería ser capaz de procesar al menos 1000 peticiones simultáneas sin degradar su rendimiento.\"]' }, 
{'text_input': 'La plataforma deber☼a garantizar\nun tiempo de respuesta inferior a\n3 segundos en condiciones normales\nde operaci♠n.', 'output': '[\"La plataforma deberá garantizar un tiempo de respuesta inferior a 3 segundos en condiciones normales de operación.\"]' }, 
{'text_input': 'Esto simula problemas comunes de codificación donde los caracteres especiales del español (ñ, á, é, í, ó, ú) se muestran incorrectamente reemplazados por símbolos.', 'output': '[]' }, 
{'text_input': 'Introducci◄n\nEsta gu☼a est★ dise¤ada para ayudar en la\nconfiguraci♠n b★sica de dispositivos\nde red. Por favor, lea atentamente las\ninstrucciones antes de comenzar.', 'output': '[]' }, 
{'text_input': 'Introducci◄n\nEsta gu☼a est★ dise¤ada para ayudar en la\nconfiguraci♠n b★sica de dispositivos\nde red. Por favor, lea atentamente las\ninstrucciones antes de comenzar.\nConsideraciones Prev↕as\nAntes de iniciar la configuraci◄n,\naseg♣rese de tener todos los elementos\nnecesarios:\n\n\nCable de alimentaci♠n\nCable de red\nDestornillador peque¤o\nManual del fabricante\nRF28\nEl sistema notificar☼a autom★ticamente\na los administradores cuando se\ndetecten anomal☼as en el\nfuncionamiento del servicio.\nCaracter◄sticas T♣cnicas\nRF29\nEl sistema deber☼a ser capaz de\nprocesar al menos 1000 peticiones\nsimult★neas sin degradar su\nrendimiento.', 'output': '[ \"El sistema notificará automáticamente a los administradores cuando se detecten anomalías en el funcionamiento del servicio.\", \"El sistema debería ser capaz de procesar al menos 1000 peticiones simultáneas sin degradar su rendimiento.\"]' }, 
{'text_input': 'Precauciones de Seguridad\n☼ No manipule los equipos con las manos h♣medas\n☼ Evite la exposici♠n directa al sol\n☼ Mantenga una ventilaci◄n adecuada\nRF26\nEl sistema deber☼a mantener un\nregistro detallado de todas las\ntransac¢iones y operaciones realizadas por\ncada usuario del sistema.\nGesti♠n de Incidencias\nRF27\nLos usuarios podr☼an reportar\nincidencias o problemas t↕cnicos\na trav♣s de un formulario\nespec☼fico.', 'output': '[\"El sistema deberá mantener un registro detallado de todas las transacciones y operaciones realizadas por cada usuario del sistema.\",\n\"Los usuarios podrán reportar incidencias o problemas técnicos a través de un formulario específico.\"]' }, 
{'text_input': 'Garant☼a y Soporte\nPer☼odo de garant☼a: 12 meses\nServicio t↕cnico disponible 24/7\nTel►fono de contacto: (XX) XXXX-XXXX\nCorreo de soporte: soporte@ejemplo.com\nRF23\nLos usuarios deber☼an poder\nregistrarse en el sistema proporcionando\ninformaci◄n b★sica como:\nnombre, correo electr►nico y contrase¤a.\nRF24\nEl sistema permitir☼a a los usuarios\nconsultar su hist●rial de\nactividades y movimientos realizados en los ♣ltimos 6 meses.\nAdministraci◄n de Recursos\n\nMantenimiento B★sico\n\n\nLimpieza peri♠dica\nActualizaci♠n de firmware\nRevisi◄n de conexiones\nVerificaci♠n de temperatura', 'output': '[\"Los usuarios deberán poder registrarse en el sistema proporcionando información básica como: nombre, correo electrónico y contraseña.\", \"El sistema permitirá a los usuarios consultar su historial de actividades y movimientos realizados en los últimos 6 meses.\"]' }, 
{'text_input': 'Aquí tienes un texto con requisitos de software con caracteres especiales mal codificados en español:', 'output': '[]' }, 
{'text_input': 'Te daré un texto con problemas de codificación similar a documentos mal convertidos:\nManual de Configuraci♠n de Red\n\nIntroducci◄n\nEsta gu☼a est★ dise¤ada para ayudar en la\nconfiguraci♠n b★sica de dispositivos\nde red. Por favor, lea atentamente las\ninstrucciones antes de comenzar.\nConsideraciones Prev↕as\nAntes de iniciar la configuraci◄n,\naseg♣rese de tener todos los elementos\nnecesarios:\n\n\nCable de alimentaci♠n\nCable de red\nDestornillador peque¤o\nManual del fabricante\n\n\nPrecauciones de Seguridad\n☼ No manipule los equipos con las manos h♣medas\n☼ Evite la exposici♠n directa al sol\n☼ Mantenga una ventilaci◄n adecuada\nEspecificaciones T↕cnicas\nTemperatura de operaci♠n: 5° a 35° C\nHumedad m★xima: 80%\nAltitud m★xima de operaci◄n: 2000 m\nTensi♠n de entrada: 220V/50Hz\nResoluci♠n de Problemas Com♣nes\n→ El equipo no enciende\n→ La luz de conexi♠n parpadea\n→ No hay se¤al de red\n→ El ventilador hace ruido excesivo\nMantenimiento B★sico\n\n\nLimpieza peri♠dica\nActualizaci♠n de firmware\nRevisi◄n de conexiones\nVerificaci♠n de temperatura\n\n\nGarant☼a y Soporte\nPer☼odo de garant☼a: 12 meses\nServicio t↕cnico disponible 24/7\nTel►fono de contacto: (XX) XXXX-XXXX\nCorreo de soporte: soporte@ejemplo.com', 'output': '[]' }, 
{'text_input': 'RF35: El sistema deber☼a permitir\nla gesti♠n de usuarios y sus\nperfiles de acceso.\nReceta de Bizcocho Casero\nIngredientes:\n\n3 huevos a temperatura ambiente\n250g de az♣car\n250g de harina', 'output': '[\"El sistema debería permitir la gestión de usuarios y sus perfiles de acceso.\"]' }, 
{'text_input': 'RF36: Los usuarios podr★n generar\nreportes estad☼sticos de las\n♣ltimas transacciones realizadas.\nCu★ndo Regar las Plantas\nLas mejores horas para el riego son:\n\nTemprano por la ma¤ana\nAl atardecer\nEvite regar en las horas de m★s calor.', 'output': '[\"Los usuarios podrán generar reportes estadísticos de las últimas transacciones realizadas.\"]' }, 
{'text_input': 'RF37: El sistema realizar☼a copias\nde seguridad autom★ticas cada\n24 horas.\nConsejos para Viajar en Avi♠n\n\nLlegar con 3 horas de anticipaci◄n\nDocumentar el equipaje adecuadamente\nLlevar un su►ter por si hace fr☼o', 'output': '[\"El sistema realizará copias de seguridad automáticas cada 24 horas.\"]' }, 
{'text_input': 'RF38: La plataforma deber☼a\nmantener un registro detallado de\ntodas las modificaciones realizadas\nen la base de datos.\nMantenimiento de Jard☼n\n→ Podar los arbustos mensualmente\n→ Fertilizar cada 3 meses\n→ Revisar el sistema de riego', 'output': '[\"La plataforma debería mantener un registro detallado de todas las modificaciones realizadas en la base de datos.\"]' }, 
{'text_input': 'RF39: Los administradores podr★n\nconfigurar diferentes niveles de\nacceso para cada tipo de usuario.\nReceta de T► de Hierbas\n\nHervir agua en una olla peque¤a\nA¤adir hojas de menta y manzanilla\nDejar reposar por 5 minutos', 'output': '[\"Los administradores podrán configurar diferentes niveles de acceso para cada tipo de usuario.\"]' }, 
{'text_input': 'RF40: El sistema enviar☼a\nnotificaciones autom★ticas cuando\nse detecten accesos no autorizados.\nConsejos para Dormir Mejor\n\nMantener una temperatura agradable\nEvitar pantallas antes de dormir\nEstablecer una rutina nocturna b★sica', 'output': '[\"El sistema enviará notificaciones automáticas cuando se detecten accesos no autorizados.\"]' }, 
{'text_input': 'RF41: La aplicaci♠n deber☼a\nser compatible con diferentes\nnavegadores web y dispositivos\nm♠viles.\nCuidado de Mascotas\n☼ Pasear al perro 3 veces al d☼a\n☼ Cambiar el agua diariamente\n☼ Cepillar el pelaje semanalmente', 'output': '[\"La aplicación debería ser compatible con diferentes navegadores web y dispositivos móviles.\"]' }, 
{'text_input': 'RF47: Los administradores deber☼an\ntener acceso a una ventana especial\nque permita:\n\nVer estado de estaciones\nVer estado de bicicletas\nGestionar incidencias', 'output': '[\"Los administradores deberían tener acceso a una ventana especial que permita: ver estado de estaciones, ver estado de bicicletas y gestionar incidencias\"]' }, 
{'text_input': 'RF48: Los usuarios deber☼an poder\nrealizar todas las gestiones desde\ncualquiera de las dos versiones:Reservar bicicletasAdministrar cuentaAdquirir bonosComo puedes ver, el texto original contiene requisitos funcionales importantes del sistema pero estaban redactados de forma narrativa. Los he reformateado siguiendo una estructura más formal de requisitos de software, manteniendo los caracteres especiales mal codificados (☼, ♠, etc.) como en los ejemplos anteriores.', 'output': '[\"Los usuarios deberían poder realizar todas las gestiones desde cualquiera de las dos versiones: Reservar bicicletas, Administrar cuenta y Adquirir bonos.\"]' }, 
{'text_input': '1.2 Ámbito\nActualmente el juego de la Lotería Primitiva solamente permite la realización de apuestas en\nlos puntos de venta físicos autorizados por SELAE y de forma presencial. El objetivo del\nsistema a desarrollar (denominado IRBet) es ampliar el sistema actual, haciendo posible la\nrealización de apuestas vía online y la automatización de parte de la gestión de los sorteos', 'output': '[]' }, 
{'text_input': 'Apuesta: Representa una sola apuesta múltiple o varias apuestas sencillas (como\nmáximo 8) realizadas de una vez. No se pueden realizar apuestas múltiples y sencillas\nen una misma apuesta.\n• Apuesta múltiple: Pronóstico consistente en seleccionar 7, 8, 5, 9, 10 o 11 números\nen un bloque. Equivale a realizar varias apuestas sencillas.\n• Apuesta sencilla: Pronóstico consistente en seleccionar 6 números en un bloque.\n• Autoexclusión: Un usuario registrado puede solicitar voluntariamente que se le\nexcluya de IRBet durante un periodo de tiempo de 1, 3, 6 meses o permanentemente.\nImplica que el usuario no podrá jugar, iniciar sesión ni cargar o descargar fondos de su\ncuenta de usuario.\n• Bloque: Conjunto de números del 1 al 49 (ambos inclusive, y sin repetir).\n• BD: Base de datos.\n• DGOJ: Dirección General de Ordenación del Juego. Es el órgano del Ministerio de\nHacienda y Función Pública que, bajo la dependencia de la Secretaría de Estado de\nHacienda, ejerce las funciones de regulación, autorización, supervisión y, en su caso,\nsanción de las actividades de juego de ámbito estatal.\n• Escrutinio: Proceso para examinar los boletos de un juego de apuestas para establecer\nlos ganadores en las diferentes categorías.\n• Hosting: Servicio que provee a los usuarios de Internet un sistema para poder\nalmacenar información, imágenes, vídeo, o cualquier contenido accesible vía web.\n• Internacionalización: Disposición de varias versiones de un mismo contenido en\ndiferentes idiomas o formatos.\n• Joker: Juego opcional asociado a la Lotería Primitiva. Si el usuario decide participar, a\nsu resguardo se le asocia aleatoriamente un número de siete cifras entre el 0.000.000\ny 9.999.999, ambos inclusive. Obtienen premio aquellos resguardos en los que el\nnúmero asignado de forma automática coincida, en todo o en parte, con el extraído\nen el sorteo.\n• Junta Superior de control: es el órgano formado por personal de SELAE encargado de\ngarantizar que todas las normas de los juegos se cumplan y asegurar la transparencia\nde los sorteos.\n• Métrica V3: Metodología de planificación, desarrollo y mantenimiento de sistemas de\ninformación propuesto por el Ministerio de Hacienda y Función Pública.\n• Protocolo HTTPS: HTTPS (protocolo de Transferencia de Hiper-Texto) es un protocolo\nque permite establecer una conexión segura entre el servidor y el cliente, que no\npuede ser interceptada por personas no autorizadas.\n• Resguardo: Comprobante que se emite al usuario una vez efectuado el pago de una\napuesta.\n• SELAE: Sociedad Estatal Loterías y Apuestas del Estado. Empresa pública a la que\ncorresponde la gestión exclusiva de los juegos de titularidad estatal.\n• Streaming: Distribución digital de contenido multimedia a través de una red de\ncomputadoras, de manera que el usuario utiliza el producto a la vez que se descarga.\n• WCAG: Las Pautas de Accesibilidad para el Contenido Web (WCAG - traducción al\ncastellano de Web Content Accessibility Guidelines) son recomendaciones que\npersiguen aumentar la accesibilidad de las páginas web.\n• W3C: World Wide Web Consortium es un consorcio internacional que genera\nrecomendaciones y estándares que aseg', 'output': '[]' }, 
{'text_input': 'En el siguiente apartado se hace una descripción general de IRBet. Se describen las relaciones\nde IRBet con otros sistemas, las funciones principales del producto, las características de los\nusuarios y restricciones generales que afectan al sistema.\nEn el apartado 3 se detallan todos los requisitos que debe cumplir IRBet.\nEn el apéndice A se incluyen los diagramas UML utilizados en la obtención de los requisitos:\ndiagrama de contexto, diagramas de casos de uso (de gestionar el monedero, jugar a la Lotería\nPrimitiva y gestionar sorteos de la Lotería Primitiva) y diagramas de estados (del perfil de un\nusuario registrado y de una apuesta).\nEn el apéndice B se incluyen escenarios que aclaran algunos de lo', 'output': '[]' }, 
{'text_input': 'RF59: Los usuarios podr★n\nconfigurar sus preferencias\nde notificaci♠n por canal.\nConsejos para Plantas de Interior\n→ Evitar luz solar directa\n→ Regar cuando la tierra est► seca\n→ Fertilizar cada 3 meses', 'output': '[\"Los usuarios podrán configurar sus preferencias de notificación por canal.\"]' }, 
{'text_input': 'PS45: El pastel deber☼a hornearse\na 180 grados durante 45 minutos,\nmanteniendo la temperatura estable.', 'output': '[]' }, 
{'text_input': 'MT67: El motor deber☼a recibir\nmantenimiento cada 10,000 km o\ncuando se detecten ruidos an♠malos.', 'output': '[]' }, 
{'text_input': 'JD23: Las plantas deber★n recibir\nluz indirecta durante al menos\n6 horas al d☼a.', 'output': '[]' }, 
{'text_input': 'CP89: El deportista deber☼a\nrealizar estiramientos antes y\ndespu►s de cada entrenamiento.\nMK45: La masa deber☼a reposar\nen un lugar templado durante\n2 horas antes de su manipulaci♠n.\nGT12: El gato deber★ recibir\nsus vacunas anuales y revisiones\nveterinarias trimestrales.', 'output': '[]' }, 
{'text_input': 'HG78: La habitaci♠n deber☼a\nmantener una temperatura entre\n18 y 22 grados para un sue¤o\n♠ptimo.\nBK34: El beb► deber☼a recibir\nalimentaci♠n cada 3-4 horas\ndurante sus primeros meses.\nVH90: El veh☼culo deber★\nsometerse a una revisi♠n\ncompleta antes de realizar\nviajes largos.\nFT56: Las flores deber☼an\nregarse temprano en la ma¤ana\no al atardecer, nunca en horas\nde calor intenso.', 'output': '[]' }, 
{'text_input': 'PS45: El pastel deber☼a hornearse\na 180 grados durante 45 minutos,\nmanteniendo la temperatura estable.\nMT67: El motor deber☼a recibir\nmantenimiento cada 10,000 km o\ncuando se detecten ruidos an♠malos.\nJD23: Las plantas deber★n recibir\nluz indirecta durante al menos\n6 horas al d☼a.\nCP89: El deportista deber☼a\nrealizar estiramientos antes y\ndespu►s de cada entrenamiento.\nMK45: La masa deber☼a reposar\nen un lugar templado durante\n2 horas antes de su manipulaci♠n.\nGT12: El gato deber★ recibir\nsus vacunas anuales y revisiones\nveterinarias trimestrales.\nHG78: La habitaci♠n deber☼a\nmantener una temperatura entre\n18 y 22 grados para un sue¤o\n♠ptimo.\nBK34: El beb► deber☼a recibir\nalimentaci♠n cada 3-4 horas\ndurante sus primeros meses.\nVH90: El veh☼culo deber★\nsometerse a una revisi♠n\ncompleta antes de realizar\nviajes largos.\nFT56: Las flores deber☼an\nregarse temprano en la ma¤ana\no al atardecer, nunca en horas\nde calor intenso.', 'output': '[]' }, 
{'text_input': 'RF58: La aplicaci♠n deber☼a\ncifrar todos los datos sensibles\nusando AES-256.\nMantenimiento de Bicicleta\n\nLubricar la cadena\nRevisar frenos\nAjustar cambios\nComprobar presi♠n\n\nRF59: Los usuarios podr★n\nconfigurar sus preferencias\nde notificaci♠n por canal.\nConsejos para Plantas de Interior\n→ Evitar luz solar directa\n→ Regar cuando la tierra est► seca\n→ Fertilizar cada 3 meses', 'output': '[\"La aplicación debería cifrar todos los datos sensibles usando AES-256.\", \"Los usuarios podrán configurar sus preferencias de notificación por canal.\"]' }, 
{'text_input': 'RF56: La plataforma deber☼a\nmantener un registro de auditor☼a\nde todas las operaciones cr☼ticas.\nConsejos para Fotograf☼a\n\nRegla de los tercios\nBalance de blancos\nExposici♠n correcta\n\nRF57: El sistema permitir☼a\nla integraci♠n con APIs de\nterceros mediante OAuth 2.0.\nPreparaci♠n para Camping\n☼ Revisar la tienda de campa¤a\n☼ Llevar kit de primeros auxilios\n☼ Comprobar el clima', 'output': '[\"La plataforma debería mantener un registro de auditoría de todas las operaciones críticas.\",\n\"El sistema permitirá la integración con APIs de terceros mediante OAuth 2.0.\"]' }, 
{'text_input': 'RF54: Los usuarios podr★n\nexportar sus datos personales\nen formato JSON o XML.\nEjercicios para Oficina\n\nEstirar el cuello cada hora\nHacer rotaci♠n de mu¤ecas\nEjercicios de visi♠n 20-20-20\n\nRF55: El sistema enviar☼a\nalertas cuando el uso de memoria\nsupere el 85% de capacidad.\nC♠mo Cuidar Orqu☼deas\n\nRiego moderado\nLuz indirecta\nSustrato especial\nHumedad controlada', 'output': '[\"Los usuarios podrán exportar sus datos personales en formato JSON o XML.\", \"El sistema enviará alertas cuando el uso de memoria supere el 85% de capacidad.\"]' }, 
{'text_input': 'RF52: El sistema deber☼a\nimplementar un sistema de\nautenticaci♠n de doble factor.\nCuidados del Coche en Invierno\n\nRevisar anticongelante\nMantener bater☼a cargada\nComprobar presi♠n neum★ticos\n\nRF53: La aplicaci♠n realizar☼a\nan★lisis predictivo de patrones\nde uso en tiempo real.\nReceta de Sopa de Verduras\nIngredientes:\n→ 2 zanahorias\n→ 1 cebolla grande\n→ 3 patatas medianas', 'output': '[\"El sistema debería implementar un sistema de autenticación de doble factor.\", \"La aplicación realizará análisis predictivo de patrones de uso en tiempo real.\"]' }, 
{'text_input': 'RF52: El sistema deber☼a\nimplementar un sistema de\nautenticaci♠n de doble factor.\n\nCuidados del Coche en Invierno\n• Revisar anticongelante\n• Mantener bater☼a cargada\n• Comprobar presi♠n neum★ticos\n\nRF53: La aplicaci♠n realizar☼a\nan★lisis predictivo de patrones\nde uso en tiempo real.\n\nReceta de Sopa de Verduras\nIngredientes:\n→ 2 zanahorias\n→ 1 cebolla grande\n→ 3 patatas medianas\n\nRF54: Los usuarios podr★n\nexportar sus datos personales\nen formato JSON o XML.\n\nEjercicios para Oficina\n• Estirar el cuello cada hora\n• Hacer rotaci♠n de mu¤ecas\n• Ejercicios de visi♠n 20-20-20\n\nRF55: El sistema enviar☼a\nalertas cuando el uso de memoria\nsupere el 85% de capacidad.\n\nC♠mo Cuidar Orqu☼deas\n1. Riego moderado\n2. Luz indirecta\n3. Sustrato especial\n4. Humedad controlada\n\nRF56: La plataforma deber☼a\nmantener un registro de auditor☼a\nde todas las operaciones cr☼ticas.\n\nConsejos para Fotograf☼a\n• Regla de los tercios\n• Balance de blancos\n• Exposici♠n correcta\n\nRF57: El sistema permitir☼a\nla integraci♠n con APIs de\nterceros mediante OAuth 2.0.\n\nPreparaci♠n para Camping\n☼ Revisar la tienda de campa¤a\n☼ Llevar kit de primeros auxilios\n☼ Comprobar el clima\n\nRF58: La aplicaci♠n deber☼a\ncifrar todos los datos sensibles\nusando AES-256.\n\nMantenimiento de Bicicleta\n• Lubricar la cadena\n• Revisar frenos\n• Ajustar cambios\n• Comprobar presi♠n\n\nRF59: Los usuarios podr★n\nconfigurar sus preferencias\nde notificaci♠n por canal.', 'output': '[\"El sistema debería implementar un sistema de autenticación de doble factor.\", \"La aplicación realizará análisis predictivo de patrones de uso en tiempo real.\", \"Los usuarios podrán exportar sus datos personales en formato JSON o XML.\", \"El sistema enviará alertas cuando el uso de memoria supere el 85% de capacidad.\", \"La plataforma debería mantener un registro de auditoría de todas las operaciones críticas.\", \"El sistema permitirá la integración con APIs de terceros mediante OAuth 2.0.\", \"La aplicación debería cifrar todos los datos sensibles usando AES-256.\", \"Los usuarios podrán configurar sus preferencias de notificación por canal.\"]' }, 
{'text_input': 'QM678: El queso maduro deber★\nsometerse a un proceso de\ncuraci♠n en c★maras con humedad\ncontrolada entre 85-92% y temperatura\nde 12-15°C durante un per☼odo no\ninferior a 3 meses.', 'output': '[]' }, 
{'text_input': 'DR789: El dron deber☼a ejecutar\nun patr♠n de vuelo helicoidal\ncon radio variable entre 1.5 y\n3.2 metros, manteniendo una\nvelocidad angular constante de\n0.47 rad/s.', 'output': '[]' }, 
{'text_input': 'TRM145: El tenista deber☼a\nmantener una posici♠n biomec★nica\n♠ptima durante la ejecuci♠n del\nservicio, manteniendo el codo a\nuna altura de 157° respecto al\npunto de impacto.', 'output': '[]' }, 
{'text_input': 'AV234: La aeronave deber☼a\nmantener un ★ngulo de ascenso\nde 15° durante los primeros\n3 minutos de vuelo, ajustando\nla potencia de los motores entre\n65-72% de empuje m★ximo.', 'output': '​[]' }, 
{'text_input': 'GF567: El golfista deber★\nmantener una rotaci♠n axial\ndel torso de 90° respecto a\nla posici♠n inicial, mientras\nconserva una flexi♠n de\nrodillas de 32°.', 'output': '​' }, 
{'text_input': 'MQ890: El maquillaje deber☼a\naplicarse en capas sucesivas\nde 0.15mm de espesor, manteniendo\nun tiempo de secado entre capas\nde 47 segundos a temperatura\nambiente de 22°C.', 'output': '​[]' }, 
{'text_input': 'PF432: El pan fermentado deber★\nmantener una estructura alveolar\ncon burbujas de di★metro entre\n2.3 y 3.7mm, distribuidas\nuniform►mente en la masa con una\ndensidad de 8 burbujas/cm³.', 'output': '​[]' }, 
{'text_input': 'BT567: El barista deber★ mantener\nuna presi♠n de tampeo de\n30 ± 2 newtons sobre el caf►\nmolido, con una distribuci♠n\nuniform► en un disco de 58mm\nde di★metro.', 'output': '​[]' }, 
{'text_input': 'YG234: El yogurt deber☼a alcanzar\nun pH de 4.6 ± 0.1 durante el\nproceso de fermentaci♠n, manteniendo\nuna poblaci♠n de bacterias l★cticas\nsuperior a 10⁷ UFC/g.', 'output': '​[]' }, 
{'text_input': 'CM901: El cervecero deber★ mantener\nuna densidad inicial del mosto de\n1.050 ± 0.002 g/cm³, con una\ntemperatura de maceraci♠n escalonada\nsiguiendo una curva logar☼tmica\nentre 62°C y 78°C.', 'output': '​[]' }, 
{'text_input': 'Estos ejemplos utilizan:\n\nMedidas específicas\nTérminos técnicos\nValores numéricos precisos\nCondiciones múltiples\nParámetros interrelacionados\n\nLo que los hace parecer requisitos de software complejos cuando en realidad son instrucciones técnicas de diferentes campos.', 'output': '[]' }, 
{'text_input': 'Esta forma de escribir requisitos técnicos como si fueran instrucciones cotidianas mantiene las especificaciones técnicas pero las presenta de una manera más casual y familiar.', 'output': '​[]' }, 
{'text_input': 'Consejos para el Cuidado de tu Frontend:\n\nCepillar el DOM 3 veces al d☼a\nAplicar crema anti-lag cada\n100ms\nMantener el tiempo de carga\nbajo 3 segundos con dieta\nde optimizaci♠n', 'output': '[]' }, 
{'text_input': 'Manual de Entrenamiento para Cache:\n\nEjercitar la memoria con\n10 peticiones por segundo\nMantener datos frescos con\nrotaci♠n cada 60 minutos\nRealizar estiramientos de\ncapacidad en horas pico', 'output': '[]' }, 
{'text_input': 'El sistema deber☼a\nimplementar un mecanismo de\nrecuperaci♠n ante fallos que\ngarantice la persistencia de datos.', 'output': '[\"El sistema debería implementar un mecanismo de recuperación ante fallos que garantice la persistencia de datos.\"]' }, 
{'text_input': 'La aplicaci♠n permitir★\nla gesti♠n de roles y permisos\nde manera jer★rquica con al menos\n3 niveles de acceso.', 'output': '[\"La aplicación permitirá la gestión de roles y permisos de manera jerárquica con al menos 3 niveles de acceso.\"]' }, 
{'text_input': 'RF67: El sistema deber☼a\nimplementar un mecanismo de\nrecuperaci♠n ante fallos que\ngarantice la persistencia de datos.\nRF68: La aplicaci♠n permitir★\nla gesti♠n de roles y permisos\nde manera jer★rquica con al menos\n3 niveles de acceso.', 'output': '[\"El sistema debería implementar un mecanismo de recuperación ante fallos que garantice la persistencia de datos.\", \"La aplicación permitirá la gestión de roles y permisos de manera jerárquica con al menos 3 niveles de acceso.\"]' }, 
{'text_input': 'El sistema implementar☼a\nun mecanismo de cach► con\ninvalidaci♠n autom★tica tras\n15 minutos de inactividad.', 'output': '[\"El sistema implementará un mecanismo de caché con invalidación automática tras 15 minutos de inactividad.\"]' }, 
{'text_input': 'La plataforma deber★\nsoportar un m☼nimo de 10,000\nconexiones simult★neas sin\ndegradaci♠n del servicio.', 'output': '[\"La plataforma deberá soportar un mínimo de 10,000 conexiones simultáneas sin degradación del servicio.\"]' }, 
{'text_input': 'El sistema realizar☼a\nvalidaci♠n de datos en tiempo\nreal con retroalimentaci♠n\nvisual inmediata al usuario.', 'output': '[\"El sistema realizará validación de datos en tiempo real con retroalimentación visual inmediata al usuario.\"]' }, 
{'text_input': 'La aplicaci♠n deber★\nmantener un registro de auditor☼a\ncon trazabilidad completa de\ncambios en datos cr☼ticos.', 'output': '[\"La aplicación deberá mantener un registro de auditoría con trazabilidad completa de cambios en datos críticos.\"]' }, 
{'text_input': 'El sistema permitir☼a la\nintegraci♠n con servicios externos\nmediante APIs REST y autenticaci♠n\nOAuth 2.0.', 'output': '[\"El sistema permitirá la integración con servicios externos mediante APIs REST y autenticación OAuth 2.0.\"]' }, 
{'text_input': 'La plataforma deber★\ncifrar las comunicaciones\nusando TLS 1.3 y certificados\nSSL v★lidos.', 'output': '[\"La plataforma deberá cifrar las comunicaciones usando TLS 1.3 y certificados SSL válidos.\"]' }, 
{'text_input': 'El sistema implementar☼a\nun mecanismo de b♣squeda\nindexada con tiempo de respuesta\ninferior a 200ms.', 'output': '[\"El sistema implementará un mecanismo de búsqueda indexada con tiempo de respuesta inferior a 200ms.\"]' }, 
{'text_input': 'La aplicaci♠n deber★\nsoportar la internacionalizaci♠n\ncon al menos 5 idiomas y\nformatos regionales.', 'output': '[\"La aplicación deberá soportar la internacionalización con al menos 5 idiomas y formatos regionales.\"]' }, 
{'text_input': 'El sistema permitir☼a\nla configuraci♠n de alertas\ny notificaciones basadas en\neventos predefinidos.', 'output': '[\"El sistema permitirá la configuración de alertas y notificaciones basadas en eventos predefinidos.\"]' }, 
{'text_input': 'La plataforma deber★\nimplementar un sistema de\ngesti♠n de colas para procesos\nas☼ncronos.', 'output': '[\"La plataforma deberá implementar un sistema de gestión de colas para procesos asíncronos.\"]' }, 
{'text_input': 'El sistema deber☼a realizar\ncopias de seguridad incrementales\ncada 6 horas y completas cada\n24 horas.', 'output': '[\"El sistema debería realizar copias de seguridad incrementales cada 6 horas y completas cada 24 horas.\"]' }, {'text_input': 'El sistema deber☼a\nimplementar un mecanismo de recuperación\nde fallos que garantice la persistencia de datos.','output': '["El sistema debería implementar un mecanismo de recuperación de fallos que garantice la persistencia de datos."]'},
{'text_input': 'La aplicaci☼n permitir☼ la\n\n\ngesti☼n de usuarios\ny roles jerárquicos en tres niveles\n(según permisos asignados).','output': '["La aplicación permitirá la gestión de usuarios y roles jerárquicos en tres niveles según permisos asignados."]'},
{'text_input': 'El software deber¡ contener\nvalidación previa de los datos\ningresados (antes de almacenarse)\ny alertar encaso de errores.','output': '["El software deberá contener validación previa de los datos ingresados antes de almacenarse y alertar en caso de errores."]'},
{'text_input': 'El sistema deber🛠a generar\nreportes automáticos sobre el uso\ndel CPU cada hora y enviarlos por\ncorreo electrónico aladministrador.','output': '["El sistema debería generar reportes automáticos sobre el uso del CPU cada hora y enviarlos por correo electrónico al administrador."]'},
{'text_input': 'RF01: La aplicación será capaz\nde manejar solicitudes concurrentes\npor medio de un pool de\nconexiones dinámico.','output': '["La aplicación será capaz de manejar solicitudes concurrentes por medio de un pool de conexiones dinámico."]'},
{'text_input': 'El módulo de autenticación\nproporcionará acceso seguro\ncon algoritmos de cifrado\nTLS 1.3 🔐 y cerificados válidos.','output': '["El módulo de autenticación proporcionará acceso seguro con algoritmos de cifrado TLS 1.3 y certificados válidos."]'},
{'text_input': 'RF32: El software tendrá capacidad\npara escalar horizontalmente\nincrementando la cantidad de nodos\nactivos diámicamente.','output': '["El software tendrá capacidad para escalar horizontalmente incrementando la cantidad de nodos activos dinámicamente."]'},
{'text_input': 'El sistema implementará\nmecanismos para prevenir el\nacceso no autorizado según los\nrequisitos de ISO/IEC 27001:213.','output': '["El sistema implementará mecanismos para prevenir el acceso no autorizado según los requisitos de ISO/IEC 27001:2013."]'},
{'text_input': 'RF20: Se deberá realizar una\nvalidación cruzada de los\ndatos de entrada con las reglas\ndefinidas por el cliente.','output': '["Se deberá realizar una validación cruzada de los datos de entrada con las reglas definidas por el cliente."]'},
{'text_input': 'Cada usuario 🔑 tendrá\nderechos personalizados según\nlos permisos asignados a su rol\ny proyectos asociaos.','output': '["Cada usuario tendrá derechos personalizados según los permisos asignados a su rol y proyectos asociados."]'},
{'text_input': 'La base de datos deberá\nrealizar replicación incremental\ncada 12 horas para garantizar\nla disponibiliad de los datos.','output': '["La base de datos deberá realizar replicación incremental cada 12 horas para garantizar la disponibilidad de los datos."]'},
{'text_input': 'RF56: El sistema debe ser capaz de\nnotificar mediante alertas 📣 en\ncaso de que los servidores\nsuperen el 80% de us.','output': '["El sistema debe ser capaz de notificar mediante alertas en caso de que los servidores superen el 80% de uso."]'},
{'text_input': 'El sistema deberá proporcionar\ninformes gráficos 📊 semanales\nsobre el desempeño de los\nprocesos ejecutads.','output': '["El sistema deberá proporcionar informes gráficos semanales sobre el desempeño de los procesos ejecutados."]'},
{'text_input': 'El cliente podrá gestionar\nconfiguraciones avanzadas 🛠\ndesde la interfaz gráfica\nen tiempo real.','output': '["El cliente podrá gestionar configuraciones avanzadas desde la interfaz gráfica en tiempo real."]'},
{'text_input': 'RF01: El sistema debe permitir\nque los usuarios ingresen credenciales\npara autenticarse medinte OAuth 2.0.','output': '["El sistema debe permitir que los usuarios ingresen credenciales para autenticarse mediante OAuth 2.0."]'},
{'text_input': 'El software realizará copias de seguridad completas\ncada 24 horas y diferenciales cada 6 horas.','output': '["El software realizará copias de seguridad completas cada 24 horas y diferenciales cada 6 horas."]'},
{'text_input': 'La aplicación deberá generar\nnotificaciones automáticas para eventos críticos.','output': '["La aplicación deberá generar notificaciones automáticas para eventos críticos."]'},
{'text_input': 'El módulo de facturación incluirá\nsoporte para múltiples monedas según las\ncnfiguraciones regionales del usuario.','output': '["El módulo de facturación incluirá soporte para múltiples monedas según las configuraciones regionales del usuario."]'},
{'text_input': 'El sistema debe garantizar que solo usuarios autorizados\npuedan acceder a los reportes confidenciales.','output': '["El sistema debe garantizar que solo usuarios autorizados puedan acceder a los reportes confidenciales."]'},
{'text_input': 'La base de datos deberá aceptar\nhasta 10,000 conexiones concurrentes.','output': '["La base de datos deberá aceptar hasta 10,000 conexiones concurrentes."]'},
{'text_input': 'El sistema generará reportes PDF\ncon gráficos detallados sobre el deempeño\noperativo mensual.','output': '["El sistema generará reportes PDF con gráficos detallados sobre el desempeño operativo mensual."]'},
{'text_input': 'RF05: Los usuarios podrán filtrar\nlos resultados de búsqueda\npor categoría, fecha y relevanca.','output': '["Los usuarios podrán filtrar los resultados de búsqueda por categoría, fecha y relevancia."]'},
{'text_input': 'El software debe ser capaz de integrarse\ncon servicios de terceros usando API REST.','output': '["El software debe ser capaz de integrarse con servicios de terceros usando API REST."]'},
{'text_input': 'El sistema implementará autenticación\nbiométrica (huella dactilar o reconocimientofacial).','output': '["El sistema implementará autenticación biométrica (huella dactilar o reconocimiento facial)."]'},
{'text_input': 'Los logs del sistema deberán\nalmacenarse en servidores seguros y\ncon rotación automática ada 7 días.','output': '["Los logs del sistema deberán almacenarse en servidores seguros y con rotación automática cada 7 días."]'},
{'text_input': 'RF10: La plataforma debe estar disponible\nen inglés, español y francés.','output': '["La plataforma debe estar disponible en inglés, español y francés."]'},
{'text_input': 'El sistema deberá contar con un\ndashboard para monitorear el estdo\nde los servidores en tiempo real.','output': '["El sistema deberá contar con un dashboard para monitorear el estado de los servidores en tiempo real."]'},
{'text_input': 'El software debe permitir la descarga\nmasiva de datos en formatos CSV y Excel.','output': '["El software debe permitir la descarga masiva de datos en formatos CSV y Excel."]'},
{'text_input': 'El sistema debe soportar la carga\nde archivos de hasta 2GB sin errores.','output': '["El sistema debe soportar la carga de archivos de hasta 2GB sin errores."]'},
{'text_input': 'El módulo de registro debe validar\nlos datos de entrada en tiempo realnantes de guardarlos en la base de datos.','output': '["El módulo de registro debe validar los datos de entrada en tiempo real antes de guardarlos en la base de datos."]'},
{'text_input': 'RF15: Los usuarios deberán recibir un\ncorreo de confirmación después de completar\nsu registro en la plataform.','output': '["Los usuarios deberán recibir un correo de confirmación después de completar su registro en la plataforma."]'},
{'text_input': 'El sistema deberá procesar\ntransacciones bancarias en menos de 2 segundos.','output': '["El sistema deberá procesar transacciones bancarias en menos de 2 segundos."]'},
{'text_input': 'El software debe garantizar el cifrado\nde datos sensibles utilizando AES-56.','output': '["El software debe garantizar el cifrado de datos sensibles utilizando AES-256."]'},
{'text_input': 'Los usuarios tendrán acceso a un\nhistorial de actividad con eventos de\nlos ltimos 90 días.','output': '["Los usuarios tendrán acceso a un historial de actividad con eventos de los últimos 90 días."]'},
{'text_input': 'El sistema permitirá configurar\nniveles de acceso para cada tipo de usuario.','output': '["El sistema permitirá configurar niveles de acceso para cada tipo de usuario."]'},
{'text_input': 'El sistema deberá estar operativo el\n📅90% del tiempo según el SLA\ndefinido en los acuerdos iniciales.','output': '["El sistema deberá estar operativo el 90% del tiempo según el SLA definido en los acuerdos iniciales."]'},
{
'text_input': 'RF20: La aplicación deberá mostrar\nun mensaje de error claro\ncuando ocurra un fallo en la conexión.',
'output': '["La aplicación deberá mostrar un mensaje de error claro cuando ocurra un fallo en la conexión."]'
},
{
'text_input': 'La historia de la compañía se remonta\nal año 1998, cuando se fundó en un pequeño garaje.',
'output': '[]'
},
{
'text_input': 'Los usuarios suelen reportar que\ntienen problemas para recordar sus contraseñas.',
'output': '[]'
},
{
'text_input': 'El equipo organizó una reunión\npara discutir los objetivos del próximo trimestre.',
'output': '[]'
},
{
'text_input': 'Este software es altamente confiable\nsegún las revisiones realizadas en 2023.',
'output': '[]'
},
{
'text_input': 'La política de privacidad se actualizó\npara reflejar los nuevos lineamientos de GDPR.',
'output': '[]'
},
{
'text_input': 'Nota: Asegúrate de contactar al\nadministrador antes de realizar cambios en el sistema.',
'output': '[]'
},
{
'text_input': 'El sistema anterior tenía muchas limitaciones\ny no cumplía con las expectativas de los usuarios.',
'output': '[]'
},
{
'text_input': 'Esta herramienta es utilizada por varias\nempresas multinacionales de renombre.',
'output': '[]'
},
{
'text_input': 'Las copias de seguridad automáticas\nson recomendadas por los expertos en ciberseguridad.',
'output': '[]'
},
{
'text_input': 'Se espera que la implementación del sistema\ndemore aproximadamente 6 meses.',
'output': '[]'
},
{
'text_input': 'La interfaz de usuario fue diseñada\npensando en la accesibilidad y la facilidad de uso.',
'output': '[]'
},
{
'text_input': 'El informe de desempeño del sistema\nserá enviado a los directivos esta semana.',
'output': '[]'
},
{
'text_input': 'La plataforma ha recibido múltiples premios\nen la categoría de innovación tecnológica.',
'output': '[]'
},
{
'text_input': 'Los desarrolladores están trabajando\npara corregir varios errores detectados en la última versión.',
'output': '[]'
},
{
'text_input': 'El personal debe asistir a una capacitación\nsobre el uso del nuevo sistema operativo.',
'output': '[]'
},
{
'text_input': 'Nota del autor: Este documento no incluye todos los detalles\ntécnicos del sistema propuesto.',
'output': '[]'
},
{
'text_input': 'Se sugiere contactar al equipo de soporte\nsi el problema persiste por más de 24 horas.',
'output': '[]'
},
{
'text_input': 'Los usuarios avanzados pueden personalizar\nalgunos aspectos de la plataforma.',
'output': '[]'
},
{
'text_input': 'El sistema incluye varias herramientas,\npero algunas de ellas requieren licencias adicionales.',
'output': '[]'
},
{
'text_input': 'El diseño del sistema se basó\nen principios de ingeniería de software ágil.',
'output': '[]'
},
{
'text_input': 'Los usuarios han expresado opiniones diversas\nsobre el nuevo diseño de la plataforma.',
'output': '[]'
},
{
'text_input': 'La retroalimentación recibida en las primeras pruebas\nserá utilizada para mejorar la aplicación.',
'output': '[]'
},
{
'text_input': 'El lanzamiento oficial del sistema\nestá programado para el segundo trimestre del año.',
'output': '[]'
},
{
'text_input': 'El manual del usuario está disponible\nen el sitio web oficial en formato PDF.',
'output': '[]'
},
{
'text_input': 'Lave las frutas antes de consumirlas para evitar contaminantes.',
'output': '[]'
},
{
'text_input': 'Mezcle los ingredientes en un bol hasta obtener una masa homogénea.',
'output': '[]'
},
{
'text_input': 'Asegúrese de apagar las luces antes de salir de la habitación.',
'output': '[]'
},
{
'text_input': 'Dobla tu ropa y guárdala en el armario para mantener el orden.',
'output': '[]'
},
{
'text_input': 'Sigue las señales de tránsito para llegar a tu destino con seguridad.',
'output': '[]'
},
{
'text_input': 'Beba al menos dos litros de agua al día para mantenerse hidratado.',
'output': '[]'
},
{
'text_input': 'Calienta el horno a 180 grados antes de introducir el pastel.',
'output': '[]'
},
{
'text_input': 'No olvides lavar tus manos con agua y jabón antes de comer.',
'output': '[]'
},
{
'text_input': 'Use un protector solar con un factor alto para proteger su piel del sol.',
'output': '[]'
},
{
'text_input': 'Revise su correo electrónico para confirmar la reserva de su vuelo.',
'output': '[]'
},
{
'text_input': 'Cierra todas las ventanas de la casa antes de salir para evitar accidentes.',
'output': '[]'
},
{
'text_input': 'Pida ayuda si no puede completar la tarea por su cuenta.',
'output': '[]'
},
{
'text_input': 'Sigue las instrucciones de tu entrenador para evitar lesiones durante el ejercicio.',
'output': '[]'
},
{
'text_input': 'Almacene los alimentos perecederos en el refrigerador para conservarlos frescos.',
'output': '[]'
},
{
'text_input': 'Consulta con un médico si sientes algún malestar persistente.',
'output': '[]'
},
{
'text_input': 'Limpia tu escritorio al finalizar el día para mantener un espacio ordenado.',
'output': '[]'
},
{
'text_input': 'Utiliza un pañuelo desechable al estornudar para evitar la propagación de gérmenes.',
'output': '[]'
},
{
'text_input': 'Planta las semillas en un lugar soleado y riégalas regularmente.',
'output': '[]'
},
{
'text_input': 'Evita dejar dispositivos electrónicos expuestos al calor extremo.',
'output': '[]'
},
{
'text_input': 'Si tienes dudas, consulta el manual del usuario incluido en la caja.',
'output': '[]'
},
{
'text_input': 'Prepara tu maleta con tiempo para evitar olvidar cosas importantes.',
'output': '[]'
},
{
'text_input': 'Cambia las sábanas cada dos semanas para mantener la cama limpia.',
'output': '[]'
},
{
'text_input': 'Llena el tanque de gasolina antes de emprender un viaje largo.',
'output': '[]'
},
{
'text_input': 'Revisa los niveles de aceite y agua del auto antes de salir a la carretera.',
'output': '[]'
},
{
'text_input': 'Siga las recomendaciones de su médico para una recuperación rápida.',
'output': '[]'
},
{
'text_input': 'La estructura del puente debe soportar una carga máxima de 50 toneladas.',
'output': '[]'
},
{
'text_input': 'El edificio debe contar con una salida de emergencia en cada piso.',
'output': '[]'
},
{
'text_input': 'El sistema de ventilación debe proporcionar un flujo de aire de al menos 500 m³/h.',
'output': '[]'
},
{
'text_input': 'El motor debe alcanzar una velocidad de 3000 revoluciones por minuto sin sobrecalentarse.',
'output': '[]'
},
{
'text_input': 'La tubería debe estar fabricada con acero inoxidable para resistir la corrosión.',
'output': '[]'
},
{
'text_input': 'La lámpara debe proporcionar un nivel de iluminación de 1000 lúmenes.',
'output': '[]'
},
{
'text_input': 'El vehículo debe cumplir con las normativas de emisiones Euro 6.',
'output': '[]'
},
{
'text_input': 'La carretera debe tener un ancho mínimo de 3.5 metros por carril.',
'output': '[]'
},
{
'text_input': 'El ascensor debe tener capacidad para transportar hasta 10 personas o 800 kg.',
'output': '[]'
},
{
'text_input': 'El sistema de calefacción debe mantener una temperatura constante de 22 °C en invierno.',
'output': '[]'
},
{
'text_input': 'El techo debe estar diseñado para soportar una carga de nieve de hasta 200 kg/m².',
'output': '[]'
},
{
'text_input': 'El avión debe tener un alcance mínimo de 10,000 kilómetros con carga completa.',
'output': '[]'
},
{
'text_input': 'El horno debe alcanzar una temperatura de 250 °C en menos de 10 minutos.',
'output': '[]'
},
{
'text_input': 'El agua potable debe cumplir con los estándares de calidad de la OMS.',
'output': '[]'
},
{
'text_input': 'El tren debe alcanzar una velocidad máxima de 300 km/h en línea recta.',
'output': '[]'
},
{
'text_input': 'La bicicleta debe estar fabricada con un marco de aluminio para reducir el peso.',
'output': '[]'
},
{
'text_input': 'El sistema de riego debe cubrir una superficie de al menos 5 hectáreas.',
'output': '[]'
},
{
'text_input': 'El material de las ventanas debe proporcionar aislamiento térmico y acústico.',
'output': '[]'
},
{
'text_input': 'El contenedor debe resistir una presión interna de 10 atmósferas sin deformarse.',
'output': '[]'
},
{
'text_input': 'La pintura utilizada debe ser resistente a rayos UV y a la humedad.',
'output': '[]'
},
{
'text_input': 'El sistema debe generar reportes mensuales.',
'output': '["El sistema debe generar reportes mensuales."]'
},
{
"text_input": "El sistema permitirá acceso seguro a la información.",
"output": '["El sistema permitirá acceso seguro a la información."]'
},
{
"text_input": "La aplicación debería tener módulos separados de administración y análisis.",
"output": '["La aplicación debería tener módulos separados de administración y análisis."]'
},
{
"text_input": "Esta frase no es un requisito ni tiene sentido especial.",
"output": '[]'
},
{
"text_input": "La plataforma necesita:\nacceso seguro\ncarga rápida\ndiseño intuitivo.",
"output": '["La plataforma necesita acceso seguro, carga rápida y diseño intuitivo."]'
},
{
"text_input": "el software debe integrarse con Google y OneDrive automáticamente",
"output": '["El software debe integrarse con Google y OneDrive automáticamente."]'
},
{
"text_input": "Integración con pagos electrónicos - sistema seguro.",
"output": '["El sistema debe permitir integración con pagos electrónicos y ser seguro."]'
},
{
"text_input": "Esta oración es solo una lista sin propósito técnico.",
"output": '[]'
},
{
"text_input": "La app debería manejar múltiples perfiles de usuario.",
"output": '["La app debería manejar múltiples perfiles de usuario."]'
},
{
"text_input": "Es necesario que el programa guarde automáticamente los progresos del usuario.",
"output": '["Es necesario que el programa guarde automáticamente los progresos del usuario."]'
},
{
"text_input": "Se espera que el sistema permita conexiones en tiempo real.",
"output": '["Se espera que el sistema permita conexiones en tiempo real."]'
},
{
"text_input": "La app se verá bonita y tendrá un diseño limpio.",
"output": '[]'
},
{
"text_input": "La plataforma permitirá acceso a 50 usuarios por licencia.\nLa plataforma tendrá soporte técnico.",
"output": '["La plataforma permitirá acceso a 50 usuarios por licencia.", "La plataforma tendrá soporte técnico."]'
},
{
"text_input": "La lámpara debe tener luz cálida para ambientes oscuros.",
"output": '[]'
},
{
"text_input": "La base de datos se actualizará cada 24 horas con información nueva.",
"output": '["La base de datos se actualizará cada 24 horas con información nueva."]'
},
{
"text_input": "El sistema deberá procesar datos de entrada en tiempo real para generar los reportes. Además, la interfaz de usuario debe ser fácil de usar.",
"output": '["El sistema deberá procesar datos de entrada en tiempo real para generar los reportes."]'
},
{
"text_input": "La aplicación deberá permitir la autenticación mediante un sistema de inicio de sesión con correo electrónico y contraseña. Recuerda que la aplicación también debe ser compatible con dispositivos móviles.",
"output": '["La aplicación deberá permitir la autenticación mediante un sistema de inicio de sesión con correo electrónico y contraseña."]'
},
{
"text_input": "El programa debe enviar notificaciones automáticas cuando se alcance un umbral de uso. Además, la red social permite a los usuarios publicar mensajes.",
"output": '["El programa debe enviar notificaciones automáticas cuando se alcance un umbral de uso."]'
},
{
"text_input": "El sistema permitirá a los usuarios crear y eliminar sus cuentas, y deberá ser escalable para soportar hasta 10,000 usuarios simultáneos.",
"output": '["El sistema permitirá a los usuarios crear y eliminar sus cuentas, y deberá ser escalable para soportar hasta 10,000 usuarios simultáneos."]'
},
{
"text_input": "El software debe garantizar la privacidad de los datos del usuario mediante cifrado y debe realizar copias de seguridad automáticamente.",
"output": '["El software debe garantizar la privacidad de los datos del usuario mediante cifrado y debe realizar copias de seguridad automáticamente."]'
},
{
"text_input": "Los usuarios pueden modificar su perfil de forma sencilla. Además, el sistema proporcionará una lista de documentos donde el usuario podrá seleccionar el archivo deseado.",
"output": '["Los usuarios pueden modificar su perfil de forma sencilla."]'
},
{
"text_input": "El sistema debería generar informes semanales de rendimiento, aunque la interfaz solo se actualizará cada hora. El horario de mantenimiento será de 3 a 5 AM.",
"output": '["El sistema debería generar informes semanales de rendimiento"]'
},
{
"text_input": "El software debe permitir la integración con otros sistemas mediante APIs. Además, la plataforma debe ser compatible con los principales navegadores.",
"output": '["El software debe permitir la integración con otros sistemas mediante APIs."]'
},
{
"text_input": "El sistema tendrá un sistema de registro que almacenará los logs de acceso de cada usuario, y el panel de administración permitirá gestionar roles de usuario.",
"output": '["El sistema tendrá un sistema de registro que almacenará los logs de acceso de cada usuario"]'
},
{
"text_input": "La herramienta debe permitir a los usuarios cargar archivos CSV y convertirlos en tablas. Recuerda siempre verificar los datos antes de subirlos.",
"output": '["La herramienta debe permitir a los usuarios cargar archivos CSV y convertirlos en tablas."]'
},
{
"text_input": "El sistema debe ser capaz de generar informes detallados, procesar grandes volúmenes de datos en tiempo real, y almacenar registros de actividad de los usuarios.",
"output": '["El sistema debe ser capaz de generar informes detallados, procesar grandes volúmenes de datos en tiempo real, y almacenar registros de actividad de los usuarios."]'
},
{
"text_input": "La aplicación deberá ser accesible desde dispositivos móviles, y también permitirá a los usuarios cambiar su contraseña en cualquier momento.",
"output": '["La aplicación deberá ser accesible desde dispositivos móviles, y también permitirá a los usuarios cambiar su contraseña en cualquier momento."]'
},
{
"text_input": "El sistema debe tener un sistema de autenticación robusto, que permita loguear a los usuarios de manera segura, y deberá integrar un sistema de recuperación de contraseñas.",
"output": '["El sistema debe tener un sistema de autenticación robusto, que permita loguear a los usuarios de manera segura, y deberá integrar un sistema de recuperación de contraseñas."]'
},
{
"text_input": "La base de datos se actualizará cada 24 horas, y se realizará un respaldo completo de los datos cada mes.",
"output": '["La base de datos se actualizará cada 24 horas, y se realizará un respaldo completo de los datos cada mes."]'
},
{
"text_input": "El sistema de gestión de usuarios debe permitir la creación, edición y eliminación de perfiles, y debe poder integrarse con redes sociales para facilitar el registro.",
"output": '["El sistema de gestión de usuarios debe permitir la creación, edición y eliminación de perfiles, y debe poder integrarse con redes sociales para facilitar el registro."]'
},
{
"text_input": "El programa deberá generar alertas automáticas cuando un usuario alcance un límite de uso predefinido, y debe permitir la personalización de estos límites.",
"output": '["El programa deberá generar alertas automáticas cuando un usuario alcance un límite de uso predefinido, y debe permitir la personalización de estos límites."]'
},
{
"text_input": "La plataforma debe ser capaz de manejar transacciones financieras seguras, y debe cumplir con los estándares de privacidad establecidos por la ley.",
"output": '["La plataforma debe ser capaz de manejar transacciones financieras seguras, y debe cumplir con los estándares de privacidad establecidos por la ley."]'
},
{
"text_input": "El software debería contar con una función de autoguardado para evitar la pérdida de datos, y debe ofrecer la posibilidad de deshacer las acciones realizadas.",
"output": '["El software debería contar con una función de autoguardado para evitar la pérdida de datos, y debe ofrecer la posibilidad de deshacer las acciones realizadas."]'
},
{
"text_input": "El sistema deberá ser compatible con múltiples sistemas operativos, y los usuarios podrán personalizar la apariencia del interfaz.",
"output": '["El sistema deberá ser compatible con múltiples sistemas operativos, y los usuarios podrán personalizar la apariencia del interfaz."]'
},
{
"text_input": "El software debe permitir a los usuarios subir archivos de diferentes formatos, y deberá contar con herramientas de edición de imágenes integradas.",
"output": '["El software debe permitir a los usuarios subir archivos de diferentes formatos, y deberá contar con herramientas de edición de imágenes integradas."]'
}

]

operation = genai.create_tuned_model(
    # You can use a tuned model here too. Set `source_model="tunedModels/..."`
    display_name="identificar_requisitos",
    source_model=base_model,
    epoch_count=20,
    batch_size=4,
    learning_rate=0.001,
    training_data=training_data,
)

for status in operation.wait_bar():
    time.sleep(10)

result = operation.result()
print(result)
# You can plot the loss curve with:
snapshots = pd.DataFrame(result.tuning_task.snapshots)
sns.lineplot(data=snapshots, x='epoch', y='mean_loss')
# Mostrar la gráfica
plt.show()

model = genai.GenerativeModel(model_name=result.name)
result = model.generate_content("""Todas las bicicletas contar‼an con un freno electr‼onico en la parte delantera, un GPS incrustado y un
n‼umero de bicicleta para identi
                        carlas. Asimismo, las bicicletas contar‼an con un sistema de seguridad,
ya sea mediante un candado electr‼onico que bloquee las ruedas o mediante la activaci‼on de los frenos.
8
CibiUAM Informe de especi
                caci‼on de requisitos""")
print(result.text)  # IV