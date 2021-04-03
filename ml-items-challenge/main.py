from flask import Flask
from flask import jsonify
from config import BasicConfig
from flask_sqlalchemy import SQLAlchemy
import ml.challenge.dominio.interf.impl.procesadorarchivoimpl as procesadorarchivoimpl
from ml.challenge.rest.excepciones.internalservererror import InternalServerError
import ml.challenge.dominio.interf.impl.procesadoritemsimpl as procesadoritemsimpl

# Por: Giovanni Martinez
# Fecha: 2021/03/31
# Descripción: main de la api con flask
app = Flask(__name__)
app.config.from_object(BasicConfig)
# Conexión a la bd.
db = SQLAlchemy(app)

# Metodos de la API
# POST: guardar los items recuperado de una fuente externa.
@app.route('/api/v1/almacenardatositems', methods=['POST'])
def almacenardatositems():
    print("Entrando al método[POST] almacenardatositems....")
    # Crear objeto de dominio para procesar el archivo.
    try:

        # Validar propiedad configurable app.config['BORRAR_TODOS_REGISTROS_ITEMSBD']
        if app.config['BORRAR_TODOS_REGISTROS_ITEMSBD']:
            # Eliminar todos los registros de Items que están persisitidos.
            domProcItem = procesadoritemsimpl.ProcesadorItemsImpl()
            domProcItem.eliminarTodosLosItemsPersistidos()

        # llamar al objeto de dominio encargado del procesamiento del archivo.
        domProcArchivo = procesadorarchivoimpl.ProcesadorArchivoImpl(app.config['ARCHIVO_NOMBRE'], app.config['ARCHIVO_FORMATO'],
                                                        app.config['ARCHIVO_SEPARADOR'], app.config['ARCHIVO_ENCODING'],
                                                        app.config['THREADPOOLEXECUTOR_NUM_WORKERS'])
        # procesar el archivo con los identificadores de los items
        respuesta = domProcArchivo.procesarArchivoStreameable()
    except Exception as err:
        print(f'(Exception) Error En la Ejecución del servicio: {err}')
        raise InternalServerError('Error Interno en el Sistema.', status_code=500)

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
