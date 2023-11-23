import mysql.connector
from faker import Faker
from random import randint

# Configurações de conexão
config = {
    'user': 'sicoop',
    'password': 'sicoop',
    'host': 'mysql',
    'port': 3306,
    'database': 'sicoop_bd'
}

fake = Faker()

try:
    # Conectar ao servidor MySQL
    conexao = mysql.connector.connect(**config)

    # Iniciar transação
    conexao.start_transaction()

    cursor = conexao.cursor()

    # Populando a tabela Associado
    for _ in range(10):
        cursor.execute("INSERT INTO associado (nome, sobrenome, idade, email) VALUES (%s, %s, %s, %s)",
                       (fake.first_name(), fake.last_name(), randint(18, 99), fake.email()))

    # Populando a tabela Conta
    for _ in range(10):
        cursor.execute("INSERT INTO conta (tipo_conta, data_criacao, id_associado) VALUES (%s, %s, %s)",
                       (fake.word(), fake.date_this_decade(), randint(1, 10)))

    # Populando a tabela Cartao
    for _ in range(10):
        cursor.execute("INSERT INTO cartao (num_cartao, nom_impresso, id_conta, id_associado) VALUES (%s, %s, %s, %s)",
                       (randint(1000, 9999), fake.name(), randint(1, 10), randint(1, 10)))

    # Populando a tabela Movimento
    for _ in range(10):
        cursor.execute("INSERT INTO movimento (vlr_transacao, des_transacao, data_movimento, id_cartao) VALUES (%s, %s, %s, %s)",
                       (round(randint.uniform(1, 1000), 2), fake.text(), fake.date_time_this_decade(), randint(1, 10)))

    # Commit da transação
    conexao.commit()

except mysql.connector.Error as err:
    print(f"Erro: {err}")
    # Rollback da transação em caso de erro
    conexao.rollback()

finally:
    # Fechar a conexão
    if 'cursor' in locals():
        cursor.close()
    conexao.close()