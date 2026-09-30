import sqlite3

connector = sqlite3.connect("notas.db")
cursor = connector.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    nota REAL NOT NULL
)
""")

cursor.executemany(
    "INSERT INTO alunos (nome, nota) VALUES (?, ?)",
    [
        ("Ana", 8.5),
        ("Carlos", 6.5),
        ("Mariana", 9.0)
    ]
)

connector.commit()

cursor.execute("""
SELECT nome, nota
FROM alunos
WHERE nota >= 7
""")

for aluno in cursor.fetchall():
    print(f"{aluno[0]} - {aluno[1]}")

connector.close()
