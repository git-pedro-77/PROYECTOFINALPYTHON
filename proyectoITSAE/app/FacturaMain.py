#coding: utf-8 
'''
Created on 22/2/2015

@author: User
'''
from app import app
from flask import render_template, request
from ec.edu.itsae.dao import FacturaDao

   
@app.route("/mainfactura")
def factura():
    return render_template("factura.html")

@app.route("/buscarfacturacliente")# para entar a la pagina por main persona al metodo
def buscarFacturaCliente():
    nombre=str(request.args.get('term'))
    objf=FacturaDao.FacturaDao().buscarClienteNombre(nombre)
    return objf #enviando al archivo html y ahi organizarlo