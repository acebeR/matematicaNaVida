# main.py

from api import app  # Importa o aplicativo do arquivo api.py

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')  # Inicia o Flask, ouvindo em todas as interfaces (0.0.0.0)
