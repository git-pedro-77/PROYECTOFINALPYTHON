# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import usuarioDao
from flask import render_template, request, redirect, url_for


@app.route("/mainusuario")# para entar a la pagina por main
def maintrabajador():
    objt=usuarioDao.usuarioDao().reportarusuario()()#llamar al reporte
    return render_template("usuario.html", data=objt)#enviando al archivo html y ahi organizarlo

@app.route("/addusuario", methods=['POST'])
def addTrabajador():
    usuario=request.form.get('usuario', type=str)
    clave=request.form.get('clave', type=str)
    estado=request.form.get('estado', type=int)
    fecha_acceso=request.form.get('fecha_Ingreso', type=str)
    idTipoTrabajador=request.form.get('tipoid', type=int)
    
    usuarioDao.usuarioDao().insertarusuario()
    return redirect(url_for('maintrabajador'))

@app.route("/buscarautopu")# para entar a la pagina por main persona al metodo
def buscarTrabajadorAuto():
    nombre=str(request.args.get('term'))
    objt=usuarioDao.usuarioDao().buscarTrabajadorNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return objt #enviando al archivo html y ahi organizarlo

@app.route("/eliminardatou")# para entar a la pagina por main persona al metodo
def eliminarTrabajadorDato():
    datoeli=request.args.get('idpersona')
    usuarioDao.usuarioDao().eliminarTrabajador(datoeli)
    return redirect(url_for('maintrabajador'))


@app.route("/buscardatou")# para entar a la pagina por main persona al metodo
def buscarTrabajadorDato():
    nombre=str(request.args.get('bnombre'))
    objt=usuarioDao.usuarioDao().buscarTrabajadorDato(nombre)
    return render_template("trabajador.html", data=objt)




