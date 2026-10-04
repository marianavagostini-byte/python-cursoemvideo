CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente TEXT NOT NULL,
    valor REAL NOT NULL
);

INSERT INTO pedidos (cliente, valor) VALUES
('Ana', 100.00),
('Ana', 250.00),
('Carlos', 80.00),
('Carlos', 120.00),
('Mariana', 500.00);

SELECT cliente, SUM(valor) AS total
FROM pedidos
GROUP BY cliente
HAVING SUM(valor) > 200
ORDER BY total DESC;
