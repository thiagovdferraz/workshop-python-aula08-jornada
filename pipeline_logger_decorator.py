from etl import pipeline_calcular_vendas_consolidada

pasta_argumento: str = 'data'
formato_de_saida: list = ['csv','parquet']

pipeline_calcular_vendas_consolidada(pasta_argumento, formato_de_saida)