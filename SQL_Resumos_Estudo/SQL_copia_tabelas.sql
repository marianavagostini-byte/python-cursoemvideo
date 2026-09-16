-- Criação e Cópia de Tabelas
CREATE TABLE nova_tabela (
    id INT PRIMARY KEY,
    nome VARCHAR(100)
);

-- Cópia de tabela com dados (Ponto atual do vídeo)
CREATE TABLE clientes_copia AS 
SELECT * FROM clientes;

-- Cópia apenas da estrutura
CREATE TABLE clientes_estrutura AS 
SELECT * FROM clientes WHERE 1 = 0;
