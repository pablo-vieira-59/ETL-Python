import pandas as pd
import cx_Oracle

def load_local(l: list):
    for i in range(0, len(l)):
        comando = "insert into dm_local values(:1, :2, :3, :4)"
        try:
            cursor_dw.execute(comando, (l[i][0], l[i][1], l[i][2], l[i][3]))
        except:
            print('Erro: Load Local - ' + l[i][1])
            continue
    print('Load Local Concluido')

def load_tempo(l: list):
    for i in range(0, len(l)):
        comando = "insert into dm_tempo values(:1, :2, :3, :4)"
        try:
            cursor_dw.execute(comando, (l[i][0], l[i][1], l[i][2], l[i][3]))
        except:
            print('Erro: Load Tempo - ' + l[i][0])
            continue
    print('Load Tempo Concluido')

def load_dados(l: list):
    for i in range(0, len(l)):
        comando = "insert into ft_dados values(:1, :2, :3, :4)"
        try:
            cursor_dw.execute(comando, (l[i][0], l[i][1], l[i][2], l[i][3]))
        except:
            print('Erro: Load Dados - ' + l[i][0] + ' - ' + l[i][1])
            continue
    print('Load Dados Concluido')

dados = pd.read_csv('Dados.csv')
dados.columns = ['id_mun','nom_mun','uf','regiao','qnt_ben','valor','anomes','semestre','trimestre','bimestre']

dados_dm_local = (dados.groupby(['id_mun','nom_mun','uf','regiao']).size()).get_values
dados_dm_tempo = (dados.groupby(['anomes','semestre','trimestre','bimestre']).size()).get_values
dados_ft_dados = (dados[['id_mun','anomes','qnt_ben','valor']]).get_values

# Criando Conexões com os Bancos
# Param 1 = db_username
# Param 2 = db_password
# Param 3 = database_address:service_port
dw = cx_Oracle.connect('bolsafamilia', 'bolsafamilia', 'localhost:1521/XE')

# Definindo Cursores para fazer Queries
cursor_dw = dw.cursor()

# Reset das Tabelas
cursor_dw.execute('delete from ft_dados')
cursor_dw.execute('delete from dm_local')
cursor_dw.execute('delete from dm_tempo')
dw.commit()

# Processo de Load
load_local(dados_dm_local)
load_tempo(dados_dm_tempo)
load_dados(dados_ft_dados)
dw.commit()