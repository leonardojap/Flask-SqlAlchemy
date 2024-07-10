from flask import jsonify
#definimos el objeto de respuesta estandar:
class StandardResponse:
    @staticmethod
    def build(message, success, data=None, status_code=200):
        response = {
            'message': message,
            'success': success,
            'data': data
        }
        return jsonify(response), status_code