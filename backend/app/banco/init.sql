CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

INSERT INTO usuarios (nome, email) VALUES
('João', 'joao@example.com'),
('Maria', 'maria@example.com');
