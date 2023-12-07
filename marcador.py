from db import db

class Marcador(db.Model):

    # nombre

    __tablename__="marcador"

    # conjunto de atributos

    id=db.Column(db.Integer, primary_key=True)
    
    nombre=db.Column(db.string(50))
    latitud=db.Column(db.Float(50))
    longitud=db.Column(db.Float(50))
    direccion=db.Column(db.String(100))
    contacto=db.Column(db.string(10))

    # metodo constructor

    def __init__(self, nombre, latitud, longitud, direccion, contacto):

        self.latitud=latitud
        self.latitud=latitud
        self.longitud=longitud
        self.direccion=direccion
        self.contacto=contacto
