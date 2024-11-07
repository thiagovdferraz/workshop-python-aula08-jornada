# workshop-python-aula08-jornada

## Primeiros passos
Ativar ambiente virtual

```
pyenv local 3.12.5
poetry init
poetry shell
```

## Objetivo:
* criar uma ETL
* leitura de arquivos (json)
* concatenar dataframes
* transformar dados
* decisão de saída: salva em csv e parquet

## Ferramentas de processamento
* pandas, polars, duckdb, spark, dask

## Ferramentas de qualidade
* Pydantic (linha a linha ou uma API)
* Pandera (SQL, Dataframe)

## Na prática
Adicionar via poetry
```
poetry add pandera pandas
```

* Adicionar arquivos json e criar etl.py
* sempre que formos trabalhar com parquet, tem que instalar o pyarrow ou fastparquet

```
poetry add fastparquet
```

* criar arquivo `__init__.py` dentro da pasta do projeto

# workshop-python-aula09-jornada

## Trabalhando com logger

A principal biblioteca de log para python é o [Logguru](https://github.com/Delgan/loguru).

```
poetry add loguru
```

Ondde tiver `print` no código, substitui por `logger.info`. Existem outros como o ``sentry`` e ``dynatrace``.

* Criar arquivo `utils_log.py` na raiz do projeto

```python
from loguru import logger
from sys import stderr

# Configuração do logger para exibir logs no stderr e salvar em arquivo, com filtragem e formatação específicas
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "meu_arquivo_de_logs.log",  # Arquivo onde os logs serão salvos
    format="{time} {level} {message} {file}",
    level="INFO"
)

# Exemplo de uso do logger
logger.info("Este é um log de informação.")
logger.error("Este é um log de erro.")
```

