import time
import pandas as pd
from ManipularDados import ManipularDados
from OrganizarPlanilhasPastas import separar_por_loja, organizar_pastas
from EncaminharEmail import CriarEmail



#Importando planilhas
caminho_baseDados = r'C:\Users\Renan\Desktop\AutomacaoIndicadores\Bases de Dados'
emails_df = pd.read_excel(rf'{caminho_baseDados}\Emails.xlsx')
lojas_df = pd.read_csv(rf'{caminho_baseDados}\Lojas.csv', sep=';', encoding='latin1')
vendas_df = pd.read_excel(rf'{caminho_baseDados}\Vendas.xlsx')

#Definindo dia do indicador a ser calculado e criando 1 planilha para cada loja
dia_indicador = vendas_df['Data'].max()
vendas_df = vendas_df.merge(lojas_df, on='ID Loja')
dic_tabelas_lojas = separar_por_loja(lojas_df, vendas_df)

#Criando pastas das lojas e colocando uma planilha de loja em sua respectiva pasta
caminho_backup = r'C:\Users\Renan\Desktop\AutomacaoIndicadores\Backup Arquivos Lojas'
organizar_pastas(caminho_backup,dia_indicador, dic_tabelas_lojas)

#percorrendo todas as lojas
for loja in dic_tabelas_lojas:
    lojas_ano = dic_tabelas_lojas[loja]
    lojas_dia = lojas_ano.loc[lojas_ano['Data']==lojas_ano['Data'].max(), :]

    # Calculando indicadores
    calcular = ManipularDados(lojas_dia, lojas_ano)
    faturamento_dia, faturamento_ano = calcular.calcular_faturamento_diaAno()
    diversidade_produto_dia, diversidade_produto_ano = calcular.calcular_diversidade_produto_diaAno()
    ticket_medio_dia, ticket_medio_ano = calcular.calcular_ticketMedio_diaAno()

    #Construção do e-mail para os gerentes:
    nome = emails_df.loc[emails_df['Loja'] == loja, 'Gerente'].values[0]
    criar_email = CriarEmail(loja,nome,dia_indicador, faturamento_dia,faturamento_ano,ticket_medio_dia, ticket_medio_ano,
                             diversidade_produto_dia,diversidade_produto_ano)
    criar_email.encaminhar_email_gerencia(emails_df,caminho_backup)

    time.sleep(3)