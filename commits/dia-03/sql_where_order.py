import sqlite3

connector = sqlite3.connect("alunos.db")
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
        ("Carlos", 6.0),
        ("Mariana", 9.5),
        ("João", 7.0)
    ]
)

connector.commit()

cursor.execute("""
SELECT nome, nota
FROM alunos
WHERE nota >= 7
ORDER BY nota DESC
""")

alunos = cursor.fetchall()

for aluno in alunos:
    print(f"{aluno[0]} - Nota: {aluno[1]}")

connector.close()
