from pathlib import Path
class ManipularDados():
    def __init__(self):
        pass


    def separar_por_loja(self, lojas_df, vendas_df):
        dic_tabelas_lojas = {}
        for loja in lojas_df['Loja']:
            dic_tabelas_lojas[loja] = vendas_df.loc[vendas_df['Loja']==loja, :]
        return dic_tabelas_lojas

    def organizar_pastas(self, caminho_backup, dia_indicador, dic_tabelas_lojas):
        caminho_backup = Path(caminho_backup)
        arquivos = caminho_backup.iterdir()
        lista_lojas = [arquivo.name for arquivo in arquivos]
        for loja in dic_tabelas_lojas:
            if loja not in lista_lojas:
                Path(caminho_backup / f'{loja}').mkdir()
                arquivo_nome = f'{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx'
                dic_tabelas_lojas[loja].to_excel(Path(caminho_backup / loja / arquivo_nome))


class CalcularIndicadores():
    def __init__(self):
        pass


    def calcular_faturamento_diaAno(self, lojas_dia, lojas_ano):
        faturamento_dia = lojas_dia['Valor Final'].sum()
        faturamento_ano = lojas_ano['Valor Final'].sum()
        return faturamento_dia, faturamento_ano


    def calcular_diversidade_produto_diaAno(self, lojas_dia, lojas_ano):
        diversidade_produto_dia = len(lojas_dia['Produto'].unique())
        diversiade_produto_ano = len(lojas_ano['Produto'].unique())
        return diversidade_produto_dia, diversiade_produto_ano


    def calcular_ticketMedio_diaAno(self,lojas_dia, lojas_ano):
        valor_venda_dia = lojas_dia.groupby('Código Venda').sum()
        ticket_medio_dia = valor_venda_dia['Valor Final'].mean()
        valor_venda_ano = lojas_ano.groupby('Código Venda').sum()
        ticket_medio_ano = valor_venda_ano['Valor Final'].mean()
        return ticket_medio_dia, ticket_medio_ano



