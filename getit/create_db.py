import sqlite3

# Conecta ao SQLite (cria o banco de dados 'notes_db.db' se não existir)
conn = sqlite3.connect('notes_db.db')

# Cria um cursor
cursor = conn.cursor()

# Apaga a tabela 'notes' se já existir
cursor.execute("DROP TABLE IF EXISTS notes")

# Cria a tabela 'notes' no banco de dados 'notes_db'
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    detalhes TEXT,
    data_criacao TEXT,
    data_modificacao TEXT
)
""")

# Commita (salva) as mudanças
conn.commit()

# Fecha a conexão
conn.close()

print("Tabela 'notes' criada com sucesso em 'notes_db.db'")