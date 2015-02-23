# coding:utf-8
'''
Created on 22/2/2015

@author: User
'''


from ec.edu.itsae.conn import DBcon
#from flask import redirect, url_for 
import json 


class FacturaDao(DBcon.DBcon): #heredando
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass#sirve cuando no hay implementacion en el metodo
    
          
    def buscarClienteNombre(self, datobusca):
        con=self.conexion().connect().cursor()
        con.execute(""" select CONCAT (nombre,' ', apellido) as value, id_cliente as id from cliente where upper(CONCAT (nombre,' ', apellido)) like upper('%s') """ %("%"+datobusca+"%") )
        reporte=con.fetchall()
        columna=('value', 'id')
        lista=[]
        for row in reporte:
            lista.append(dict(zip(columna,row)))
        return json.dumps(lista, indent=2)