from flask_sqlalchemy import SQLAlchemy
# Crear la instancia de SQLAlchemy
db = SQLAlchemy()
def init_app(app):
    db.init_app(app)  # Inicializa la instancia de la base de datos con la aplicación