from flask import Flask
from extensions import db, migrate

#para manejar las rutas de los controladores
from controllers import all_blueprints

app = Flask(__name__)

#activa el contexto para pa base de datos
app.app_context().push()

#configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/saludos'
db.init_app(app)

#configuracion de la migracion, para crear la base de datos, tabals, etc
migrate.init_app(app, db)

#registra los controladores dinamicamente
for blueprint in all_blueprints:
    app.register_blueprint(blueprint)

