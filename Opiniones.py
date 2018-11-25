#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from BaseDeDatos import BaseDeDatos 

class Opiniones():
    
    listaArgumentos = ['numeroDeopiniones','calificacion','compartido','mencionesEnlaweb','comentarios','usuario','fecha','respuesta','comentarioInadecuado']
    _listaObjetos = []

    @classmethod
    def regresarArgumentos(cls):
        return cls.listaArgumentos

    @classmethod
    def regresarObjeto(cls,argumento, nombreObjeto):
        for objeto in cls._listaObjetos:
            cadena = eval('objeto.'+argumento)
            if cadena == nombreObjeto: 
                return objeto

    @classmethod
    def eliminarObjeto(cls, objet):
        for objeto in cls._listaObjetos:
            if objeto == objet:
                cls._listaObjetos.remove(objet)
    
    @classmethod
    def editarArgumento(cls, argumento, objeto, dato):
       for arg in cls.listaArgumentos:
                if argumento == arg:
                    for obj in cls._listaObjetos:
                        if obj == objeto:
                            eval('cls._listaObjetos[cls._listaObjetos.index(obj)].'+argumento+' = dato')

                    

    @staticmethod
    def crearPrevios():
        listas = BaseDeDatos.obtenerDatosTotales('numeroDeopiniones')
        for lista in listas:
            Opiniones(lista)

    @classmethod
    def listarObjetos(cls, objeto):
        cls._listaObjetos.append(objeto)

    def crearBase(self):
        BaseDeDatos('numeroDeopiniones',self.listaArgumentos)

    def __init__(self, modo = None):
        
        if modo == 1:
            self.numeroDeopiniones = input('Numero de opiniones: ')
            self.calificacion = input('calificacion : ')
            self.compartido = input('compartido : ')
            self.mencionesEnlaweb = input('menciones en la web : ')
            self.comentarios = input('comentarios : ')
            self.usuario = input('usuario : ')
            self.fecha = input('fecha : ')
            self.respuesta = input('respuesta : ')
            self.comentarioInadecuado = input('Comentario inadecuado: ')
            self.listarObjetos(self)
            BaseDeDatos.agregarDatos('Usuario', [self.numeroDeopiniones,self.calificacion,self.compartido,self.mencionesEnlaweb,self.comentarios,self.usuario,self.fecha,self.respuesta,self.comentarioInadecuado], self.listaArgumentos)
        elif modo != None:
            self.numeroDeopiniones = modo[0]
            self.calificacion = modo[1]
            self.compartido = modo[2]
            self.mencionesEnlaweb = modo[3]
            self.comentarios = modo[4]
            self.usuario = modo[5]
            self.fecha = modo[6]
            self.respuesta = modo[7]
            self.comentarioInadecuado = modo[8]
            self.listarObjetos(self)
        else:
            self.crearBase()

