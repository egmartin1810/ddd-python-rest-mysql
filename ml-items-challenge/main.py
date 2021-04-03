from flask import Flask
from flask import jsonify
from config import BasicConfig
from flask_sqlalchemy import SQLAlchemy
from ml.challenge.rest.excepciones.internalservererror import InternalServerError
import ml.challenge.rest.recursoprocesararchivoitems as recursoprocesararchivoitems

# Por: Giovanni Martinez
# Fecha: 2021/03/31
# Descripción: main de la api con flask
app = Flask(__name__)
# Cargar las propiedades del archivo de confinguración.
app.config.from_object(BasicConfig)
# Conexión a la bd.
db = SQLAlchemy(app)

# Metodos de la API
# POST: guardar los items recuperado de una fuente externa.
@app.route('/api/v1/almacenardatositems', methods=['POST'])
def almacenardatositems():
    print("Entrando al método[POST] almacenardatositems....")
    # Crear el recurso para procesar el archivo.
    recPrcesadorArcItems = recursoprocesararchivoitems.RecursoProcesarArchivoItems()
    respuesta = recPrcesadorArcItems.procesarArchivoItemsStreameable()
    # Adiciociona Ejecución exitosa a la respuesta.
    respuesta['mensaje'] = 'Ejecicion Exitosa'
    print("Saliendo del método[POST] almacenardatositems....")
    return jsonify(respuesta)

# Manejar los errores lanzados por las otras capas para responder al usuario.
@app.errorhandler(InternalServerError)
def handle_internal_server_(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

# Main.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
