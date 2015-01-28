# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''

from ec.edu.itsae.conn import DBcon 
#from flask import redirect, url_for
import json 


class VentaDao(DBcon.DBcon):#heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
    
    def reportarventa(self):
        con=self.conexion().connect().cursor()  #capturando de la clase DBcon
        con.execute(" select * from venta ")
        reporte=con.fetchall()
        return reporte #despues del return no se debe colocar nada
    
    def grabarVenta(self, vendedor, turno, fechaventa,gestion ):
        con=self.conexion().connect()
        sql= """insert into venta(vendedor, turno, fechaventa, gestion)
                             values ('%s','%s', '%s','%s')
                             """ %(vendedor, turno, fechaventa,gestion ) 
        #print sql    Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)#aqui debe estar sql para que se ejecute el insert
    
        #deber actualizar y eliminar
        
        '''  def eliminarCliente(self,datoelim):
        con=self.conexion().connect()
        sql= """ delete from cliente where id_cliente= %i """ %int(datoelim)
        #print sql    Para imprimir nuestra consulta para poder ver        
        with con:
            cursor=con.cursor()
            cursor.execute(sql)'''
    
    def buscarVentaFactura(self, datobusca):
        con=self.conexion().connect().cursor()
        con.execute(""" select CONCAT (nombre,' ', apellido) as value, id_cliente as id from cliente where upper(CONCAT (nombre,' ', apellido)) like upper('%s') """ %("%"+datobusca+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna,row)))
        return json.dumps(lista, indent=2) 
    
    def buscarVentaDato(self, datobuscado):
        con=self.conexion().connect().cursor() 
        sql=""" select * from cliente  where upper(CONCAT (nombre,' ', apellido)) like upper('%s') """ %("%"+datobuscado+"%")
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte 

    
    def validarventa(self, datot):
        con=self.conexion().connect().cursor() 
        sql=""" select * from personas p, trabajador t where t.idpersona=%i """ %(datot)
        con.execute(sql)
        reporte=con.fetchall() 
        return reporte 
    
    
    