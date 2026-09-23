import sqlite3

connector = sqlite3.connect("clientes.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

cursor.execute(
    "INSERT INTO clientes (nome, email) VALUES (?, ?)",
    ("Maria", "maria@email.com")
)

connector.commit()

print("Cliente cadastrado com sucesso!")

connector.close()
