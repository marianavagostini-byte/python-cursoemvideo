-- Junções de Tabelas (JOIN)
SELECT pedidos.id, clientes.nome 
FROM pedidos 
INNER JOIN clientes ON pedidos.cliente_id = clientes.id;

SELECT clientes.nome, pedidos.id 
FROM clientes 
LEFT JOIN pedidos ON clientes.id = pedidos.cliente_id;
