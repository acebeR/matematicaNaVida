# Imagem base para o frontend - Node.js 16
FROM node:16

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências (package.json e package-lock.json) para o diretório de trabalho
COPY frontend/package.json frontend/package-lock.json /app/

# Instalar as dependências do frontend
RUN npm install

# Copiar todos os arquivos da pasta frontend/app/src para o diretório /app/src no container
COPY frontend/src /app/src

# Expor a porta em que o frontend vai rodar
EXPOSE 3000

# Comando para rodar o frontend
CMD ["npm", "start"]
