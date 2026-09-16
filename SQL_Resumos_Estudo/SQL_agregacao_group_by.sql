-- Funções de Agregação e Agrupamento (GROUP BY)
SELECT COUNT(*), AVG(preco) FROM produtos;

SELECT categoria, SUM(preco) AS total_preco 
FROM produtos 
GROUP BY categoria 
HAVING SUM(preco) > 1000;
