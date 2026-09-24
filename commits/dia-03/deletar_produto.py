import sqlite3

connector = sqlite3.connect("estoque.db")
cursor = connector.cursor()

cursor.execute(
    "DELETE FROM produtos WHERE nome = ?",
    ("Mouse",)
)

connector.commit()

print("Produto removido com sucesso!")

cursor.execute("SELECT * FROM produtos")

for produto in cursor.fetchall():
    print(produto)

connector.close()
