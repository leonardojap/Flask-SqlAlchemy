from utils.generic_response import StandardResponse
from models.saludo import Saludo


def get_saludos():
    try:
        return StandardResponse.build('Saludos obtenidos exitosamente', True, Saludo.get_all())
    except Exception as e:
        return StandardResponse.build('Error al obtener saludos', False, str(e), 500)

def get_saludo_by_id(id):
    try:
        saludo = Saludo.get_by_id(id)
        if saludo is None:
            return StandardResponse.build('Saludo no encontrado', False, None, 404)
        return StandardResponse.build('Saludo obtenido exitosamente', True, saludo)
    except Exception as e:
        return StandardResponse.build('Error al obtener saludo', False, str(e), 500)

def create_saludo(mensaje):
    try:
        saludo = Saludo(mensaje)
        saludo.save()
        return StandardResponse.build('Saludo guardado exitosamente', True, saludo.serialize())
    except Exception as e:
        return StandardResponse.build('Error al guardar saludo', False, str(e), 500)
    
def get_saludos_by_content(content):
    try:
        return StandardResponse.build('Saludos obtenidos exitosamente', True, Saludo.get_by_content(content))
    except Exception as e:
        return StandardResponse.build('Error al obtener saludos', False, str(e), 500)