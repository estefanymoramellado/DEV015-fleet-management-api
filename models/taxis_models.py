from . import db

# Definir el modelo de taxi
class Taxi(db.Model):
    __tablename__ = 'taxis'  # Define el nombre de la tabla
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)
    def __repr__(self):
        return f'<Taxi {self.plate}>'