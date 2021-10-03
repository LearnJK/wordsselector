proyecto = {
    'original': '''
la idea es tener una app donde los estudiantes ingresen con su Usuario
yo habilito la plataforma y q solo sea con el Usuario
puedo tener un estado para indicar si el usuario se encuentra en su franja
la idea es dejar un reporte de actividades de los estudiantes
de igual forma para la actividad ellos van a crear estas listas se van a persistir en un xls
en ese xls se van crear unas hojas por estudiantes y se van a crear unas listas que van a ser las que ellos crearon
ellos pueden agregar listas cada vez q quieran y agregar elementos a la lista
la lista va relacionada a el texto que se esta separando y secmentado
es decir quiero un objeto con el texto y las diferentes palabras
que ellos seleccionen del color de la clasificacion en la que se encuentran
que pasa con las palabras repetidas?
hay una opcion para armar frases, en que consiste?
es hacer un drag and drop para correr las palabras y agregarlas a una lista
hay una opcion de lista nueva en la mitad que me permite cuando agrego una nueva 
palabra abrir un promp para preguntar el nombre de la nueva lista
puedo cambiar el color de el elemento segun el color de la lista que se va creando
debemos hacer un ramdon de listas para los colores de los elementos que se agregen despues de agregar 7 listas
es una hoja por estudiante entopnces hay q revisar el guardado como funcionaria
ver proceso de carga del excel como recurso
ellos van a poder ingresar texto y secmentarlo, se crea el nuevo objeto con el texto ingresado 
preparado para las listas que agregen
en el objeto del texto sale tambien el estudiante este es el que debe registar el texto
cada texto queda guardado con un id este id debe actualizarce cuando el texto cambia el objeto que deberia hacer
pues el objeto seria aumentar su version cada vez que una palabra es actualizada y una mega version cada vez que agrega texto concatenando
puede actualizar palabra por palabra buscando sinonimos pero jamas debe borrar una palabra pues no e sla idea del ejercicio
pero si puede agregar esa palabra a una lista negra en la cual se revisara en una futura iteracion
tambien puede concatenar texto y buscar la forma de que se actualicen las palabras repetidas que hacen referencia a verbos
pues en algunos tipos de listas 

primero van a leer la redaccion toda... y vas a esribir un resumen de lo que entendieron que hace con sus propias palabras
despues van a capturar palabra por palabra para clasificar lo masevidente
vervos, acciones, operaciones,
objetos, personas, roles, 
adjetivos, calificativos, caracteristicas,
soin algunas de las listas 
cada palabra va a estar en una lista, la palabra no pued estar en 2 listas, pero si la palabra esta repetida si puede estar tanto en una como en otra
es decir si el texto tiene 100 palabras, las 100 palabras deben estar distribuidas entre las diferentes clasificaciones o listas que se hicieron

con pandas podemos procesar despues la longitud de las plabras, y hacer algunas trasnformaciones y estadisticas
''',
    'corto': 
'''
Probando el corto
'''
}

def getProyectData(proyect='original'):
    # get proyect information
    proyect = {'proyect':proyect}
    proyect['views'] = [
        'wordselector', 'selector'
        # 'battleracing', 'tester'
    ]    
    proyect['texto'] = createWordText(proyect['proyect'])
    proyect['listas'] = getList(proyect)
    return proyect
# -----------------------------------listas---------------------------------- #
def getList(user):
    listas = []
    return listas    

def createWordText(text='original'):  # esta creacion solo se realiza la primera vez
    ps = []
    parrafos = proyecto[text].split('\n')
    for p in parrafos:
        words = p.split()
        if(len(words) > 0):
            lwords = []
            for word in words:
                dword = {}
                dword['word'] = word
                dword['list'] = None
                dword['color'] = None
                dword['index'] = len(ps)
                lwords.append(dword)
            ps.append(lwords)
    return ps

# print('listas'.center(75,'-'))
