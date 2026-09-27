import sqlite3

connector = sqlite3.connect("vendas_produtos.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

cursor.executemany(
    "INSERT INTO vendas (produto, quantidade) VALUES (?, ?)",
    [
        ("Mouse", 2),
        ("Mouse", 3),
        ("Teclado", 1),
        ("Teclado", 2)
    ]
)

connector.commit()

cursor.execute("""
SELECT produto, SUM(quantidade)
FROM vendas
GROUP BY produto
""")

for venda in cursor.fetchall():
    print(f"{venda[0]}: {venda[1]} unidades")

connector.close()
