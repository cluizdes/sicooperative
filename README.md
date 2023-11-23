# Projeto SiCooperative - ETL e Data Lake

Este projeto visa abordar os desafios da SiCooperative LTDA em relação à agregação de dados, criação de um Data Lake e a disponibilização automatizada desse processo usando Docker.

## Pré-requisitos

Antes de começar, certifique-se de ter o Docker e o Docker Compose instalados em sua máquina.

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Estrutura do Projeto

- **`gerar_tabelas_bd.sql`**: Arquivo SQL para criar a estrutura do banco de dados.
- **`gerar_dados.py`**: Script Python para inserir dados fictícios nas tabelas do banco de dados.
- **`movimento_flat.py`**: Script Python para realizar o ETL usando o Apache Spark.
- **`docker-compose.yml`**: Arquivo de configuração Docker Compose.
- **`requirements.txt`**: Arquivo de contendo os principais componentes.

## Executando o Projeto

1. Clone este repositório:

```bash
git clone git@github.com:cluizdes/sicooperative.git
cd sicooperative
```

2. Execute o Docker Compose:

```bash
docker-compose up -d
```
Este comando criará os contêineres necessários, iniciará o MySQL e o processo ETL.

## Estratégias de Design

Foi utilizado o banco de dados MySQL, o uso do Apache Spark para ETL, e Docker para conteneirizar a automatização.

## Possíveis Melhorias

Se tivesse mais tempo, consideraria as seguintes melhorias:

1. **Otimização de Desempenho**: Exploraria maneiras de otimizar o desempenho do ETL, especialmente para grandes volumes de dados.
2. **Segurança**: Implementaria medidas de segurança adequadas, como senhas criptografadas e conexões seguras.
3. **Logs e Monitoramento**: Adicionar logs e recursos de monitoramento para rastrear o desempenho e identificar possíveis problemas.
4. **Escalabilidade**: Avaliaria a escalabilidade do sistema para lidar com um aumento significativo no volume de dados.

## Dificuldades Encontradas

Não realizar o processo em um ambiente já estruturado em nuvem, realizar em pouco tempo.