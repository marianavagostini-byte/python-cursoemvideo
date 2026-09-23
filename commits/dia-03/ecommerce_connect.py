import sqlite3

connector = sqlite3.connect("ecommerce.db")
cursor = connector.cursor()

# Criação da tabela com os parênteses corretos no final
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        valor_venda NUMERIC NOT NULL,
        cliente_id INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
    )
"""
)

# Inserção de dados corrigida
cursor.execute(
    "INSERT INTO vendas (valor_venda, cliente_id) VALUES (?, ?)", (150.00, 1)
)
connector.commit()

# Consulta com o nome da coluna correto (cliente_id)
cursor.execute(
    """
    SELECT * FROM vendas v 
    JOIN clientes c ON v.cliente_id = c.id
"""
)

vendas = cursor.fetchall()
print(vendas)
connector.close()