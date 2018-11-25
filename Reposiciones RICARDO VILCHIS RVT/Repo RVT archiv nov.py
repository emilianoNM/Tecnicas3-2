#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#FUNCION: abrirArchivo(nombre)
#ENTRADA: Nombre del archivo a leer
#SALIDA: Tamaño del archivo y el archivo
def abrirArchivo(nombre):
    try:
        #Se trata de abrir el archivo
        archivo=open(nombre,'rb')
        #Se posiciona el puntero al final del archivo el primer argumento se refiere a cual va a ser el desplazamiento 
        #a partir del segundo argumento. El segundo argumento (2) se interpreta como el final del archivo
        archivo.seek(0,2)
        #Se guarda cual es la posicion del puntero, lo cual indica el tamaño
        tam=archivo.tell()
    except:
        #Si hay algun error, se manda un mensaje y se retornan valores invalidos 
        print("Error al abrir el archivo")
        return -1,None
    return tam,archivo

#FUNCION: crearArchivo(nombre,data)
#ENTRADA: nombre del archivo y los datos(bytes) a escribir 
#SALIDA: Una imagen.png de la galaxiaM51 
def crearArchivo(nombre,data):
    try:
        #Se abre el archivo en modo escritura de bytes y 
        #se escribe con los datos obtenidos
        archivo=open(nombre, "wb")
        archivo.write(data)
    except:
        print("No se pudo abiri el archivo")
    archivo.close()
    return

#FUNCION: buscar(magicNumber,tam,archivo)
#ENTRADA: Magic Number del archivo, tamaño del archivo, archivo
#SALIDA: datos(bytes) del archivo buscado
def buscar(magicNumber,tam,archivo):
    #Recorremos todo el archivo como una busqueda lineal
    for i in range(tam):
        #Posicionamos el puntero en cada numero recorrido
        archivo.seek(i)
        #Leemos un bloque de 8 bytes para compararlo con el
        #Magic Number
        bloque=archivo.read(8)
        #Comparamos el bloque con el Magic Number
        if bloque == magicNumber:
            print("Se encontro!!!! en ",i)
            #Leemos en los siguientes cuatro bytes la informacion sobre su tamaño
            file_size = archivo.read(4)
            #Estos bytes los convertimos a un numero entero y utilizamos from_bytes
            #Parametros file_size el arreglo de bytes que vamos a analizar
            #byteorder es como va a leer los datos en este caso 'little' se refiere a que
            #el byte mas significativo esta al final del arreglo de bytes
            #signed=False se refiere a si tiene signo el valor, al ser el tamaño un numero natural
            #no tiene signo(siempre es positivo)
            file_size = int.from_bytes(file_size, byteorder='little', signed=False)
            #Posicionamos el puntero de nuevo en la posicion original
            archivo.seek(i)
            #Guardamos el arreglo desde la posicion donde se encontro el magic number
            #hasta el tamaño del archivo mas los ultimos 8 bytes donde cierra el archivo
            file_data = archivo.read(file_size + 8)
            return file_data 
    return None
#Funcion Principal : Arranque del programa
def main():
    #Convertimos el string (en hexadecimal) a bytes 
    magicNumber='89 50 4E 47 0D 0A 1A 0A'
    magicNumber=bytes.fromhex(magicNumber)
    
    nombreArchivoOrigen='img.ext2'
    #Abrimos el archivo
    tam,archivo=abrirArchivo(nombreArchivoOrigen)
    if archivo==None:
        return
    #Buscamos el magic Number
    datos=buscar(magicNumber,tam,archivo)
    if datos ==None:
        print("No se encontró el archivo")
        return
    #Guardamos el archivo extraido si es que existe
    crearArchivo('galaxiaM51 .png',datos)
    
    archivo.close()
main()

