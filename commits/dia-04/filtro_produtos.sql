CREATE TABLE produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
);

INSERT INTO produtos (nome, preco) VALUES
('Teclado', 150.00),
('Mouse', 80.00),
('Monitor', 900.00),
('Headset', 250.00);

SELECT *
FROM produtos
WHERE preco > 100
ORDER BY preco DESC;
