from flask import Flask
from sqlalchemy.pool import QueuePool

from config import BasicConfig
from flask_sqlalchemy import SQLAlchemy
import ml.challenge.dominio.interf.impl.procesadorarchivoimpl as procesadorarchivoimpl

# import ml.challenge.repositorio.persistencia.modelo.user as usr

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
    proc_ = procesadorarchivoimpl.ProcesadorArchivoImpl(app.config['ARCHIVO_NOMBRE'], app.config['ARCHIVO_FORMATO'],
                                                        app.config['ARCHIVO_SEPARADOR'], app.config['ARCHIVO_ENCODING'],
                                                        app.config['THREADPOOLEXECUTOR_NUM_WORKERS'])
    # procesar el archivo con los items
    respuesta = proc_.procesarArchivoStreameable()
    response = {'mensaje': 'Ejecución Exitosa', 'tiempo': respuesta}
    print("Saliendo del método[POST] almacenardatositems....")
    return response


# Main.
if __name__ == '__main__':
    app.run(host='0.0.0.0')
