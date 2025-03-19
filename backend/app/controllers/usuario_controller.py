# Tudo que tem haver com regras de negócio.

from flask_restx import Resource, fields
from models.usuario import get_usuarios, add_usuario

# Definindo o modelo do usuário (para validação e documentação no Swagger)
usuario_model = fields.String(required=True, description='Nome do usuário')

# Rota para listar os usuários e adicionar um novo
class UsuarioList(Resource):
    def get(self):
        """Retorna a lista de usuários"""
        usuarios = get_usuarios()
        return usuarios

    def post(self):
        """Cadastra um novo usuário"""
        data = request.get_json()
        nome = data['nome']
        email = data['email']

        add_usuario(nome, email)
        return {'message': 'Usuário cadastrado com sucesso!'}, 201
