import polars as pl

arquivo_info = 'Music Info.csv'
arquivo_user = 'User Listening History.csv'

try:
    df_info = pl.read_csv(arquivo_info)
    df_user = pl.read_csv(arquivo_user)

    print(df_info.glimpse())
    print(df_user.glimpse())


    df_merge = df_info.join(df_user, on='track_id', how='left')
    print(df_merge.head())
    print(df_merge.glimpse())


except Exception as e:
    print(f'Erro ao ler arquivos: {e}')