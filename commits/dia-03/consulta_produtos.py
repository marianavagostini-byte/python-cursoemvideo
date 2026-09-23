import sqlite3

connector = sqlite3.connect("produtos.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

cursor.execute(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    ("Teclado", 150.00)
)

connector.commit()

cursor.execute("SELECT id, nome, preco FROM produtos")

produtos = cursor.fetchall()

for produto in produtos:
    print(produto)

connector.close()
