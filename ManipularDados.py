class ManipularDados():
    def __init__(self, lojas_dia, lojas_ano, dia_indicador):
        self.lojas_dia = lojas_dia
        self.lojas_ano = lojas_ano
        self.dia_indicador = dia_indicador


    def calcular_faturamento_diaAno(self):
        faturamento_dia = self.lojas_dia['Valor Final'].sum()
        faturamento_ano = self.lojas_ano['Valor Final'].sum()

        return faturamento_dia, faturamento_ano


    def calcular_diversidade_produto_diaAno(self):
        diversidade_produto_dia = len(self.lojas_dia['Produto'].unique())
        diversiade_produto_ano = len(self.lojas_ano['Produto'].unique())

        return diversidade_produto_dia, diversiade_produto_ano


    def calcular_ticketMedio_diaAno(self):
        valor_venda_dia = self.lojas_dia.groupby('Código Venda').sum()
        ticket_medio_dia = valor_venda_dia['Valor Final'].mean()
        valor_venda_ano = self.lojas_ano.groupby('Código Venda').sum()
        ticket_medio_ano = valor_venda_ano['Valor Final'].mean()

        return ticket_medio_dia, ticket_medio_ano

    def criar_rankingLojas_diaAno(self, vendas_df):
       #Ranking das lojas - Faturamento diário
        vendas_dia = vendas_df.loc[vendas_df['Data']==self.dia_indicador, :]
        ranking_faturamento_lojasDia = vendas_dia.groupby('Loja')[['Loja', 'Valor Final']].sum()
        ranking_faturamento_lojasDia = ranking_faturamento_lojasDia.sort_values(by='Valor Final', ascending=False)

        # Ranking faturamento ano.
        ranking_faturamento_lojasAno = vendas_df.groupby('Loja')[['Loja', 'Valor Final']].sum()
        ranking_faturamento_lojasAno = ranking_faturamento_lojasAno.sort_values(by='Valor Final', ascending=False)

        return ranking_faturamento_lojasDia, ranking_faturamento_lojasAno

    def criar_excel(self, ranking_faturamento_lojasDia, ranking_faturamento_lojasAno, caminho_ranking_dia,
                    caminho_ranking_ano):

        ranking_faturamento_lojasDia.to_excel(caminho_ranking_dia)
        ranking_faturamento_lojasAno.to_excel(caminho_ranking_ano)