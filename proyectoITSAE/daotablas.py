# coding:utf-8
'''
Created on 19/1/2015

@author: PC30
'''

from ec.edu.itsae.dao import usuarioDao
from ec.edu.itsae.dao import ClienteDao

'''vamos a crear un objeto de persona dao'''

obj=ClienteDao.ClienteDao()
print obj.reportarCliente()

objt=usuarioDao.UsuarioDao()
print objt.reportarusuario()


#objt=usuarioDao.TrabajadorDao()
#print objt.reportarTrabajador()