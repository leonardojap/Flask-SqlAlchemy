from extensions import db

class Saludo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    mensaje = db.Column(db.String(120), nullable=False, unique=True)

    def __init__(self, mensaje):
        self.mensaje = mensaje
    
    def serialize(self):
        return {
            'id': self.id,
            'mensaje': self.mensaje
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        return "Saludo guardado"

    def get_all():
        saludo = Saludo.query.all()
        return [saludo.serialize() for saludo in saludo]
    
    def get_by_id(id):
        saludo = Saludo.query.get(id)
        if saludo is None:
            return None
        return saludo.serialize()
    
    def get_by_content(content):
        saludos = Saludo.query.filter(Saludo.mensaje.contains(content)).all()
        return [saludo.serialize() for saludo in saludos] 
    