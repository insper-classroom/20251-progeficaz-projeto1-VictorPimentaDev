import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Lê o arquivo HTML e retorna a string:
def load_template(filename_template):
    # Monta o caminho para o arquivo HTML:
    file_path = os.path.join("static", "templates", filename_template)  

    # Abre o arquivo no modo leitura
    with open(file_path, "r", encoding="utf-8") as file:        
        # Retorna o conteúdo do arquivo como string:
        return file.read()                                      

# Define a classe Note, que herda de db.Model
class Note(db.Model):
    # Coluna 'id': chave primária do tipo Integer
    id = db.Column(db.Integer, primary_key=True)

    # Coluna 'titulo': String de tamanho máximo 100
    titulo = db.Column(db.String(100))

    # Coluna 'detalhes': Text para textos longos
    detalhes = db.Column(db.Text)

    # Coluna 'data_criacao': String de tamanho máximo 20
    data_criacao = db.Column(db.String(20))

    # Coluna 'data_modificacao': String de tamanho máximo 20
    data_modificacao = db.Column(db.String(20))

    # Coluna 'pensamentos': Text
    pensamentos = db.Column(db.Text)

    # Coluna 'pensamentos_rapidos': Text
    pensamentos_rapidos = db.Column(db.Text)