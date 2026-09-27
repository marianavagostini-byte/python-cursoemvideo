import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

busca = input("Digite o nome do produto: ")

cursor.execute(
    "SELECT id, nome, preco FROM produtos WHERE nome LIKE ?",
    (f"%{busca}%",)
)

produtos = cursor.fetchall()

for produto in produtos:
    print(f"{produto[1]} - R")

connector.close()
