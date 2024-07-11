from flask import Flask
from extensions import db
import os
from dotenv import load_dotenv
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.engine.url import make_url

# Para manejar las rutas de los controladores
from controllers import all_blueprints

def create_app():
    app = Flask(__name__)
    load_dotenv()

    # Configuración de la base de datos
    DATABASE_URI = os.getenv('DATABASE_URL', 'fallback_default_database_uri')
    print(DATABASE_URI)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

    # Inicialización de la base de datos con la aplicación
    db.init_app(app)

    with app.app_context():
        # Intenta crear la base de datos si no existe
        if not database_exists(DATABASE_URI):
            create_database(DATABASE_URI)
        
        # Crear las tablas si no existen
        db.create_all()

    return app

app = create_app()

# Registra los controladores dinámicamente
for blueprint in all_blueprints:
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True)