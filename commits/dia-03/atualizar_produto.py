import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

cursor.execute(
    "UPDATE produtos SET preco = ? WHERE nome = ?",
    (120.00, "Mouse")
)

connector.commit()

print("Produto atualizado com sucesso!")

cursor.execute(
    "SELECT id, nome, preco FROM produtos WHERE nome = ?",
    ("Mouse",)
)

produto = cursor.fetchone()

print(produto)

connector.close()
