import mysql.connector
from faker import Faker
from random import randint

# Conectar ao banco de dados MySQL
conexao = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="seu_banco_de_dados"
)

cursor = conexao.cursor()
fake = Faker()

# Populando a tabela Associado
for _ in range(10):
    cursor.execute("INSERT INTO associado (nome, sobrenome, idade, email) VALUES (%s, %s, %s, %s)",
                   (fake.first_name(), fake.last_name(), randint(18, 99), fake.email()))
    conexao.commit()

# Populando a tabela Conta
for _ in range(10):
    cursor.execute("INSERT INTO conta (tipo_conta, data_criacao, id_associado) VALUES (%s, %s, %s)",
                   (fake.word(), fake.date_this_decade(), randint(1, 10)))
    conexao.commit()

# Populando a tabela Cartao
for _ in range(10):
    cursor.execute("INSERT INTO cartao (num_cartao, nom_impresso, id_conta, id_associado) VALUES (%s, %s, %s, %s)",
                   (randint(1000, 9999), fake.name(), randint(1, 10), randint(1, 10)))
    conexao.commit()

# Populando a tabela Movimento
for _ in range(10):
    cursor.execute("INSERT INTO movimento (vlr_transacao, des_transacao, data_movimento, id_cartao) VALUES (%s, %s, %s, %s)",
                   (round(random.uniform(1, 1000), 2), fake.text(), fake.date_time_this_decade(), randint(1, 10)))
    conexao.commit()

# Fechar a conexão
cursor.close()
conexao.close()