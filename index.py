import pandas as pd
dados = pd.read_csv("/content/drive/MyDrive/Programação paralela/dados.csv")

dados.head()

sorted(dados['UF'].unique())
sorted(dados['Sexo'].unique())
sorted(dados['Cor'].unique())

print('De %s até %s anos' % (dados.Idade.min(), dados.Idade.max()))
print('De %s até %s metros' % (dados['Altura'].min(), dados.Altura.max()))

dados['Sexo'].value_counts()
dados['Sexo'].value_counts(normalize = True) * 100

frequencia = dados['Sexo'].value_counts()
percentual = dados['Sexo'].value_counts(normalize = True) * 100

dist_freq_qualitativas = pd.DataFrame({'Frequencia': frequencia, 'Porcentagens (%)': percentual})
dist_freq_qualitativas
dist_freq_qualitativas.rename(index = {0: 'Masculino', 1: 'Feminino'}, inplace = True)
dist_freq_qualitativas.rename_axis('Sexo', axis= 'columns', inplace = True)
dist_freq_qualitativas
