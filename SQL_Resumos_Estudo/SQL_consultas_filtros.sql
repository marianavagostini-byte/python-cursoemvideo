-- Consultas Básicas e Filtros (SELECT e WHERE)
SELECT coluna1, coluna2 FROM tabela;
SELECT * FROM tabela;

SELECT * FROM produtos WHERE preco > 50 AND categoria = 'Eletrônicos';
SELECT * FROM clientes WHERE cidade IN ('São Paulo', 'Rio de Janeiro');
SELECT * FROM funcionarios WHERE nome LIKE 'A%';

SELECT * FROM produtos ORDER BY preco DESC LIMIT 10;
