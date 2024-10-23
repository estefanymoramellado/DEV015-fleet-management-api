from flask import Flask, jsonify
from models import db, init_app  # Solo importa db y Taxi desde models
from models.taxis_models import Taxi


app = Flask(__name__)
# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg://default:7ClPIws1tSvd@ep-delicate-bush-a4p1lwcb.us-east-1.aws.neon.tech:5432/verceldb"

# Inicializa la base de datos
init_app(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Hola mundo")
# Definir endpoint para obtener taxis
@app.route('/taxis', methods=['GET'])
def taxis():
    taxis = Taxi.query.all()  # Obtiene todos los registros de la tabla Taxi
    return jsonify([{'id': taxi.id, 'plate': taxi.plate} for taxi in taxis])  # Retorna una lista de taxis en formato JSON
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea todas las tablas si no existen
    app.run(debug=True)  # Inicia la aplicación