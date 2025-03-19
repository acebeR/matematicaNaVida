# matematicaNaVida
Jogo para ...

# Tecnologias usadas
- Python
- PostgreSQL
- Docker

#  Padrão de arquitetura de software
- MVC(Model-View-Controller)

# Estrutura
matematicanavida/
├── app/
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
└── Dockerfile
# Passo a Passo para rodar o Projeto
- Passo 1: Instalar o Docker
- Passo 2: Rodar o Projeto com Docker Compose
- Passo 3: Para iniciar: docker-compose up --build
- Passo 4: Para parar: docker-compose down
- Passo 5: Testar a Aplicação
- Passo 6:docker logs matematicanavida
- Passo 7: Para acessar Configurações de banco, projeto... no Docker.
- docker exec -it meu_postgres psql -U usuario meubanco
- Dentro do container do banco use: psql -U usuario meubanco para entrar no pronpt do banco.

# Link locall
http://localhost:5000


