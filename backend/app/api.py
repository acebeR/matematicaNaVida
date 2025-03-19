# api.py

from flask import Flask
from flask_restx import Api
from controllers.usuario_controller import UsuarioList

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração do Swagger (Flask-RESTX)
api = Api(app, version='1.0', title='API de Usuários', description='Uma API para gerenciar usuários')
ns = api.namespace('usuarios', description='Operações relacionadas aos usuários')

# Registrando as rotas no Swagger
ns.add_resource(UsuarioList, '/usuarios')

