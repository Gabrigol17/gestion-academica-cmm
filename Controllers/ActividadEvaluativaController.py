from flask import Blueprint, request, jsonify
from Services.ActividadEvaluativaService import ActividadEvaluativaService

actividad_bp = Blueprint('actividad_evaluativa', __name__)
service = ActividadEvaluativaService()

@actividad_bp.route('/actividades', methods=['POST'])
def add_actividad():
    """
    Ruta para crear una nueva Actividad Evaluativa
    Esperado: JSON con (id_componente, id_periodo, titulo, descripcion, fecha_entrega)
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se proporcionaron datos en la solicitud"}), 400

    try:
        resultado = service.add(data)
        return jsonify({
            "message": "Actividad evaluativa creada exitosamente",
            "result": resultado
        }), 201
    except Exception as e:
        return jsonify({"error": f"Error al crear la actividad: {str(e)}"}), 500


@actividad_bp.route('/actividades', methods=['GET'])
@actividad_bp.route('/actividades/<int:id_actividad>', methods=['GET'])
def read_actividad(id_actividad=None):
    """
    Ruta para consultar todas las actividades o una específica por su ID
    """
    try:
        resultado = service.read(id_actividad)
        
        if id_actividad and not resultado:
            return jsonify({"message": "Actividad evaluativa no encontrada"}), 404
            
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({"error": f"Error al consultar actividades: {str(e)}"}), 500


@actividad_bp.route('/actividades/<int:id_actividad>', methods=['PUT'])
def update_actividad(id_actividad):
    """
    Ruta para actualizar una Actividad Evaluativa existente por su ID
    """
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No se proporcionaron datos para actualizar"}), 400

    try:
        resultado = service.update(id_actividad, data)
        return jsonify({
            "message": "Actividad evaluativa actualizada exitosamente",
            "result": resultado
        }), 200
    except Exception as e:
        return jsonify({"error": f"Error al actualizar la actividad: {str(e)}"}), 500


@actividad_bp.route('/actividades/<int:id_actividad>', methods=['DELETE'])
def delete_actividad(id_actividad):
    """
    Ruta para eliminar una Actividad Evaluativa por su ID
    """
    try:
        resultado = service.delete(id_actividad)
        return jsonify({
            "message": "Actividad evaluativa eliminada exitosamente",
            "result": resultado
        }), 200
    except Exception as e:
        return jsonify({"error": f"Error al eliminar la actividad: {str(e)}"}), 500