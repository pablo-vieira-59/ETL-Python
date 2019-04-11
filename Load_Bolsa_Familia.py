import pandas as pd

dados = pd.read_csv('Dados.csv')
dados.columns = ['id_mun','nom_mun','uf','regiao','qnt_ben','valor','anomes','semestre','trimestre','bimestre']

dados_dm_local = (dados.groupby(['id_mun','nom_mun','uf','regiao']).size()).get_values
dados_dm_tempo = (dados.groupby(['anomes','semestre','trimestre','bimestre']).size()).get_values
dados_ft_dados = (dados[['id_mun','anomes','qnt_ben','valor']]).get_values