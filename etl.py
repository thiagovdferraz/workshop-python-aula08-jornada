import pandas as pd
import glob
import os # para comunicar com sistema operacional, como os comandos do prompt

# uma função de extract que le e consolida os json

def extrair_dados_e_consolidar(pasta: str):
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# um função de transformação: criar campo vendas

def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df


# uma funcao que da load em csv ou parquet

def carregar_dados(df: pd.DataFrame, format_saida: list):
    """
    essa funcao define se o arquivo sera salvo em csv ou parquet ou os dois
    """
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv", index=False)
        if formato == 'csv':
            df.to_parquet("dados.parquet")


def pipeline_calcular_vendas_consolidada(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    print("")
    print("Salvando arquivos")
    carregar_dados(data_frame_calculado, formato_de_saida)


# if __name__ == '__main__':
#     pasta_argumento: str = 'data'
#     data_frame = extrair_dados_e_consolidar(pasta=pasta_argumento)
#     data_frame_calculado = calcular_kpi_total_vendas(data_frame)
#     formato_de_saida: list = ['csv','parquet']
#     print("")
#     print("Salvando arquivos")
#     carregar_dados(data_frame_calculado, formato_de_saida)