import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

nome = input("Produto que deseja alterar: ")
novo_preco = float(input("Novo preco: "))

cursor.execute(
    "UPDATE produtos SET preco = ? WHERE nome = ?",
    (novo_preco, nome)
)

connector.commit()

print("Produto atualizado.")

connector.close()
