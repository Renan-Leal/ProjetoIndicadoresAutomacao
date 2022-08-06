class ManipularDados():
    def __init__(self, lojas_dia, lojas_ano):
        self.lojas_dia = lojas_dia
        self.lojas_ano = lojas_ano


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