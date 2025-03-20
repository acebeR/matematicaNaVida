# Usar a imagem oficial do Python 3.9
FROM python:3.9-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar os arquivos de dependências
COPY ./app/requirements.txt /app/requirements.txt



# Instalar as dependências
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar o restante do código da aplicação
COPY ./ /app/

# Expor a porta do back-end (5000)
EXPOSE 5000

# Instalar Gunicorn para rodar o Flask em produção
RUN pip install gunicorn

# Rodar o servidor com Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]
