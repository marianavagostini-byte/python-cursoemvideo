import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

cursor.execute(
    "SELECT id, nome, preco FROM produtos WHERE preco > ?",
    (100,)
)

produtos = cursor.fetchall()

for produto in produtos:
    print(f"ID: {produto[0]} | Produto: {produto[1]} | Preço: R")

connector.close()
