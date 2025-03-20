# Usar a imagem oficial do Python
FROM python:3.9-slim

# Definir diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos de dependências
COPY ./app/requirements.txt /app/requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o restante do código da aplicação
COPY ./app /app

# Expor a porta 5000 para acesso externo
EXPOSE 5000

# Definir o comando para rodar o Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]