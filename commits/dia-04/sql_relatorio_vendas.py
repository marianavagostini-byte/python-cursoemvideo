import sqlite3

conexao = sqlite3.connect(":memory:")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    valor REAL NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
)
""")

clientes = [
    (1, "Ana"),
    (2, "Carlos"),
    (3, "Mariana"),
    (4, "João")
]

pedidos = [
    (1, 1, 500.00),
    (2, 1, 300.00),
    (3, 2, 150.00),
    (4, 2, 250.00),
    (5, 3, 1000.00),
    (6, 4, 50.00)
]

cursor.executemany(
    "INSERT INTO clientes VALUES (?, ?)",
    clientes
)

cursor.executemany(
    "INSERT INTO pedidos VALUES (?, ?, ?)",
    pedidos
)

cursor.execute("""
SELECT
    clientes.nome,
    SUM(pedidos.valor) AS total_gasto
FROM clientes
INNER JOIN pedidos
    ON clientes.id = pedidos.cliente_id
GROUP BY clientes.id
HAVING total_gasto >= 500
ORDER BY total_gasto DESC
""")

resultados = cursor.fetchall()

for nome, total in resultados:
    print(f"{nome}: R$ {total:.2f}")

conexao.close()
