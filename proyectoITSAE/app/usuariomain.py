# coding:utf-8
'''
Created on 27/1/2015

@author: Programacion
'''
from app import app
from ec.edu.itsae.dao import usuarioDao
from flask import render_template, request, redirect, url_for


@app.route("/mainusuario")# para entar a la pagina por main
def mainusuario():
    obju=usuarioDao.UsuarioDao().reportarusuario()#llamar al reporte
    return render_template("usuario.html", usuariobd=obju)#enviando al archivo html y ahi organizarlo

@app.route("/addusuario", methods=['POST'])
def addUsuario():
    nombre=request.form.get('usuario', type=str)
    contrasena=request.form.get('clave', type=str)
    rep_contrasena=request.form.get('repclave', type=str)
    estado=request.form.get('estado', type=int)
    
    usuarioDao.UsuarioDao().insertarusuario(nombre, contrasena, rep_contrasena, estado)
    return redirect(url_for('mainusuario'))

@app.route("/buscarautou")# para entar a la pagina por main persona al metodo
def buscarUsuarioAuto():
    nombre=str(request.args.get('term'))
    obju=usuarioDao.UsuarioDao().buscarusuarioNombre(nombre)#llamar al reporte
    # print objR  #solo es para provar las impresiones
    return obju #enviando al archivo html y ahi organizarlo

@app.route("/eliminardatou")# para entar a la pagina por main persona al metodo
def eliminarUsuarioDato():
    datoeli=request.args.get('id_user')
    usuarioDao.UsuarioDao().eliminarusuario(datoeli)
    return redirect(url_for('mainusuario'))


@app.route("/buscardatou")# para entar a la pagina por main persona al metodo
def buscarUsuarioDato():
    nombre=str(request.args.get('bnombre'))
    obju=usuarioDao.UsuarioDao().buscarusuarioDato(nombre)
    return render_template("usuario.html", usuariobd=obju)




