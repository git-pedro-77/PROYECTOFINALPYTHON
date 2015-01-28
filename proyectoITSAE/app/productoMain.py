# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import productoDao 
from flask import render_template, request, redirect, url_for


@app.route("/mainproducto")# para entar a la pagina por main persona al metodo
def maincliente():
    objp=productoDao.productoDao().reportarproducto()#llamar al reporte
    return render_template("producto.html", data=objp)#enviando al archivo html y ahi organizarlo


@app.route("/addproducto", methods=['POST'])
def addCliente():
    dni_cliente=request.form.get('Cedula', type=str)
    nombre=request.form.get('nombre', type=str)
    apellido=request.form.get('apellido', type=str)
    celular=request.form.get('celular', type=str)
    direccion=request.form.get('direccion', type=str)
    correo=request.form.get('correo', type=str)
    sexo=request.form.get('sexo', type=str)
    telefono=request.form.get('telefono', type=str)
    estado=request.form.get('estado', type=int)
    
    productoDao.productoDao().insertarproducto(dni_cliente, nombre, apellido, celular, direccion, correo, sexo, telefono, estado)
    return redirect(url_for('maincliente'))

@app.route("/buscarautoc")# para entar a la pagina por main persona al metodo
def buscarPersonaAuto():
    nombre=str(request.args.get('term'))
    objp=productoDao.productoDao().buscarproductoNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objp #enviando al archivo html y ahi organizarlo

@app.route("/eliminardatoc")# para entar a la pagina por main persona al metodo
def eliminarPersonaDato():
    datoeli=request.args.get('id_cliente')
    productoDao.productoDao().eliminarproducto(datoeli)
    return redirect(url_for('maincliente'))


@app.route("/buscardatoc")# para entar a la pagina por main persona al metodo
def buscarPersonaDato():
    nombre=str(request.args.get('bnombre'))
    objp=productoDao.productoDao().buscarproductoDato(nombre)
    return render_template("cliente.html", data=objp)


@app.route("/buscardatoc")# para entar a la pagina por main persona al metodo
def buscarDatot():
    nombre=str(request.args.get('nombret'))
    objR=productoDao.productoDao().validartrabajador(nombre)
    return render_template("cliente.html", data=objR)




