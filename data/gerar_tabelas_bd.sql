-- Tabela Associado
CREATE TABLE associado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    sobrenome VARCHAR(255),
    idade INT,
    email VARCHAR(255)
);

-- Tabela Conta
CREATE TABLE conta (
    id INT PRIMARY KEY,
    tipo_conta VARCHAR(50),
    data_criacao TIMESTAMP,
    id_associado INT,
    FOREIGN KEY (id_associado) REFERENCES associado(id)
);

-- Tabela Cartao
CREATE TABLE cartao (
    id INT PRIMARY KEY,
    num_cartao INT,
    nom_impresso VARCHAR(100),
    id_conta INT,
    id_associado INT,
    FOREIGN KEY (id_conta) REFERENCES conta(id),
    FOREIGN KEY (id_associado) REFERENCES associado(id)
);

-- Tabela Movimento
CREATE TABLE movimento (
    id INT PRIMARY KEY,
    vlr_transacao DECIMAL(10,2),
    des_transacao VARCHAR(255),
    data_movimento TIMESTAMP,
    id_cartao INT,
    FOREIGN KEY (id_cartao) REFERENCES cartao(id)
);