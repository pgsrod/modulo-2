import polars as pl
from sqlalchemy import create_engine


# configuracao
PARQUET_PATH = r'dados_bronze/df_bf.parquet' 
TABELA = 'bolsa_familia' 
BATCH_SIZE = 100000
ENGINE_URL = ('mysql+pymysql://root:@localhost:3306/bolsa_familia')

# conexão
engine = create_engine(ENGINE_URL)

# leitura
print('Lendo arquivo parquet')
df = pl.read_parquet(PARQUET_PATH)

# escrita em batch (lote) no banco 
total = df.shape[0]
linhas = 0

for i, batch in enumerate(df.iter_slices(n_rows=BATCH_SIZE)): 
    batch_pd = batch.to_pandas()
    modo = 'replace' if i ==0 else 'append'
    batch_pd.to_sql(name=TABELA, con=engine, if_exists=modo, index=False)
    linhas += batch_pd.shape[0]
    percent = (linhas/total) * 100
    print(f'Lote {i+1} | {percent:.2f}%)')


print('Escrita Finalizada')