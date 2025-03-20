# Usar a imagem oficial do Node.js
FROM node:16

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos de dependência (package.json e package-lock.json) para o diretório de trabalho
COPY frontend/app/package.json frontend/app/package-lock.json /app/

# Instalar as dependências do front-end (incluindo TypeScript)
RUN npm install

# Copiar o código fonte (src)
COPY frontend/app/src /app/src

# Se você tiver um tsconfig.json, copie também
COPY frontend/app/tsconfig.json /app/tsconfig.json

# Se o seu projeto depende de arquivos públicos (como ícones ou imagens), copie a pasta public também (se aplicável)
# COPY frontend/app/public /app/public

# Compilar o código TypeScript (caso o TypeScript não seja automaticamente compilado no comando start)
RUN npx tsc

# Expor a porta que o front-end vai rodar (caso esteja usando o React)
EXPOSE 3000

# Comando para rodar o front-end (ajustado para projetos TypeScript)
CMD ["npm", "start"]
