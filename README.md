# matematicaNaVida
Jogo para ...

# Tecnologias usadas
- Python
- PostgreSQL
- Docker

#  Padrão de arquitetura de software
- MVC(Model-View-Controller)

# Estrutura 
/project
  /frontend
    /app
        Dockerfile        # Dockerfile para o front-end
        /src              # Código do React
        /public           # Arquivos públicos do React
        package.json      # Dependências do front-end
        package-lock.json
        docker-compose.yml
  /backend
    /app
        Dockerfile        # Dockerfile para o back-end (Flask)
        main.py           # Código do Flask
        requirements.txt  # Dependências do back-end
        docker-compose.yml
  docker-compose.yml  # Arquivo para orquestrar os containers
  Dockerfile

# Passo a Passo para rodar o Projeto Back-end
Passo 1: Instalar o Docker
Passo 2: Rodar o Projeto com Docker Compose
- Para iniciar: docker-compose up --build
- Para parar: docker-compose down
Passo 3: Testar a Aplicação
- docker logs matematicanavida
Para acessar Configurações de banco, projeto... no Docker.
- docker exec -it meu_postgres psql -U usuario meubanco
- Dentro do container do banco use: psql -U usuario meubanco para entrar no pronpt do banco.

# Link locall o Projeto
http://localhost:5000
http://localhost:4200

# Passo a passo front-end
- nvm install 18
- nvm use 18
- npm install -g @angular/cli
- npm install rxjs --save







