from flask import Flask
from gestionImmob.database.db import initialize_db
from flask_restful import Api
from gestionImmob.routes import initialize_routes
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
#app.config['ENV_FILE_LOCATION'] =  {'path' : './.env'}
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'

api = Api(app)
# sécurisation des mdp avec une fct de hashage
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


app.config['MONGODB_SETTINGS'] = {
'host': 'mongodb://localhost/gestion-immob'
}

initialize_db(app)

initialize_routes(api)

app.run()