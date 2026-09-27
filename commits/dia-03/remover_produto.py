import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

nome = input("Produto que deseja remover: ")

cursor.execute(
    "DELETE FROM produtos WHERE nome = ?",
    (nome,)
)

connector.commit()

print("Produto removido.")

connector.close()
