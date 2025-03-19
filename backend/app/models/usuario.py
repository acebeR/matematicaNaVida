# Descrição: Tudo que tem haver com Banco

import psycopg2
from psycopg2.extras import RealDictCursor

# Função para conexão com o banco de dados PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        dbname="meubanco", 
        user="usuario", 
        password="senha", 
        host="meu_postgres",  # nome do container do PostgreSQL no Docker
        port="5432"
    )
    return conn

# Função para obter todos os usuários do banco de dados
def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute('SELECT * FROM usuarios;')
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return usuarios

# Função para inserir um usuário no banco de dados
def add_usuario(nome, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO usuarios (nome, email) VALUES (%s, %s)',
        (nome, email)
    )
    conn.commit()
    cursor.close()
    conn.close()
