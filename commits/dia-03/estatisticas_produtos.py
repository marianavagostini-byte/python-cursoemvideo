import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

cursor.execute("SELECT COUNT(*) FROM produtos")

quantidade = cursor.fetchone()[0]

cursor.execute("SELECT AVG(preco) FROM produtos")

media = cursor.fetchone()[0]

print(f"Quantidade de produtos: {quantidade}")
print(f"Preço médio: R\")

connector.close()
