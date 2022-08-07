import time
import pandas as pd
from ManipularDados import ManipularDados
from OrganizarPlanilhasPastas import separar_por_loja, organizar_pastas, criar_pasta_backup_lojas
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

#Criando pastas das lojas e colocando a planilha de cada loja em sua respectiva pasta
criar_pasta_backup_lojas()
caminho_backup = r'C:\Users\Renan\Desktop\AutomacaoIndicadores\Backup Arquivos Lojas'
organizar_pastas(caminho_backup,dia_indicador, dic_tabelas_lojas)

#percorrendo todas as lojas
for loja in dic_tabelas_lojas:
    lojas_ano = dic_tabelas_lojas[loja]
    lojas_dia = lojas_ano.loc[lojas_ano['Data']==lojas_ano['Data'].max(), :]

    #Calculando indicadores
    manipular_dados = ManipularDados(lojas_dia, lojas_ano, dia_indicador)
    faturamento_dia, faturamento_ano = manipular_dados.calcular_faturamento_diaAno()
    diversidade_produto_dia, diversidade_produto_ano = manipular_dados.calcular_diversidade_produto_diaAno()
    ticket_medio_dia, ticket_medio_ano = manipular_dados.calcular_ticketMedio_diaAno()

    #Construção do e-mail para os gerentes
    nome = emails_df.loc[emails_df['Loja'] == loja, 'Gerente'].values[0]
    criar_email = CriarEmail(loja,nome,dia_indicador, faturamento_dia,faturamento_ano,ticket_medio_dia, ticket_medio_ano,
                             diversidade_produto_dia,diversidade_produto_ano)
    criar_email.encaminhar_email_gerencia(emails_df,caminho_backup)

    time.sleep(3)

#Criando rankings e salvando como arquivos excel
ranking_faturamento_lojasDia, ranking_faturamento_lojasAno = manipular_dados.criar_rankingLojas_diaAno(vendas_df)
caminho_ranking_dia = fr'{caminho_backup}\Ranking_Diário{dia_indicador.month}_{dia_indicador.day}.xlsx'
caminho_ranking_ano = fr'{caminho_backup}\Ranking_Anual{dia_indicador.month}_{dia_indicador.day}.xlsx'

#Salvar os rankings na pasta de Backup
manipular_dados.criar_excel(ranking_faturamento_lojasDia, ranking_faturamento_lojasAno, caminho_ranking_dia, caminho_ranking_ano)
time.sleep(0.5)

#Criando e encaminhando e-mail para a diretoria
email_diretoria = criar_email.criar_email_diretoria(ranking_faturamento_lojasDia, ranking_faturamento_lojasAno)
criar_email.encaminhar_email_diretoria(emails_df, email_diretoria,caminho_ranking_ano, caminho_ranking_dia)