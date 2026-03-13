import pandas as pd
import numpy as np 

# criar dados ficticios
# media = 33 // mediana = 21

dados = np.array([10, 25, 56, 8, 17, 12, 85, 49, 72, 1])

# 25% do todo
q1 = np.percentile(dados, 25) 

# 50% (mediana)
q2 = np.percentile(dados, 50)

# 75% de todo
q3 = np.percentile(dados, 75)

print(f'Primeiro Quartil (Q1 - mais rapidos): {q1}')
print(f'Segundo Quartil (Q2 - Mediana/Padrão): {q2}')
print(f'Terceiro Quartil (Q3 - Mais lentos): {q3}')

media = np.mean(dados)

delta_media_mediana = media - q2

print(f'Média: {media}')
print(f' Diferença entre média e mediana: {delta_media_mediana:,.2f}')