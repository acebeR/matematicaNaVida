from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Configuração do Swagger (Flask-RESTX)
api = Api(app, version='1.0', title='API de Usuários', description='Uma API para gerenciar usuários')
ns = api.namespace('usuarios', description='Operações relacionadas aos usuários')

# Definindo o modelo do usuário (para validação e documentação no Swagger)
usuario_model = api.model('Usuario', {
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário')
})

# Função de conexão com o PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="meubanco", 
        user="usuario", 
        password="senha", 
        host="meu_postgres",  # nome do container do PostgreSQL no Docker
        port="5432"
    )
    return conn

# Rota para listar os usuários
@ns.route('/usuarios')
class UsuarioList(Resource):
    def get(self):
        """Retorna a lista de usuários"""
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute('SELECT * FROM usuarios;')
        usuarios = cursor.fetchall()
        cursor.close()
        conn.close()
        return usuarios

    def post(self):
        """Cadastra um novo usuário"""
        data = request.get_json()
        nome = data['nome']
        email = data['email']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO usuarios (nome, email) VALUES (%s, %s)',
            (nome, email)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return {'message': 'Usuário cadastrado com sucesso!'}, 201

# Função principal
if __name__ == '__main__':
    app.run(debug=True)
