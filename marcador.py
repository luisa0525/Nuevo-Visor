from db import db

class Marcador(db.Model):

    # nombre

    __tablename__="marcador"

    # conjunto de atributos

    id=db.Column(db.Integer, primary_key=True)
    latitud=db.Column(db.Float(50))
    longitud=db.Column(db.Float(50))
    descripcion=db.Column(db.String(100))

    # metodo constructor

    def __init__(self, latitud, longitud, descripcion):

        self.latitud=latitud
        self.longitud=longitud
        self.descripcion=descripcion