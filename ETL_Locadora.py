from builtins import print
import cx_Oracle


class Artista:
    cdg_art = ''
    tpo_art = ''
    nac_bras = ''
    nom_art = ''

    def __init__(self, cdg, tpo, nac, nom):
        self.cdg_art = cdg
        self.tpo_art = tpo
        self.nac_bras = nac
        self.nom_art = nom

    def transform(self):
        if self.tpo_art == 'I':
            self.tpo_art = 'Artista Individual'
        elif self.tpo_art == 'D':
            self.tpo_art = 'Dupla'
        elif self.tpo_art == 'B':
            self.tpo_art = 'Banda'

        if self.nac_bras == 'V':
            self.nac_bras = 'Verdadeiro'
        elif self.nac_bras == 'F':
            self.nac_bras = 'Falso'


class Socio:
    id_soc = ''
    nom_soc = ''
    tpo_soc = ''

    def __init__(self, id, nom, tpo):
        self.id_soc = id
        self.nom_soc = nom
        self.tpo_soc = tpo


class Gravadora:
    id_grav = ''
    uf_grav = ''
    nac_bras = ''
    nom_grav = ''

    def __init__(self, id, uf, nac, nom):
        self.id_grav = id
        self.uf_grav = uf
        self.nac_bras = nac
        self.nom_grav = nom

    def transform(self):
        if self.nac_bras == 'V':
            self.nac_bras = 'Verdadeiro'
        elif self.nac_bras == 'F':
            self.nac_bras = 'Falso'


class Titulo:
    id_tit = ''
    tpo_tit = ''
    cla_tit = ''
    dsc_tit = ''

    def __init__(self, id, tpo, cla, dsc):
        self.id_tit = id
        self.tpo_tit = tpo
        self.cla_tit = cla
        self.dsc_tit = dsc

    def transform(self):
        if self.tpo_tit == 'D':
            self.tpo_tit = 'DVD'
        elif self.tpo_tit == 'C':
            self.tpo_tit = 'CD'

        if self.cla_tit == 'N':
            self.cla_tit = 'Normal'
        elif self.cla_tit == 'P':
            self.cla_tit = 'Promocional'
        elif self.cla_tit == 'L':
            self.cla_tit = 'Lancamento'


class Tempo:
    id_tmp = ''
    nu_ano = ''
    nu_mes = ''
    nu_anomes = ''
    sg_mes = ''
    nm_mesano = ''
    nm_mes = ''
    nu_dia = ''
    dt_tempo = ''
    nu_hora = ''
    turno = ''

    def __init__(self, id, nu_ano, nu_mes, sg_mes, nm_mes, nu_dia, data, nu_hora, turno):
        self.id_tmp = id
        self.nu_ano = nu_ano
        self.nu_mes = nu_mes
        self.nu_anomes = str(nu_ano) + str(nu_mes)
        self.sg_mes = sg_mes
        self.nm_mesano = str(nm_mes) + str(nu_ano)
        self.nm_mes = nm_mes
        self.nu_dia = nu_dia
        self.dt_tempo = data
        self.nu_hora = nu_hora
        self.turno = turno


class Locacao:
    id_soc = ''
    id_tit = ''
    id_art = ''
    id_grav = ''
    id_tmp = ''
    vlr_arr = ''
    tmp_dev = ''
    mlt_atr = ''

    def __init__(self, id_soc, id_tit, id_art, id_grav, id_tmp, vlr_arr, tmp_dev, val_uni, qnt_atr):
        self.id_soc = id_soc
        self.id_tit = id_tit
        self.id_art = id_art
        self.id_grav = id_grav
        self.id_tmp = id_tmp
        self.vlr_arr = vlr_arr + self.calcular_atraso(val_uni, qnt_atr)
        self.tmp_dev = tmp_dev
        self.mlt_atr = self.calcular_atraso(val_uni, qnt_atr)

    def calcular_atraso(self, val_uni, qnt_atr):
        atraso = 0
        if qnt_atr >= 1 :
            atraso = val_uni + ((0.3*val_uni)*(qnt_atr-1))
        return atraso


def extract_socios():
    cursor_logico.execute('select cod_soc, nom_soc, dsc_tps from socios join tipos_socios using(cod_tps)')
    linhas = cursor_logico.fetchall()
    socios = []
    for i in range(0, len(linhas)):
        linha = list(linhas[i])
        soc = Socio(linha[0], linha[1], linha[2])
        socios.append(soc)
    print("Extract Socios Concluido")
    return socios


def extract_artistas():
    cursor_logico.execute('select cod_art, tpo_art, nac_bras, nom_art from artistas')
    linhas = cursor_logico.fetchall()
    artistas = []
    for i in range(0, len(linhas)):
        linha = list(linhas[i])
        art = Artista(linha[0], linha[1], linha[2], linha[3])
        art.transform()
        artistas.append(art)
    print("Extract Artistas Concluido")
    print("Transform Artistas Concluido")
    return artistas


def extract_gravadoras():
    cursor_logico.execute('select cod_grav, uf_grav, nac_bras, nom_grav from gravadoras')
    linhas = cursor_logico.fetchall()
    gravadoras = []
    for i in range(0, len(linhas)):
        linha = list(linhas[i])
        grv = Gravadora(linha[0], linha[1], linha[2], linha[3])
        grv.transform()
        gravadoras.append(grv)
        #print(linha)
    print("Extract Gravadoras Concluido")
    return gravadoras


def extract_titulos():
    cursor_logico.execute('select cod_tit, tpo_tit, cla_tit, dsc_tit from titulos')
    linhas = cursor_logico.fetchall()
    titulos = []
    for i in range(0, len(linhas)):
        linha = list(linhas[i])
        tit = Titulo(linha[0], linha[1], linha[2], linha[3])
        tit.transform()
        titulos.append(tit)
    print("Extract Titulos Concluido")
    return titulos


def extract_tempo():
    querie = "select distinct EXTRACT (year from dat_loc), EXTRACT (month from dat_loc), TO_CHAR(ADD_MONTHS(dat_loc, 1),'mon'), TO_CHAR(dat_loc, 'mon'), EXTRACT (day from dat_loc), dat_loc, TO_CHAR(dat_loc,'HH24'), TO_CHAR(dat_loc,'AM') from locacoes"
    cursor_logico.execute(querie)
    linhas = cursor_logico.fetchall()
    tempos = []
    codigo = 1
    for i in range(0, len(linhas)):
        linha = list(linhas[i])
        tmp = Tempo(codigo, linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6], linha[7])
        tempos.append(tmp)
        codigo += 1
    print("Extract Tempos Concluido")
    return tempos


def extract_locacao():
    querie = "select cod_soc, cod_tit,cod_art, cod_grav, dat_loc, locacoes.val_loc, nvl((dat_dev - dat_loc), 0), itens_locacoes.val_loc, nvl((dat_dev - dat_prev), 0) from locacoes join itens_locacoes using(cod_soc, dat_loc) join titulos using(cod_tit)"
    cursor_logico.execute(querie)
    linhas = cursor_logico.fetchall()
    locacoes = []
    for i in range(0, len(linhas)):
        linha = list(linhas[i])
        data = linha[4]
        cursor_dw.execute("select id_tempo from dm_tempo where dt_tempo = :1", [data])
        id_data = cursor_dw.fetchall()
        loc = Locacao(linha[0], linha[1], linha[2], linha[3], id_data[0][0], linha[5], linha[6], linha[7], linha[8])
        locacoes.append(loc)
    print("Extract Locacoes Concluido")
    return locacoes


def load_socios(s: list):
    for i in range(0, len(s)):
        comando = 'insert into dm_socio values(:1, :2, :3)'
        try:
            cursor_dw.execute(comando, (s[i].id_soc, s[i].nom_soc, s[i].tpo_soc))
        except:
            print('Erro : Load Socios')
            continue
    print('Load Socios Concluido')


def load_artistas(a: list):
    for i in range(0, len(a)):
        comando = 'insert into dm_artista values(:1, :2, :3, :4)'
        try:
            cursor_dw.execute(comando, (a[i].cdg_art, a[i].tpo_art, a[i].nac_bras, a[i].nom_art))
        except:
            print('Erro : Load Artistas')
            continue
    print('Load Artistas Concluido')


def load_gravadoras(g: list):
    for i in range(0, len(g)):
        comando = "insert into dm_gravadora values(:1, :2, :3, :4)"
        try:
            cursor_dw.execute(comando, (g[i].id_grav, g[i].uf_grav, g[i].nac_bras, g[i].nom_grav))
        except:
            print('Erro : Load Gravadoras')
            continue
    print('Load Gravadoras Concluido')


def load_titulos(t: list):
    for i in range(0, len(t)):
        comando = "insert into dm_titulo values(:1, :2, :3, :4)"
        try:
            cursor_dw.execute(comando, (t[i].id_tit, t[i].tpo_tit, t[i].cla_tit, t[i].dsc_tit))
        except:
            print('Erro : Load Titulos')
            continue
    print('Load Titulos Concluido')


def load_tempo(t: list):
    for i in range(0, len(t)):
        comando = "insert into dm_tempo values(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
        cursor_dw.execute(comando, (t[i].id_tmp, t[i].nu_ano, t[i].nu_mes, t[i].nu_anomes, t[i].sg_mes, t[i].nm_mesano, t[i].nm_mes, t[i].nu_dia, t[i].dt_tempo, t[i].nu_hora, t[i].turno))
    print('Load Tempo Concluido')


def load_locacao(l: list):
    for i in range(0, len(l)):
        comando = "insert into ft_locacoes values(:1, :2, :3, :4, :5, :6, :7, :8)"
        cursor_dw.execute(comando, (l[i].id_soc, l[i].id_tit, l[i].id_art, l[i].id_grav, l[i].id_tmp, l[i].vlr_arr, l[i].tmp_dev, l[i].mlt_atr))
    print('Load Locacoes Concluido')


# Criando Conexões com os Bancos
# Param 1 = db_username
# Param 2 = db_password
# Param 3 = database_address:service_port
dw = cx_Oracle.connect('dw_locadora', 'dw_locadora', 'localhost:1521/XE')
logico = cx_Oracle.connect('locadora', 'locadora', 'localhost:1521/XE')

# Definindo Cursores para fazer Queries
cursor_dw = dw.cursor()
cursor_logico = logico.cursor()

# Reset das Tabelas
cursor_dw.execute('delete from ft_locacoes')
cursor_dw.execute('delete from dm_artista')
cursor_dw.execute('delete from dm_socio')
cursor_dw.execute('delete from dm_gravadora')
cursor_dw.execute('delete from dm_titulo')
cursor_dw.execute('delete from dm_tempo')
dw.commit()

# Processo de ETL da Dimensão de Socios
socios = extract_socios()
load_socios(socios)
dw.commit()
socios = []

# Processo de ETL da Dimensão de Gravadoras
gravadoras = extract_gravadoras()
load_gravadoras(gravadoras)
dw.commit()
gravadoras = []

# Processo de ETL da Dimensão de Artistas
artistas = extract_artistas()
load_artistas(artistas)
dw.commit()
artistas = []

# Processo de ETL da Dimensão de Titulos
titulos = extract_titulos()
load_titulos(titulos)
dw.commit()
titulos = []

# Processo de ETL da Dimensão de Tempo
tempos = extract_tempo()
load_tempo(tempos)
dw.commit()
tempos = []

# Processo de ETL dos Fatos Locacoes
locacoes = extract_locacao()
load_locacao(locacoes)
dw.commit()
locacoes = []
