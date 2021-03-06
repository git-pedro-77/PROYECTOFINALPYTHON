# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import productoDao
from flask import render_template, request, redirect, url_for


@app.route("/mainproducto")# para entar a la pagina por main persona al metodo
def mainproducto():
    objp=productoDao.ProductoDao().reportarproducto()#llamar al reporte
    return render_template("producto.html", databdprod=objp)#enviando al archivo html y ahi organizarlo


@app.route("/addproducto", methods=['POST'])
def addProducto():
    codigo=request.form.get('codproducto', type=str)
    nombre=request.form.get('nombre', type=str)
    precio=request.form.get('precio', type=str)
    proveedor=request.form.get('proveedor', type=str)
    fechacrea=request.form.get('fechaelab', type=str)
    fechavenc=request.form.get('fechaven', type=str)
    
    productoDao.ProductoDao().insertarproducto(codigo, nombre, precio, proveedor, fechacrea, fechavenc)
    return redirect(url_for('mainproducto'))

@app.route("/buscarautop")# para entar a la pagina por main persona al metodo
def buscarproductoAuto():
    nombre=str(request.args.get('term'))
    objp=productoDao.ProductoDao().buscarproductoNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objp #enviando al archivo html y ahi organizarlo

@app.route("/eliminardatop")# para entar a la pagina por main persona al metodo
def eliminarproductoDato():
    datoeli=request.args.get('id_producto')
    productoDao.ProductoDao().eliminarproducto(datoeli)
    return redirect(url_for('mainproducto'))


@app.route("/buscardatop")# para entar a la pagina por main persona al metodo
def buscarproductoDato():
    nombre=str(request.args.get('bnombre'))
    objp=productoDao.ProductoDao().buscarproductoDato(nombre)
    return render_template("producto.html", databdprod=objp)


'''@app.route("/buscardatop")# para entar a la pagina por main persona al metodo
def buscarDatot():
    nombre=str(request.args.get('nombret'))
    objp=productoDao.productoDao().validartrabajador(nombre)
    return render_template("producto.html", databdprod=objp)
'''



