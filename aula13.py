import polars as pl
import datetime as dt
import pandas as pd

# para ler arquivos dentro de uma pasta no windows
import os

# limpar resíduos - garbage collector
import gc 

ENDERECO_DADOS = r'C:/Users/priscilla.goncalves/Documents/analise-dados/Analise_modulo2/venv/base/'

try:
    print(f'Obtendo arquivos')
    hora_inicio = dt.datetime.now()

    # lista de arquivos
    lista_arquivos = os.listdir(ENDERECO_DADOS)

    for arquivo in lista_arquivos:
        print(f'lendo arquivo: {arquivo}')
        
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=';', encoding = 'iso-8859-1')

        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=';', encoding='iso-8859-1')

        if 'df_bf' in locals():
            df_bf = pl.concat([df_bf, df])
        else:
            df_bf = df

        del df

    df_bf = df_bf.with_columns(pl.col("VALOR PARCELA").str.replace(',' , '.').cast(pl.Float64))
    df_bf.write_parquet('C:/Users/priscilla.goncalves/Documents/analise-dados/Analise_modulo2/dados_bronze/df_bf.parquet')

    gc.collect()
    hora_fim = dt.datetime.now()
    print(f'Tempo total: {hora_fim - hora_inicio}')

except Exception as e:
    print(f'Erro ao obter dados: {e}')