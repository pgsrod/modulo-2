import pandas as pd 

vendas = pd.read_csv('01.amazon_sales_dataset.csv')

print(*30'-')
print(vendas.columns)
print(vendas.dtypes)
print(vendas.info())

total_vendas = vendas['total_sales'].sum()

media_valores_vendas = vendas['total_sales'].mean()
venda_minima_valores = vendas['total_sales'].min()
venda_maxima_valores = vendas['total_sales'].max()

print('\n--- Resumo Executivo de Vendas ---')

print(f'1. Volume Total (Soma das Vendas): $ {total_vendas:,.2f}')
# Representa o tamanho total da nossa operação no período 

print(f'2. Gasto Médio: $ {media_valores_vendas:,.2f}')
#  valor esperado que um cliente gaste em média conosco

print(f'3. Maior Venda: $ {venda_maxima_valores:,.2f}')
# Nosso recorde de venda. Investigar o perfil do cliente.

print(f'4. Menor Venda: $ {venda_minima_valores:,.2f}')
# Menor valor vendido. Investigar se há anomalias ou fraude.