from pyspark.sql import SparkSession

# Configuração do Spark
spark = SparkSession.builder \
    .appName("MySQL to CSV") \
    .config("spark.jars", "./jars/mssql-jdbc-9.2.1.jre8.jar") \
    .getOrCreate()

# Configurações do MySQL
mysql_options = {
    "url": "jdbc:mysql://localhost:3309/sicoop_bd",
    "driver": "com.mysql.cj.jdbc.Driver",
    "dbtable": "sicoop_bd",
    "user": "sicoop",
    "password": "sicoop"
}

# Leitura das tabelas
associado_df = spark.read.format("jdbc"). \
    option("url", mysql_options["url"]). \
    option("dbtable", "associado"). \
    option("driver", mysql_options["driver"]). \
    option("user", mysql_options["user"]). \
    option("password", mysql_options["password"]).load()

conta_df = spark.read.format("jdbc"). \
    option("url", mysql_options["url"]). \
    option("dbtable", "conta"). \
    option("driver", mysql_options["driver"]). \
    option("user", mysql_options["user"]). \
    option("password", mysql_options["password"]).load()

cartao_df = spark.read.format("jdbc"). \
    option("url", mysql_options["url"]). \
    option("dbtable", "cartao"). \
    option("driver", mysql_options["driver"]). \
    option("user", mysql_options["user"]). \
    option("password", mysql_options["password"]).load()

movimento_df = spark.read.format("jdbc"). \
    option("url", mysql_options["url"]). \
    option("dbtable", "movimento"). \
    option("driver", mysql_options["driver"]). \
    option("user", mysql_options["user"]). \
    option("password", mysql_options["password"]).load()

# Junção das tabelas
result_df = movimento_df \
    .join(cartao_df, movimento_df["id_cartao"] == cartao_df["id"]) \
    .join(conta_df, cartao_df["id_conta"] == conta_df["id"]) \
    .join(associado_df, conta_df["id_associado"] == associado_df["id"]) \
    .select("nome", 
            "sobrenome", 
            "idade", 
            "vlr_transacao", 
            "data_movimento", 
            "num_cartao", 
            "nom_impresso", 
            "data_criacao", 
            "tipo_conta", 
            "data_criacao_conta")

# Salvar o resultado em um arquivo CSV
output_path = "./data/movimento_flat.csv"
result_df.write.csv(output_path, header=True, mode="overwrite")

# Encerrar a sessão do Spark
spark.stop()