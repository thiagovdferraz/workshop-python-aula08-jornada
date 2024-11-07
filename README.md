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