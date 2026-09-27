import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

cursor.execute("SELECT id, nome, preco FROM produtos ORDER BY preco DESC")

for produto in cursor.fetchall():
    print(f"{produto[1]} - R")

connector.close()
