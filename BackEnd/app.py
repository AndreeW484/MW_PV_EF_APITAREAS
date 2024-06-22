# Importación de librerías a utilizar para serialización y desserialización.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Inicialización de aplicación Flask y configuración de la Base de Datos MySQL local
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://AndreeW484:Invierno2024@127.0.0.1:3306/apiflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Instanciación de la base de datos y del serializador
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Creación de Modelo para procesamiento de los datos
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion_tarea = db.Column(db.String(150), nullable=False)
    fecha_maxima_realizacion = db.Column(db.Date, nullable=False)

# Creación de la clase Schema para aplicar apropiadamente el modelo y procesar bien cada registro de entrada como de salida.
class TareaSchema(SQLAlchemyAutoSchema):
    class Meta:
        modelo = Tarea
        load_instance = True

tarea_schema = TareaSchema()
tarea_schema = TareaSchema(many=True)