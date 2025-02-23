# Importa os módulos necessários do Flask e outros pacotes
from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql  # Para conexão com banco SQLite
from datetime import datetime  # Para manipulação de datas

# Cria uma instância do Flask, especificando a pasta de templates
app = Flask(__name__, template_folder='static/templates')

# Configura o diretório de arquivos estáticos (CSS, JS, imagens)
app.static_folder = 'static'

# Função helper para criar conexão com o banco de dados
def get_db():
    conn = sql.connect('notes_db.db')  # Conecta ao arquivo do banco
    conn.row_factory = sql.Row  # Configura resultados como dicionários
    return conn

# Rota principal que lista todas as notas
@app.route("/")
@app.route("/notes")  # Duas URLs apontam para mesma função
def list_notes():
    # Abre conexão com banco
    conn = get_db()
    # Cria cursor para executar queries
    cur = conn.cursor()
    # Busca todas as notas
    cur.execute("SELECT * FROM notes")
    # Obtém resultados
    notes = cur.fetchall()
    # Fecha conexão
    conn.close()
    # Renderiza template com as notas
    return render_template("notes.html", notes=notes)

# Rota para adicionar nova nota via método POST
@app.route("/add_note", methods=['POST'])
def add_note():
    if request.method == 'POST':
        conn = get_db()
        cur = conn.cursor()
        # Insere nova nota com título, detalhes e timestamps
        cur.execute("""
            INSERT INTO notes (titulo, detalhes, data_criacao, data_modificacao)
            VALUES (?, ?, ?, ?)
        """, (
            request.form['titulo'],  # Título do form
            request.form['detalhes'],  # Detalhes do form
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Data atual
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Data atual
        ))
        conn.commit()
        conn.close()
        return redirect(url_for('list_notes'))

    return render_template("add_note.html")

# Rota para editar nota existente, aceita GET e POST
@app.route("/edit_note/<int:id>", methods=['GET', 'POST'])
def edit_note(id):
    if request.method == 'POST':
        conn = get_db()
        cur = conn.cursor()
        # Atualiza nota existente com novos dados
        cur.execute("""
            UPDATE notes 
            SET titulo=?, detalhes=?, data_modificacao=?
            WHERE id=?
        """, (
            request.form['titulo'],  # Novo título
            request.form['detalhes'],  # Novos detalhes
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # Data atual
            id  # ID da nota
        ))
        conn.commit()

        conn.close()

        return redirect(url_for('list_notes'))
    
    # Para GET, busca dados da nota para exibir no form
    conn = get_db()
    cur = conn.cursor()
    # Busca nota pelo ID
    cur.execute("SELECT * FROM notes WHERE id=?", (id,))
    # Obtém primeira (única) nota
    note = cur.fetchone()
    conn.close()

    return render_template("edit_note.html", note=note)

# Rota para deletar nota pelo ID
@app.route("/delete_note/<int:id>")
def delete_note(id):
    conn = get_db()
    cur = conn.cursor()
    # Remove nota pelo ID
    cur.execute("DELETE FROM notes WHERE id=?", (id,))
    conn.commit()

    conn.close()

    return redirect(url_for('list_notes'))

# Handler para erro 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Inicia servidor Flask em modo desenvolvimento
if __name__ == '__main__':
    # Debug ativo e porta 5001
    app.run(debug=True, port=5001)