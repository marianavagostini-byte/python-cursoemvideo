CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    produto TEXT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO clientes (nome) VALUES
('Ana'),
('Carlos'),
('Mariana');

INSERT INTO pedidos (cliente_id, produto) VALUES
(1, 'Teclado'),
(2, 'Mouse'),
(1, 'Monitor');

SELECT
    clientes.nome,
    pedidos.produto
FROM clientes
INNER JOIN pedidos
    ON clientes.id = pedidos.cliente_id;
