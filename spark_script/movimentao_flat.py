from pyspark.sql import SparkSession

# Configuração do Spark
with SparkSession.builder \
    .appName("MySQL to CSV") \
    .config("spark.jars", "./jars/mssql-jdbc-9.2.1.jre8.jar") \
    .getOrCreate() as spark:

    # Configurações do MySQL
    mysql_options = {
        "url": "jdbc:mysql://mysql:3306/sicoop_bd",  # Alterado o host para o nome do serviço no Docker Compose
        "driver": "com.mysql.cj.jdbc.Driver",
        "dbtable": "sicoop_bd",
        "user": "sicoop",
        "password": "sicoop"
    }

    # Leitura das tabelas
    associado_df = spark.read.format("jdbc").options(**mysql_options).option("dbtable", "associado").load()
    conta_df = spark.read.format("jdbc").options(**mysql_options).option("dbtable", "conta").load()
    cartao_df = spark.read.format("jdbc").options(**mysql_options).option("dbtable", "cartao").load()
    movimento_df = spark.read.format("jdbc").options(**mysql_options).option("dbtable", "movimento").load()

    # Junção das tabelas
    result_df = movimento_df \
        .join(cartao_df, "id_cartao") \
        .join(conta_df, "id_conta") \
        .join(associado_df, "id_associado") \
        .select("nome", "sobrenome", "idade", "vlr_transacao", "data_movimento",
                "num_cartao", "nom_impresso", "data_criacao", "tipo_conta", "data_criacao_conta")

    # Salvar o resultado em um arquivo CSV
    output_path = "./data/movimento_flat.csv"
    result_df.write.csv(output_path, header=True, mode="overwrite")