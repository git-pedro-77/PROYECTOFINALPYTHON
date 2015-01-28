# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import ventaDao
from flask import render_template, request, redirect, url_for


@app.route("/mainventa")# para entar a la pagina por main persona al metodo
def mainventa():
    objv=ventaDao.VentaDao().reportarventa()#llamar al reporte
    return render_template("venta.html", tablaven=objv)#enviando al archivo html y ahi organizarlo


@app.route("/addventa", methods=['POST'])
def addventa():
    vendedor=request.form.get('vendedor', type=str)
    turno=request.form.get('turno', type=str)
    fechaventa=request.form.get('fechaven', type=str)
    gestion=request.form.get('gestion', type=str)
    
    ventaDao.VentaDao().grabarVenta(vendedor, turno, fechaventa, gestion)
    return redirect(url_for('mainventa'))

@app.route("/buscarautov")# para entar a la pagina por main persona al metodo
def buscarventaAuto():
    nombre=str(request.args.get('term'))
    objv=ventaDao.VentaDao().buscarVentaFactura(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objv #enviando al archivo html y ahi organizarlo

'''@app.route("/eliminardatov")# para entar a la pagina por main persona al metodo
def eliminarventaDato():
    datoeli=request.args.get('id_cliente')
    ventaDao.VentaDao()
    return redirect(url_for('mainventa'))'''


@app.route("/buscardatov")# para entar a la pagina por main persona al metodo
def buscarventaDato():
    nombre=str(request.args.get('bnombre'))
    objv=ventaDao.VentaDao().buscarVentaDato(nombre)
    return render_template("venta.html", tablaven=objv)

@app.route("/buscardatov")# para entar a la pagina por main persona al metodo
def buscarDatov():
    nombre=str(request.args.get('nombrev'))
    objv=ventaDao.VentaDao().validarventa(nombre)
    return render_template("venta.html", tablaven=objv)


