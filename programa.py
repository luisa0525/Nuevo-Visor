from flask import Flask,render_template, request, redirect, url_for
from db import db
from marcador import Marcador

class Programa:

    def __init__(self):

        self.app=Flask(__name__)
        self.app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///marcadores.sqlite3"

        db.init_app(self.app)

        self.app.add_url_rule('/', view_func=self.Visor)
        self.app.add_url_rule('/nuevo', view_func=self.agregar, methods=["GET","POST"])
        self.app.add_url_rule('/puntos', view_func=self.puntitos)

        #iniciar el servidor
        with self.app.app_context():
            db.create_all()
            self.app.run(debug=True)

    def Visor(self):
        return render_template('visor.html', Marcador=marcador.query.all())
    
    def puntitos(self):
        return render_template('mostrartodos.html', Marcador=marcador.query.all())

    def agregar(self):

        #VERIFICAR OPERACION

        if request.method=="POST":

            #CREAR OBJETO
            nombre=request.form['nombre']
            latitud=request.form['latitud']
            longitud=request.form['longitud']
            direccion=request.form['descripcion']
            contacto=request.form['contacto']
            miMarcador=marcador(nombre, latitud, longitud, direccion, contacto)

            #guardar el objeto
            db.session.add(miMarcador)
            db.session.commit()

            return redirect(url_for('visor.html'))



        return render_template('nuevomarcador.html')
    
miPrograma=Programa()