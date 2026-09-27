import sqlite3

connector = sqlite3.connect("vendas.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    valor REAL NOT NULL
)
""")

cursor.executemany(
    "INSERT INTO vendas (produto, valor) VALUES (?, ?)",
    [
        ("Notebook", 3500.00),
        ("Mouse", 120.00),
        ("Teclado", 150.00)
    ]
)

connector.commit()

cursor.execute("SELECT SUM(valor) FROM vendas")

total = cursor.fetchone()[0]

print(f"Total das vendas: R")

connector.close()
