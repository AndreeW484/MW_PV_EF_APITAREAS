# Importación de librerías a utilizar para serialización y desserialización.
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Inicialización de aplicación Flask y configuración de la Base de Datos MySQL local
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://AndreeW484:Invierno2024@127.0.0.1:3306/apiflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Instanciación de la base de datos y del serializador
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
        model = Tarea
        load_instance = True

tarea_schema = TareaSchema()
tareas_schema = TareaSchema(many=True)

# Elaboración de rutas API's/Endpoints empleando Flask
@app.route('/tarea', methods=['POST'])
def agregar_tarea():
    descripcion_tarea = request.json['descripcion_tarea']
    fecha_maxima_realizacion = request.json['fecha_maxima_realizacion']

    nueva_tarea = Tarea(descripcion_tarea=descripcion_tarea, fecha_maxima_realizacion=fecha_maxima_realizacion)
    db.session.add(nueva_tarea)
    db.session.commit()
    return jsonify(tarea_schema.dump(nueva_tarea)), 201

@app.route('/tarea', methods=['GET'])
def obtener_tareas():
    tareas = Tarea.query.all()
    resultado = tareas_schema.dump(tareas)
    return jsonify(resultado)

@app.route('/tarea/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea is None:
        return jsonify({'message': 'Tarea no encontrada por el id proporcionado'}), 404
    return jsonify(tarea_schema.dump(tarea))

@app.route('/tarea/<int:id>', methods=['DELETE'])
def borrar_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea is None:
        return jsonify({'message': 'Tarea no encontrada por el id proporcionado'}), 404
    db.session.delete(tarea)
    db.session.commit()
    return jsonify({'message': 'Tarea eliminada exitosamente'})

@app.route('/tarea/<int:id>', methods=['PUT'])
def actualizar_tarea(id):
    tarea = Tarea.query.get(id)
    if tarea is None:
        return jsonify({'message': 'Tarea no encontrada por el id proporcionado'}), 404

    descripcion_tarea = request.json['descripcion_tarea']
    fecha_maxima_realizacion = request.json['fecha_maxima_realizacion']

    tarea.descripcion_tarea = descripcion_tarea
    tarea.fecha_maxima_realizacion = fecha_maxima_realizacion

    db.session.commit()
    return jsonify(tarea_schema.dump(tarea))

if __name__ == '__main__':
    app.run(debug=True)


