from flask import Blueprint, request
from services.saludo import create_saludo, get_saludos, get_saludo_by_id, get_saludos_by_content
saludo_bp = Blueprint('saludo', __name__)

@saludo_bp.route('/saludo', methods=['GET'])
def saludo():
    return get_saludos()

@saludo_bp.route('/saludo/<int:id>', methods=['GET'])
def saludo_id(id):
    return get_saludo_by_id(id)

@saludo_bp.route('/saludo', methods=['POST'])
def saludo_post():
    return create_saludo(request.json['mensaje'])

@saludo_bp.route('/saludo/filter/<string:conten>', methods=['GET'])
def saludo_filter(conten):
    return get_saludos_by_content(conten)
