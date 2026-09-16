-- Manipulação de Dados (INSERT, UPDATE, DELETE)
INSERT INTO clientes (nome, email) VALUES ('Ana Souza', 'ana@email.com');

UPDATE clientes SET email = 'novo_email@email.com' WHERE id = 5;

DELETE FROM clientes WHERE id = 5;
