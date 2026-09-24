import sqlite3

connector = sqlite3.connect("vendas.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto TEXT NOT NULL,
    valor REAL NOT NULL,
    cliente_id INTEGER NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
""")

cursor.execute(
    "INSERT INTO clientes (nome) VALUES (?)",
    ("João",)
)

cliente_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO pedidos (produto, valor, cliente_id) VALUES (?, ?, ?)",
    ("Notebook", 3500.00, cliente_id)
)

connector.commit()

cursor.execute("""
SELECT clientes.nome, pedidos.produto, pedidos.valor
FROM clientes
JOIN pedidos ON clientes.id = pedidos.cliente_id
""")

pedidos = cursor.fetchall()

for pedido in pedidos:
    print(
        f"Cliente: {pedido[0]} | "
        f"Produto: {pedido[1]} | "
        f"Valor: R\"
    )

connector.close()
