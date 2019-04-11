import requests as rq
import pandas as pd

def get_regiao(id):
    if id >= 1 and id <= 17:
        return 'Norte'
    elif id >= 21 and id <= 29:
        return 'Nordeste'
    elif id >= 31 and id <= 35:
        return 'Sudeste'
    elif id >= 41 and id <= 43:
        return 'Sul'
    elif id >= 50 and id <= 53:
        return 'Centro-Oeste'

def get_semestre(vlr):
    if vlr <= 6:
        return 1
    elif vlr > 6:
        return 2

def get_bimestre(vlr):
    if vlr == 1 or vlr == 2:
        return 1
    elif vlr == 3 or vlr == 4:
        return 2
    elif vlr == 5 or vlr == 6:
        return 3
    elif vlr == 7 or vlr == 8:
        return 4
    elif vlr == 9 or vlr == 10:
        return 5
    elif vlr == 11 or vlr == 12:
        return 6

def get_trimestre(vlr):
    if vlr >= 1 and vlr <= 3:
        return 1
    if vlr >= 4 and vlr <= 6:
        return 2
    if vlr >= 7 and vlr <= 9:
        return 3
    if vlr >= 10 and vlr <= 12:
        return 4
    
url = 'http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/'
municipios = pd.read_excel('municipios.xls')
municipios = municipios.get_values()
municipios = municipios[5:5567,1:3].astype(str)

matriz = []
ano = 2016
for i in range(0,3):
    for j in range(1,13):
        mes = ''
        if j < 10:
            mes = '0' + str(j)
        else:
            mes = str(j)
        for k in range(0,len(municipios)):
            linha = []
            anomes = str(ano)+mes
            id_mun = municipios[k][0] + municipios[k][1]
            print(id_mun + ' : ' + anomes)
            params = dict(mesAno=anomes, codigoIbge=id_mun, pagina=1)
            resp = requests.get(url=url, params=params)
            resp = resp.json()
            resp = resp[0]
            valor = resp['valor']
            qnt_ben = resp['quantidadeBeneficiados']
            uf = resp['municipio']['uf']['sigla']
            nome_mun = resp['municipio']['nomeIBGE']
            regiao = get_regiao(int(municipios[k][0]))
            semestre = get_semestre(int(mes))
            bimestre = get_bimestre(int(mes))
            trimestre = get_trimestre(int(mes))
            linha = [id_mun, nome_mun, uf, regiao, qnt_ben, valor, anomes, semestre, trimestre, bimestre]
            matriz.append(linha)
    ano += 1


dados = pd.DataFrame(matriz, columns=['id_mun','nom_mun','uf','regiao','qnt_ben','valor','anomes','semestre','trimestre','bimestre'])
dados.to_csv('Dados.csv',index=False, header=False)

