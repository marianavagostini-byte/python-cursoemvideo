import sqlite3

connector = sqlite3.connect("empresa.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    departamento_id INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS departamentos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

cursor.execute(
    "INSERT INTO departamentos (nome) VALUES (?)",
    ("Tecnologia",)
)

departamento_id = cursor.lastrowid

cursor.execute(
    "INSERT INTO funcionarios (nome, departamento_id) VALUES (?, ?)",
    ("Mariana", departamento_id)
)

connector.commit()

cursor.execute("""
SELECT funcionarios.nome, departamentos.nome
FROM funcionarios
JOIN departamentos
ON funcionarios.departamento_id = departamentos.id
""")

for funcionario in cursor.fetchall():
    print(f"Funcionário: {funcionario[0]}")
    print(f"Departamento: {funcionario[1]}")

connector.close()
