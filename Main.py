import pandas as pd
from ManipularDados import ManipularDados, CalcularIndicadores
from OrganizarPastas import OrganizarPastas

#Importando planilhas
caminho_baseDados = r'C:\Users\Renan\Desktop\AutomacaoIndicadores\Bases de Dados'
emails_df = pd.read_excel(rf'{caminho_baseDados}\Emails.xlsx')
lojas_df = pd.read_csv(rf'{caminho_baseDados}\Lojas.csv', sep=';', encoding='latin1')
vendas_df = pd.read_excel(rf'{caminho_baseDados}\Vendas.xlsx')

#Definindo dia do indicador a ser calculado e criando 1 planilha para cada loja
dia_indicador = ManipularDados().definir_dia_indicador(vendas_df)
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
dic_tabelas_lojas = ManipularDados().separar_por_loja(lojas_df, vendas_df)

#Criando pastas das lojas e colocando uma planilha de loja em sua respectiva pasta
caminho_backup = r'C:\Users\Renan\Desktop\AutomacaoIndicadores\Backup Arquivos Lojas'
OrganizarPastas().organizar_pastas(caminho_backup, dia_indicador, dic_tabelas_lojas)

#Calculando indicadores
dic_lojas_indicadores = {} #API
for loja in dic_tabelas_lojas:
    lojas_ano = dic_tabelas_lojas[loja]
    lojas_dia = lojas_ano.loc[lojas_ano['Data']==lojas_ano['Data'].max(), :]

    faturamento_dia, faturamento_ano = CalcularIndicadores().calcular_faturamento_diaAno(lojas_dia, lojas_ano)

    diversidade_produto_dia, diversidade_produto_ano = CalcularIndicadores().calcular_diversidade_produto_diaAno(lojas_dia,lojas_ano)

    ticket_medio_dia, ticket_medio_ano = CalcularIndicadores().calcular_ticketMedio_diaAno(lojas_dia, lojas_ano)