# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''

from ec.edu.itsae.conn import DBcon
import json 


class TrabajadorDao(DBcon.DBcon):#heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
    
    def reportarusuario(self):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(" select * from user ")
        reporte=con.fetchall()
        return reporte #despues del return no se debe colocar nada

    def insertarusuario(self, nombre, contrasena, rep_contrasena, estado):
        con=self.conexion().connect()
        sql= """insert into user(nombre, contraseña, rep_contraseña, estado)
                             values ('%s', '%s', '%s', %i)
                             """ %(nombre, contrasena, rep_contrasena, estado) 
        # print sql   Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
        #deber actualizar y eliminar
    def eliminarusuario(self,datoelim):
        con=self.conexion().connect()
        sql= """ delete from user where id_user= %i """ %int(datoelim)
        #print sql    Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
    def buscarusuarioNombre(self, datobusca):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(""" select CONCAT (nombre) as value, id_user as id from user where upper(CONCAT (nombre)) like upper('%s') """ %("%"+datobusca+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        print con.execute
        for row in reporte:
            lista.append(dict(zip(columna,row))) #dict = diccionario, zip = para unir las las dos columnas
        return json.dumps(lista, indent=2) 
    
    def buscarusuarioDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        sql=""" select * from user where upper(CONCAT (nombre)) like upper('%s') """ %("%"+datobuscado+"%")
        print sql
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte 
    
    
    '''
    def validarUsuario(self, usuario,clave):
        con=self.conexion().connect().cursor() 
        con.execute(""" select * from trabajador where usuario='%s' and clave='%s' """ %(usuario, clave))
        reporte=con.fetchall() 
        return reporte '''

    
    