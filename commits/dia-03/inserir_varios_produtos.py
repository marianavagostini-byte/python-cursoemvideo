import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

produtos = [
    ("Mouse", 80.00),
    ("Teclado", 150.00),
    ("Monitor", 900.00)
]

cursor.executemany(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
    produtos
)

connector.commit()

print("Produtos cadastrados com sucesso!")

connector.close()
