import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.Preparação e Merge de Dados
try:
    dados = pd.read_csv('03.BaseDPEvolucaoMensalCisp.csv', sep=';', encoding='iso-8859-1')

    dp = pd.read_csv('08.DP.csv', sep=',', encoding='utf-8')
 
    df_comDP = dados.merge(dp, left_on='cisp',right_on='codDP', how='left')

    print(f'colums do df_comDP: {df_comDP.columns}')

    df_roubo = df_comDP[['cisp', 'roubo_celular', 'nome', 'roubo_transeunte', 'regiao', 'ano']]
    
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit(1)

# 2.Diagnóstico estatístico
try:
       
    df_roubo_regiao = df_roubo.groupby('regiao')[['roubo_celular', 'nome','roubo_transeunte']].sum().reset_index().sort_values(by='roubo_celular', ascending=False)

    # df_roubo_transeunte = df_roubo.groupby('regiao')[['roubo_celular','roubo_transeunte']].sum().reset_index().sort_values(by='roubo_transeunte', ascending=False)
 
    print (f' --- Roubo de Celular, DP e Transeunte por Região --- \n{df_roubo_regiao}')
    # print (f' --- Roubo de Transeunte por Região --- \n{df_roubo_transeunte}')    

except Exception as e:
    print(f'Erro ao analisar os dados: {e}')

# Medidas de tendência central

# Tendências central para roubo de celular 
media_celular = df_roubo['roubo_celular'].mean()
# mediana_celular = df_roubo['roubo_celular'].median()
moda_celular = df_roubo['roubo_celular'].mode()[0]

# Tendências central para roubo de transeuntes
media_transeunte = df_roubo['roubo_transeunte'].mean()
# mediana_transeunte = df_roubo['roubo_transeunte'].median()
moda_transeunte = df_roubo['roubo_transeunte'].mode()[0]

# medidas de dispersão
variancia_celular = df_roubo['roubo_celular'].var()
desvio_celular = df_roubo['roubo_celular'].std()
cv_celular = desvio_celular / media_celular * 100

variancia_transeunte = df_roubo['roubo_transeunte'].var()
desvio_transeunte = df_roubo['roubo_transeunte'].std()
cv_transeunte = desvio_transeunte / media_transeunte * 100

# Posição e limites
min_celular = df_roubo['roubo_celular'].min()
max_celular = df_roubo['roubo_celular'].max()
amplitude_celular = max_celular - min_celular
q1_celular = df_roubo['roubo_celular'].quantile(0.25)
q2_celular = df_roubo['roubo_celular'].quantile(0.50)
q3_celular = df_roubo['roubo_celular'].quantile(0.75)
limite_inferior_celular = q1_celular - 1.5 * (q3_celular - q1_celular)
limite_superior_celular = q3_celular + 1.5 * (q3_celular - q1_celular)
iqr_celular = q3_celular - q1_celular

min_transeunte = df_roubo['roubo_transeunte'].min()
max_transeunte = df_roubo['roubo_transeunte'].max()
amplitude_transeunte = max_transeunte - min_transeunte
q1_transeunte = df_roubo['roubo_transeunte'].quantile(0.25)
q2_transeunte = df_roubo['roubo_transeunte'].quantile(0.50)
q3_transeunte = df_roubo['roubo_transeunte'].quantile(0.75)
limite_inferior_transeunte = q1_transeunte - 1.5 * (q3_transeunte - q1_transeunte)
limite_superior_transeunte = q3_transeunte + 1.5 * (q3_transeunte - q1_transeunte)
iqr_transeunte = q3_transeunte - q1_transeunte

# Formato da distribuição
skewness_celular = df_roubo['roubo_celular'].skew()
kurtosis_celular = df_roubo['roubo_celular'].kurtosis()

skewness_transeunte = df_roubo['roubo_transeunte'].skew()
kurtosis_transeunte = df_roubo['roubo_transeunte'].kurtosis()

# Análise de Deslocamento
delta_celular = media_celular - q2_celular

delta_transeunte = media_transeunte - q2_transeunte


# Resultados
print(f' --- Análise Estatística de Roubo de Celular --- ')
print(f'Roubo de Celular - Média: {media_celular:.2f}')
# print(f'Roubo de Celular - Mediana: {mediana_celular}')
print(f'Roubo de Celular - Moda: {moda_celular}')
print(f'Roubo de Celular - Variância: {variancia_celular:.2f}')
print(f'Roubo de Celular - Desvio Padrão: {desvio_celular:.2f}')
print(f'Roubo de Celular - Coeficiente de Variação: {cv_celular:.2f}%')
print(f'Roubo de Celular - Mínimo: {min_celular}')
print(f'Roubo de Celular - Máximo: {max_celular}')
print(f'Roubo de Celular - Amplitude: {amplitude_celular}')
print(f'Roubo de Celular - Q1: {q1_celular}')
print(f'Roubo de Celular - Mediana (Q2): {q2_celular}')
print(f'Roubo de Celular - Q3: {q3_celular}')
print(f'Roubo de Celular - Limite Inferior: {limite_inferior_celular:.2f}')
print(f'Roubo de Celular - Limite Superior: {limite_superior_celular:.2f}')
print(f'Roubo de Celular - IQR: {iqr_celular:.2f}')
print(f'Roubo de Celular - Skewness: {skewness_celular:.2f}')
print(f'Roubo de Celular - Kurtosis: {kurtosis_celular:.2f}')
print(f'Roubo de Celular - Delta (Média - Mediana): {delta_celular:.2f}\n')

print(f' O Delta para roubo de celular é de 5.97, indicando que está acima da mediana em alguns períodos. Portanto, aguns meses tiveram número de roubos de celular significativamente maior do que o padrão, sugerindo a presença de meses com picos elevados de roubos.')



print(f' --- Análise Estatística de Roubo de Transeunte --- ')
print(f'Roubo de Transeunte - Média: {media_transeunte:.2f}')
# print(f'Roubo de Transeunte - Mediana: {mediana_transeunte}')
print(f'Roubo de Transeunte - Moda: {moda_transeunte}')
print(f'Roubo de Transeunte - Variância: {variancia_transeunte:.2f}')
print(f'Roubo de Transeunte - Desvio Padrão: {desvio_transeunte:.2f}')
print(f'Roubo de Transeunte - Coeficiente de Variação: {cv_transeunte:.2f}%')
print(f'Roubo de Transeunte - Mínimo: {min_transeunte}')
print(f'Roubo de Transeunte - Máximo: {max_transeunte}')
print(f'Roubo de Transeunte - Amplitude: {amplitude_transeunte}')
print(f'Roubo de Transeunte - Q1: {q1_transeunte}')
print(f'Roubo de Transeunte - Mediana (Q2): {q2_transeunte}')
print(f'Roubo de Transeunte - Q3: {q3_transeunte}')
print(f'Roubo de Transeunte - Limite Inferior: {limite_inferior_transeunte:.2f}')
print(f'Roubo de Transeunte - Limite Superior: {limite_superior_transeunte:.2f}')
print(f'Roubo de Transeunte - IQR: {iqr_transeunte:.2f}')
print(f'Roubo de Transeunte - Skewness: {skewness_transeunte:.2f}')
print(f'Roubo de Transeunte - Kurtosis: {kurtosis_transeunte:.2f}')
print(f'Roubo de Transeunte - Delta (Média - Mediana): {delta_transeunte:.2f}')

print(f'O Delta de 23,94 para roubo de transeuntes indica que a média está bem acima da mediana, sugerindo a presença de meses com ocorrências significativamente mais altas que o padrão, o que evidencia picos de criminalidade ao longo do período analisado.')

# 3.identificação de Anomalias(Outliers)

try:
    dp_roubo_celular = df_roubo[df_roubo['roubo_celular'] > limite_superior_celular]
    dp_roubo_transeunte = df_roubo[df_roubo['roubo_transeunte'] > limite_superior_transeunte]

    print(dp_roubo_celular)
    print(dp_roubo_transeunte)

except Exception as e: 
    print(f'Erro ao identificar anomalias: {e}')

# 4.Visualização de Dados
try:
    plt.subplots(2, 2, figsize=(16, 7))
    plt.suptitle('Análise de Roubos', fontsize=16)

    # primeiro grafico -> por ano (linha)
    plt.subplot(2, 2, 1)
    plt.plot(df_roubo['regiao'].astype(str),df_roubo_regiao['roubo_celular'],marker='o', color='red', linestyle='--',linewidth=2)
    plt.xticks(rotation=45)

    # segundo grafico -> por regiao (barra)
    plt.subplot(2, 2, 2)
    plt.bar(df_roubo_regiao['regiao'], df_roubo_regiao['roubo_transeunte'])
    
    # terceiro grafico -> boxplot
    plt.subplot(2, 2, 3)
    plt.boxplot(df_roubo['roubo_celular'], showmeans=True, showfliers=True)
    
    # quarto quadrante -> boxplot sem outliers
    plt.subplot(2, 2, 4)
    plt.boxplot(df_roubo['roubo_transeunte'], showmeans=True, showfliers=False)
   
    plt.tight_layout()
    plt.show()
except Exception as e:
    print(f'Erro na vizualização de dados: {e}')